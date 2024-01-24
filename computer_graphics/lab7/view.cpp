#include "view.h"
#include "iostream"

#include "math.h"

const double pi = 4 * atan(1);

View::View(QWidget *parent)
    : QWidget{parent}
{

    QPalette pal(palette());
    pal.setColor(QPalette::Window, Qt::white);
    setPalette(pal);

    setAutoFillBackground(true);

    p1 = QPointF(50, 50);
    p2 = QPointF(550, 50);
    p3 = QPointF(50, 550);
    p4 = QPointF(550, 550);
}

void View::paintEvent(QPaintEvent*) {

    int n = panel->accuracy();

    QPainter ptr = QPainter(this);
    ptr.setPen(Qt::blue);

    ptr.drawPoint(p1);
    ptr.drawEllipse(p1, 10, 10);
    ptr.drawPoint(p4);
    ptr.drawEllipse(p4, 10, 10);

    ptr.setPen(Qt::green);

    ptr.drawPoint(p2);
    ptr.drawEllipse(p2, 10, 10);
    ptr.drawPoint(p3);
    ptr.drawEllipse(p3, 10, 10);


    drawBezier(double(n));

}

void View::mouseMoveEvent(QMouseEvent *mo)
{

    QPointF dist1(p1.x() - mo->pos().x(), p1.y() - mo->pos().y());
    QPointF dist2(p2.x() - mo->pos().x(), p2.y() - mo->pos().y());
    QPointF dist3(p3.x() - mo->pos().x(), p3.y() - mo->pos().y());
    QPointF dist4(p4.x() - mo->pos().x(), p4.y() - mo->pos().y());

    if(mo->buttons() == Qt::LeftButton && sqrt(QPointF::dotProduct(dist1, dist1)) < 10) {
        p1 = mo->pos();
        update();
    }
    else if(mo->buttons() == Qt::LeftButton && sqrt(QPointF::dotProduct(dist2, dist2)) < 10) {
        p2 = mo->pos();
        update();
    }
    else if(mo->buttons() == Qt::LeftButton && sqrt(QPointF::dotProduct(dist3, dist3)) < 10) {
        p3 = mo->pos();
        update();
    }
    else if(mo->buttons() == Qt::LeftButton && sqrt(QPointF::dotProduct(dist4, dist4)) < 10) {
        p4 = mo->pos();
        update();
    }
}

Panel* View::controlPanel() {

    return panel;
}

void View::setControlPanel(Panel* p) {

    panel = p;
    update();
}

void View::drawBezier(double n)
{

    QPainter ptr = QPainter(this);
    ptr.setPen(Qt::red);

    QVector<QPointF> p;

    p.append(p1);

    QPointF p12 = QPointF(p2.x() - p1.x(), p2.y() - p1.y());
    QPointF p23 = QPointF(p3.x() - p2.x(), p3.y() - p2.y());
    QPointF p34 = QPointF(p4.x() - p3.x(), p4.y() - p3.y());


    for(double t = 1; t < n + 1; t++) {

        QPointF p12_t(t / n * p12.x(), t / n * p12.y());
        QPointF p23_t(t / n * p23.x(), t / n * p23.y());
        QPointF p34_t(t / t * p34.x(), t / n * p34.y());

        QPointF p12_23_t((1 - t / n) * p12.x() + p23_t.x(), (1 - t / n) * p12.y() + p23_t.y());
        QPointF p23_34_t((1 - t / n) * p23.x() + p34_t.x(), (1 - t / n) * p23.y() + p34_t.y());

        QPointF p12_23_34_t((1 - t / n) * p12_23_t.x() + t / n * p23_34_t.x(), (1 - t / n) * p12_23_t.y() + t / n * p23_34_t.y());

        QPointF p_next(p1.x() + p12_t.x() + t / n * p12_23_t.x() + t / n * p12_23_34_t.x(), p1.y() + p12_t.y() + t / n * p12_23_t.y() + t / n * p12_23_34_t.y());
        p.append(p_next);

    }

    p.append(p4);

    for(int i = 0; i < n + 1; i++) {

        ptr.drawLine(p[i], p[i + 1]);
    }

}
