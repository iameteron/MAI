#include "view.h"

#include <QPainter>
#include "iostream"

View::View(QWidget *parent)
    : QWidget{parent}
{

    QPalette pal(palette());
    pal.setColor(QPalette::Window, Qt::white);
    setPalette(pal);

    setAutoFillBackground(true);
}

void View::paintEvent(QPaintEvent*)
{

    double k_x = double(width()) / 578;
    double k_y = double(height()) / 578;

    const double pi = 4 * atan(1);
    const double a = this->panel->a_value();

    QPointF center(width() / 2, height() / 2);
    QPointF p1(a, 0);

    this->draw_axes(k_x, k_y);

    double steps = 10000;

    QPainter ptr(this);
    ptr.setPen(Qt::blue);

    for(int i = 0; i < 2 * steps; i++) {
        double t = 2 * pi * i / steps;
        double x = k_x * a * sqrt(cos(2 * t)) * cos(t);
        double y = k_y * a * sqrt(cos(2 * t)) * sin(t);

        QPointF p2(x, y);

        ptr.drawLine(center + p1, center + p2);

        p1 = p2;
    }
}

void View::draw_axes(double k_x, double k_y) {

    QPainter ptr(this);
    ptr.setPen(Qt::black);

    double w = double(width());
    double h = double(height());

    QPointF p1 = QPointF(w / 2, 0);
    QPointF p2 = QPointF(w / 2, h);
    QPointF p3 = QPointF(0, h / 2);
    QPointF p4 = QPointF(w, h / 2);

    ptr.drawLine(p1, p2);
    ptr.drawLine(p3, p4);

    for(int i = 1; i < 6; i++) {
        QPointF p1 = QPointF(w / 2 + 50 * i * k_x, h / 2 + 10 * k_y);
        QPointF p2 = QPointF(w / 2 + 50 * i * k_x, h / 2 - 10 * k_y);

        ptr.drawLine(p1, p2);

        QPointF p3 = QPointF(w / 2 - 50 * i * k_x, h / 2 + 10 * k_y);
        QPointF p4 = QPointF(w / 2 - 50 * i * k_x, h / 2 - 10 * k_y);

        ptr.drawLine(p3, p4);

        QPointF p5 = QPointF(w / 2 + 10 * k_x, h / 2 + 50 * i * k_y);
        QPointF p6 = QPointF(w / 2 - 10 * k_x, h / 2 + 50 * i * k_y);

        ptr.drawLine(p5, p6);

        QPointF p7 = QPointF(w / 2 + 10 * k_x, h / 2 - 50 * i * k_y);
        QPointF p8 = QPointF(w / 2 - 10 * k_x, h / 2 - 50 * i * k_y);

        ptr.drawLine(p7, p8);
    }
}

Panel* View::controlPanel() {

    return panel;
}

void View::setControlPanel(Panel* p) {

    panel = p;
    update();
}

