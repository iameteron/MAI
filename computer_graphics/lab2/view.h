#ifndef VIEW_H
#define VIEW_H

#include <QWidget>

#include "panel.h"

class View : public QWidget
{
    Q_OBJECT
public:
    explicit View(QWidget *parent = nullptr);

    Panel* controlPanel();
    void setControlPanel(Panel* p);
    void draw_wedge(double** plane_points, int* edges_status);
    void draw_axes();

protected:
    void paintEvent(QPaintEvent*);

private:
    Panel* panel;

};

#endif // VIEW_H
