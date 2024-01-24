#ifndef VIEW_H
#define VIEW_H

#include <QWidget>
#include <QMouseEvent>
#include <QPainter>

#include "panel.h"

class View : public QWidget
{
    Q_OBJECT
public:
    explicit View(QWidget *parent = nullptr);

    Panel* controlPanel();
    void setControlPanel(Panel* p);

    void drawBezier(double n);

protected:
    void paintEvent(QPaintEvent*);

    virtual void mouseMoveEvent(QMouseEvent*);

private:
    Panel* panel;
    QPoint mPos;

    QPointF p1;
    QPointF p2;
    QPointF p3;
    QPointF p4;


};

#endif // VIEW_H
