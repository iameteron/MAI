#ifndef OPERATIONS_H
#define OPERATIONS_H

#include "math.h"

class Operations
{
public:
    Operations();

    double** rotate_OY(double** points, int n, double phi);
    double** rotate_OX(double** points, int n, double phi);
    double** rotate_OZ(double** points, int n, double phi);
    double** scale(double** points, int n, double lambda);

    int* roberts_algorithm(double** normals);
};

#endif // OPERATIONS_H
