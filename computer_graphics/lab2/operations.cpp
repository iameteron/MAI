#include "operations.h"

Operations::Operations()
{

}

double** Operations::rotate_OY(double **points, int n, double phi) {

    double** new_points = new double*[n];
    for(int i = 0; i < n; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < n; i++) {
        new_points[i][0] = points[i][0] * cos(phi) - points[i][2] * sin(phi);
        new_points[i][1] = points[i][1];
        new_points[i][2] = points[i][0] * sin(phi) + points[i][2] * cos(phi);
    }

    return new_points;
}

double** Operations::rotate_OX(double **points, int n, double phi) {

    double** new_points = new double*[n];
    for(int i = 0; i < n; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < n; i++) {
        new_points[i][0] = points[i][0];
        new_points[i][1] = points[i][1] * cos(phi) - points[i][2] * sin(phi);
        new_points[i][2] = points[i][1] * sin(phi) + points[i][2] * cos(phi);
    }

    return new_points;
}

double** Operations::rotate_OZ(double **points, int n, double phi) {

    double** new_points = new double*[n];
    for(int i = 0; i < n; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < n; i++) {
        new_points[i][0] = points[i][0] * cos(phi) - points[i][1] * sin(phi);
        new_points[i][1] = points[i][0] * sin(phi) + points[i][1] * cos(phi);
        new_points[i][2] = points[i][2];
    }

    return new_points;
}

double** Operations::scale(double **points, int n, double scaler) {

    double** new_points = new double*[n];
    for(int i = 0; i < n; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < n; i++) {
        new_points[i][0] = scaler * points[i][0];
        new_points[i][1] = scaler * points[i][1];
        new_points[i][2] = scaler * points[i][2];
    }

    return new_points;
}

double dot_product(double x[3], double y[3]) {

    return x[0] * y[0] + x[1] * y[1] + x[2] * y[2];
}

int* Operations::roberts_algorithm(double** normals) {

    int* edges_status = new int[9];
    for(int i = 0; i < 9; i++) {
        edges_status[i] = 0;
    }

    double n_0[3] = {0, 0, 100};

    if(dot_product(n_0, normals[0]) > 0) {
        edges_status[3] = edges_status[4] = edges_status[5] = 1;
    }
    if(dot_product(n_0, normals[1]) > 0) {
        edges_status[1] = edges_status[6] = edges_status[7] = 1;
    }
    if(dot_product(n_0, normals[2]) > 0) {
        edges_status[2] = edges_status[5] = edges_status[7] = edges_status[8] = 1;
    }
    if(dot_product(n_0, normals[3]) > 0) {
        edges_status[0] = edges_status[4] = edges_status[6] = edges_status[8] = 1;
    }
    if(dot_product(n_0, normals[4]) > 0) {
        edges_status[0] = edges_status[1] = edges_status[2] = edges_status[3] = 1;
    }

    return edges_status;
}

