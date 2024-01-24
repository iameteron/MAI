#ifndef WEDGE_H
#define WEDGE_H

#include "widget.h"

class Wedge
{
public:
    Wedge();
    double** get_points(double a, double b);

    double** get_normals(double** points);

private:
    double points[6][3];
    double normals[5][3];
};

#endif // WEDGE_H
