#ifndef HEMISPHERE_H
#define HEMISPHERE_H

#include "widget.h"

class Hemisphere
{
public:
    Hemisphere(int parallels, int meridians);
    double** get_points(double a, double b, int n);

    double** get_normals(double** points, int n, int m);

private:
    double** points;
    double** normals;
};

#endif // HEMISPHERE_H
