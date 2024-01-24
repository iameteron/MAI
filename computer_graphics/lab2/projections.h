#ifndef PROJECTIONS_H
#define PROJECTIONS_H


class Projections
{
public:
    Projections();

    double** Orthogonal_Projection(double** points);
    double** Perspective_Projection(double** perspective_points);

    double** Perspective_Points(double** points, double distance);
    double** Perspective_Normals(double** normals, double distance);
};

#endif // PROJECTIONS_H
