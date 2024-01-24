#include "wedge.h"

Wedge::Wedge() {

    points[0][0] = -50, points[0][1] = 0, 	points[0][2] = -50;
    points[1][0] =  50,	points[1][1] = 0, 	points[1][2] = -50;
    points[2][0] =  50, points[2][1] = 0, 	points[2][2] =  50;
    points[3][0] = -50,	points[3][1] = 0, 	points[3][2] =  50;
    points[4][0] = -50,	points[4][1] = 100, points[4][2] = 	0;
    points[5][0] =  50, points[5][1] = 100,	points[5][2] =  0;

}

double** Wedge::get_points(double a, double b) {

    double** p = new double*[6];
    for(int i = 0; i < 6; i++) {
        p[i] = new double[3];
        p[i][0] = a * points[i][0];
        p[i][1] = b * points[i][1];
        p[i][2] = points[i][2];

    }

    return p;
}

double* cross_product(double* x, double* y) {

    double* z = new double[3];
    z[0] =   x[1] * y[2] - x[2] * y[1];
    z[1] = - x[0] * y[2] + x[2] * y[0];
    z[2] =   x[0] * y[1] - x[1] * y[0];
    return z;
}

double** Wedge::get_normals(double** points) {

    double** normals = new double*[5];

    double* AD = new double[3];
    double* AE = new double[3];
    double* BF = new double[3];
    double* BC = new double[3];
    double* DC = new double[3];
    double* DE = new double[3];
    double* AB = new double[3];

    for(int i = 0; i < 3; i++) {
        AD[i] = points[3][i] - points[0][i];
        AE[i] = points[4][i] - points[0][i];
        BF[i] = points[5][i] - points[1][i];
        BC[i] = points[2][i] - points[1][i];
        DC[i] = points[2][i] - points[3][i];
        DE[i] = points[4][i] - points[3][i];
        AB[i] = points[1][i] - points[0][i];

    }

    normals[0] = cross_product(AD, AE);
    normals[1] = cross_product(BF, BC);
    normals[2] = cross_product(DC, DE);
    normals[3] = cross_product(AE, AB);
    normals[4] = cross_product(AB, AD);

    return normals;
}
