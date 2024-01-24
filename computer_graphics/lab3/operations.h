#ifndef OPERATIONS_H
#define OPERATIONS_H

#include "math.h"

class Operations
{
public:
    Operations();

    double** rotate_OY(double** points, int N, double phi);
    double** rotate_OX(double** points, int N, double phi);
    double** rotate_OZ(double** points, int N, double phi);
    double** scale(double** points, int N, double lambda);

    int* roberts_algorithm(double** normals, int N);
    double* phong_lighting_model(double** perspective_points, double** normals, double distance, int n, int m);
};

#endif // OPERATIONS_H
