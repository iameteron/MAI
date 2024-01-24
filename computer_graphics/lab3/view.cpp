#include "view.h"

#include <QPainter>
#include <QPainterPath>
#include <QBrush>

#include "math.h"
#include "hemisphere.h"
#include "operations.h"
#include "projections.h"

const double pi = 4 * atan(1);

View::View(QWidget *parent)
    : QWidget{parent}
{

    QPalette pal(palette());
    pal.setColor(QPalette::Window, Qt::white);
    setPalette(pal);

    setAutoFillBackground(true);
}

void View::paintEvent(QPaintEvent*) {

    if(!panel) {
        return;
    }

    double w = double(width());
    double h = double(height());

    this->center_x = w / 2;
    this->center_y = h / 2;
    this->k_x = w / 578;
    this->k_y = h / 578;

    this->draw_axes();

    double OY_angle = this->panel->angle_turn_OY() * (2 * pi) / 360;
    double OX_angle = this->panel->angle_turn_OX() * (2 * pi) / 360;
    double OZ_angle = this->panel->angle_turn_OZ() * (2 * pi) / 360;

    this->distance = this->panel->distance();
    this->frame_state = this->panel->frame_state();
    this->illustrated_figure_state = this->panel->illustrated_figure_state();

    double parallels = this->panel->parallels();
    double meridians = this->panel->meridians();

    this->n = meridians;
    this->m = parallels;
    this->N = n * m + 1;

    Hemisphere hemisphere(meridians, parallels);
    double** points = hemisphere.get_points(1, 1, N);

    Operations operations;
    double** new_points = new double*;

    new_points = operations.rotate_OY(points, N, OY_angle);
    new_points = operations.rotate_OX(new_points, N, OX_angle);
    new_points = operations.rotate_OZ(new_points, N, OZ_angle);

    Projections projections;

    double** perspective_points = projections.Perspective_Points(new_points, distance, N);
    double** plane_points = projections.Perspective_Projection(perspective_points, N);

    double** normals = hemisphere.get_normals(perspective_points, meridians, parallels);

    double* edges_lighting = operations.phong_lighting_model(perspective_points, normals, distance, n, m);
    int* edges_status = operations.roberts_algorithm(normals, N);

    draw_hemisphere(plane_points, edges_status, edges_lighting);

}

void View::draw_lower_center(double** plane_points, int* edges_status, double* edges_lighting) {

    QPainter ptr(this);
    ptr.setPen(Qt::black);

    QPointF lower_center(center_x, center_y);

    if(edges_status[N] == 1) {
        for(int i = 0; i < n; i++) {

            QBrush brush(QColor(edges_lighting[m * n + i], edges_lighting[m * n + i], edges_lighting[m * n + i], 255));


            QPointF p1(center_x + k_x * plane_points[i][0], center_y + k_y * plane_points[i][1]);
            QPointF p2(center_x + k_x * plane_points[(i + 1) % n][0], center_y + k_y * plane_points[(i + 1) % n][1]);

            if(frame_state == 1) {
                ptr.drawLine(lower_center, p1);
                ptr.drawLine(p1, p2);
                ptr.drawLine(p2, lower_center);
            }

            if(illustrated_figure_state == 1) {
            QPainterPath path;
                path.moveTo(lower_center);
                path.lineTo(p1);
                path.lineTo(p2);
                path.lineTo(lower_center);

                ptr.fillPath(path, brush);
            }
        }
    }
}

void View::draw_upper_center(double** plane_points, int* edges_status, double* edges_lighting) {

    QPainter ptr(this);
    ptr.setPen(Qt::black);

    QPointF upper_center(center_x + k_x * plane_points[N - 1][0], center_y + k_y * plane_points[N - 1][1]);

    for(int i = 0; i < n; i++) {
        QPointF p1(center_x + k_x * plane_points[(m - 1) * n + i][0],
                   center_y + k_y * plane_points[(m - 1) * n + i][1]);

        if(edges_status[(m - 1) * n + i] == 1) {

            QBrush brush(QColor(edges_lighting[(m - 1) * n + i], edges_lighting[(m - 1) * n + i], edges_lighting[(m - 1) * n + i], 255));

            QPointF p2(center_x + k_x * plane_points[(m - 1) * n + (i + 1) % n][0],
                       center_y + k_y * plane_points[(m - 1) * n + (i + 1) % n][1]);

            if(frame_state == 1) {
                ptr.drawLine(upper_center, p1);
                ptr.drawLine(p1, p2);
                ptr.drawLine(p2, upper_center);
            }

            if(illustrated_figure_state == 1) {
                QPainterPath path;
                path.moveTo(upper_center);
                path.lineTo(p1);
                path.lineTo(p2);
                path.lineTo(upper_center);

                ptr.fillPath(path, brush);
            }
        }
    }
}

void View::draw_main_hull(double** plane_points, int* edges_status, double* edges_lighting) {

    QPainter ptr(this);
    ptr.setPen(Qt::black);

    QPointF center(center_x, center_y);

    for(int i = 0; i < n * (m - 1); i++) {
        QPointF p1(center_x + k_x * plane_points[i][0], center_y + k_y * plane_points[i][1]);
        if(edges_status[i] == 1) {

            QBrush brush(QColor(edges_lighting[i], edges_lighting[i] , edges_lighting[i], 255));

            int j = i;

            if((i + 1) % n == 0) {
                j = i - n;
            }

            QPointF p2(center_x + k_x * plane_points[j + 1][0], 	center_y + k_y * plane_points[j + 1][1]);
            QPointF p3(center_x + k_x * plane_points[i + n][0], 	center_y + k_y * plane_points[i + n][1]);
            QPointF p4(center_x + k_x * plane_points[j + n + 1][0], center_y + k_y * plane_points[j + n + 1][1]);

            if(frame_state == 1) {
                ptr.drawLine(p1, p2);
                ptr.drawLine(p1, p3);
                ptr.drawLine(p2, p4);
                ptr.drawLine(p3, p4);
            }

            if(illustrated_figure_state == 1) {
                QPainterPath path;
                path.moveTo(p1);
                path.lineTo(p2);
                path.lineTo(p4);
                path.lineTo(p3);
                path.lineTo(p1);

                ptr.fillPath(path, brush);
            }
        }
    }
}

void View::draw_hemisphere(double** plane_points, int* edges_status, double* edges_lighting) {

    this->draw_main_hull(plane_points, edges_status, edges_lighting);
    this->draw_upper_center(plane_points, edges_status, edges_lighting);
    this->draw_lower_center(plane_points, edges_status, edges_lighting);

}

void View::draw_axes() {

    QPainter ptr(this);
    QPointF p1 = QPointF(center_x, 0);
    QPointF p2 = QPointF(center_x, 2 * center_y);
    QPointF p3 = QPointF(0, center_y);
    QPointF p4 = QPointF(2 * center_x, center_y);

    ptr.drawLine(p1, p2);
    ptr.drawLine(p3, p4);
}

Panel* View::controlPanel() {

    return panel;
}

void View::setControlPanel(Panel* p) {

    panel = p;
    update();
}
