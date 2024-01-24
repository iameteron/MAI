#ifndef PROJECTIONS_H
#define PROJECTIONS_H


class Projections
{
public:
    Projections();

    double** Orthogonal_Projection(double** points, int N);
    double** Perspective_Projection(double** perspective_points, int N);
    double** Perspective_Points(double** points, double distance, int N);
};

#endif // PROJECTIONS_H
