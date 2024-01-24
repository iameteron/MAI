#include "view.h"

#include <QPainter>

#include "math.h"
#include "wedge.h"
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

    this->draw_axes();

    double OY_angle = this->panel->angle_turn_OY() * (2 * pi) / 360;
    double OX_angle = this->panel->angle_turn_OX() * (2 * pi) / 360;
    double OZ_angle = this->panel->angle_turn_OZ() * (2 * pi) / 360;
    double distance = this->panel->distance();

    Wedge wedge;
    double** points = wedge.get_points(1, 1);

    Operations operations;
    double** new_points = new double*;

    new_points = operations.rotate_OY(points, 6, OY_angle);
    new_points = operations.rotate_OX(new_points, 6, OX_angle);
    new_points = operations.rotate_OZ(new_points, 6, OZ_angle);


    Projections projections;

    double** perspective_points = projections.Perspective_Points(new_points, distance);
    double** normals = wedge.get_normals(perspective_points);
    int* edges_status = operations.roberts_algorithm(normals);
    double** plane_points = projections.Perspective_Projection(perspective_points);
    this->draw_wedge(plane_points, edges_status);

}

void View::draw_wedge(double** plane_points, int* edges_status) {

    QPainter ptr(this);
    ptr.setPen(Qt::blue);

    double w = double(width());
    double h = double(height());

    double center_x = w / 2;
    double center_y = h / 2;
    double k_x = w / 578;
    double k_y = h / 578;

    QPointF center(center_x, center_y);

    QPointF p1(center_x + k_x * plane_points[0][0], center_y + k_y * plane_points[0][1]);
    QPointF p2(center_x + k_x * plane_points[1][0], center_y + k_y * plane_points[1][1]);
    QPointF p3(center_x + k_x * plane_points[2][0], center_y + k_y * plane_points[2][1]);
    QPointF p4(center_x + k_x * plane_points[3][0], center_y + k_y * plane_points[3][1]);
    QPointF p5(center_x + k_x * plane_points[4][0], center_y + k_y * plane_points[4][1]);
    QPointF p6(center_x + k_x * plane_points[5][0], center_y + k_y * plane_points[5][1]);

    if(edges_status[0] == 1) {
        ptr.drawLine(p1, p2);
    }
    if(edges_status[1] == 1) {
        ptr.drawLine(p2, p3);
    }
    if(edges_status[2] == 1) {
        ptr.drawLine(p3, p4);
    }
    if(edges_status[3] == 1) {
        ptr.drawLine(p1, p4);
    }
    if(edges_status[4] == 1) {
        ptr.drawLine(p1, p5);
    }
    if(edges_status[5] == 1) {
        ptr.drawLine(p4, p5);
    }
    if(edges_status[6] == 1) {
        ptr.drawLine(p2, p6);
    }
    if(edges_status[7] == 1) {
        ptr.drawLine(p3, p6);
    }
    if(edges_status[8] == 1) {
        ptr.drawLine(p5, p6);
    }

}

void View::draw_axes() {

    QPainter ptr(this);
    QPointF p1 = QPointF(width() / 2, 0);
    QPointF p2 = QPointF(width() / 2, height());
    QPointF p3 = QPointF(0, height() / 2);
    QPointF p4 = QPointF(width(), height() / 2);

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
