#include "projections.h"

Projections::Projections()
{

}

double** Projections::Orthogonal_Projection(double **points, int N) {

    double** projection = new double*[N];
    for(int i = 0; i < N; i++) {
       projection[i] = new double[2];
       for(int j = 0; j < 2; j++) {
           projection[i][j] = points[i][j];
       }
    }

    return projection;
}

double** Projections::Perspective_Projection(double** perspective_points, int N) {

    double** projection = new double*[N];
    for(int i = 0; i < N; i++) {
       projection[i] = new double[2];
       for(int j = 0; j < 2; j++) {
           projection[i][j] = perspective_points[i][j];
       }
    }

    return projection;
}

double** Projections::Perspective_Points(double** points, double distance, int N) {

    double** perspective_points = new double*[N];
    for(int i = 0; i < N; i++) {
       perspective_points[i] = new double[3];
       perspective_points[i][2] = points[i][2];
       for(int j = 0; j < 2; j++) {
           //perspective_points[i][j] = distance * points[i][j] / (distance - points[i][2] + 1);
           perspective_points[i][j] = points[i][j] / ((-1 / distance) * points[i][2] + 1);
       }
    }

    return perspective_points;

}

