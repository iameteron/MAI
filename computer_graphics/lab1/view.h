#ifndef VIEW_H
#define VIEW_H

#include <QWidget>

#include "panel.h"

class View : public QWidget
{
    Q_OBJECT
public:
    explicit View(QWidget *parent = nullptr);
    void setControlPanel(Panel* p);
    Panel* controlPanel();
    void draw_axes(double k_x, double k_y);


protected:
    void paintEvent(QPaintEvent*);

private:
    Panel* panel;

};

#endif // VIEW_H
