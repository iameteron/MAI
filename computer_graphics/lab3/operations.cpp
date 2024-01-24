#include "operations.h"

Operations::Operations()
{

}

double** Operations::rotate_OY(double **points, int N, double phi) {

    double** new_points = new double*[N];
    for(int i = 0; i < N; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < N; i++) {
        new_points[i][0] = points[i][0] * cos(phi) - points[i][2] * sin(phi);
        new_points[i][1] = points[i][1];
        new_points[i][2] = points[i][0] * sin(phi) + points[i][2] * cos(phi);
    }

    return new_points;
}

double** Operations::rotate_OX(double **points, int N, double phi) {

    double** new_points = new double*[N];
    for(int i = 0; i < N; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < N; i++) {
        new_points[i][0] = points[i][0];
        new_points[i][1] = points[i][1] * cos(phi) - points[i][2] * sin(phi);
        new_points[i][2] = points[i][1] * sin(phi) + points[i][2] * cos(phi);
    }

    return new_points;
}

double** Operations::rotate_OZ(double **points, int N, double phi) {

    double** new_points = new double*[N];
    for(int i = 0; i < N; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < N; i++) {
        new_points[i][0] = points[i][0] * cos(phi) - points[i][1] * sin(phi);
        new_points[i][1] = points[i][0] * sin(phi) + points[i][1] * cos(phi);
        new_points[i][2] = points[i][2];
    }

    return new_points;
}

double** Operations::scale(double **points, int N, double scaler) {

    double** new_points = new double*[N];
    for(int i = 0; i < N; i++) {
        new_points[i] = new double[3];
    }

    for(int i = 0; i < N; i++) {
        new_points[i][0] = scaler * points[i][0];
        new_points[i][1] = scaler * points[i][1];
        new_points[i][2] = scaler * points[i][2];
    }

    return new_points;
}

double dot_product(double x[3], double y[3]) {

    return x[0] * y[0] + x[1] * y[1] + x[2] * y[2];
}

int* Operations::roberts_algorithm(double** normals, int N) {

    int* edges_status = new int[N + 1];

    double n_0[3] = {0, 0, 1};

    for(int i = 0; i < N + 1; i++) {
        double n[3] = {normals[i][0], normals[i][1], normals[i][2]};
        if(dot_product(n, n_0) > 0) {
            edges_status[i] = 1;
        }
        else {
            edges_status[i] = 0;
        }
    }

    return edges_status;
}

double* Operations::phong_lighting_model(double** perspective_points, double** normals, double distance, int n, int m) {

    int N = n * m + 1;

    double k_a = 1;
    double i_a = 75;

    double k_d = 1;
    double i_d = 75;

    double k_s = 1;
    double i_s = 75;
    double alpha = 2;

    double light_source[3] = {0, 0, distance};

    double* edges_lighting = new double[n * (m + 1)];

    double** l = new double*[n * (m + 1)];
    for(int i = 0; i < n * m; i++) {
        l[i] = new double[3];

        double norm = sqrt((light_source[0] - perspective_points[i][0]) * (light_source[0] - perspective_points[i][0]) +
                           (light_source[1] - perspective_points[i][1]) * (light_source[1] - perspective_points[i][1]) +
                           (light_source[2] - perspective_points[i][2]) * (light_source[2] - perspective_points[i][2]));

        for(int j = 0; j < 3; j++) {
            l[i][j] = (light_source[j] - perspective_points[i][j]) / norm;
        }
    }

    for(int i = 0; i < n; i++) {
        l[i + (n * m)] = new double[3];

        double norm = sqrt((light_source[0] - perspective_points[i][0]) * (light_source[0] - perspective_points[i][0]) +
                           (light_source[1] - perspective_points[i][1]) * (light_source[1] - perspective_points[i][1]) +
                           (light_source[2] - perspective_points[i][2]) * (light_source[2] - perspective_points[i][2]));

        for(int j = 0; j < 3; j++) {
            l[i + (n * m)][j] = (light_source[j] - perspective_points[i][j]) / norm;
        }
    }

    for(int i = 0; i < n * (m + 1); i++) {
        if(i >= n * m) {
            double cos_NL = dot_product(normals[N], l[i]);
            edges_lighting[i] = k_a * i_a + k_d * cos_NL * i_d + k_s * pow(2 * cos_NL * cos_NL - 1, alpha) * i_s;
        }
        if(i < n * m) {
            double cos_NL = dot_product(normals[i], l[i]);
            edges_lighting[i] = k_a * i_a + k_d * cos_NL * i_d + k_s * pow(2 * cos_NL * cos_NL - 1, alpha) * i_s;
        }
    }

    return edges_lighting;
}

