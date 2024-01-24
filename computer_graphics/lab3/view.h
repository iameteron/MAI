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

    void draw_axes();

    void draw_hemisphere(double** plane_points, int* edges_status, double* edges_lighting);
    void draw_lower_center(double** plane_points, int* edges_status, double* edges_lighting);
    void draw_upper_center(double** plane_points, int* edges_status, double* edges_lighting);
    void draw_main_hull(double** plane_points, int* edges_status, double* edges_lighting);

    void fill_hemisphere(double** plane_points);

protected:
    void paintEvent(QPaintEvent*);

private:
    Panel* panel;

    double distance;
    int frame_state;
    int illustrated_figure_state;

    double k_x;
    double k_y;
    double center_x;
    double center_y;

    int n;
    int m;
    int N;

};

#endif // VIEW_H
