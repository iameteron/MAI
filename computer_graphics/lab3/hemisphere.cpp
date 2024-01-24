#include "hemisphere.h"

const double pi = 3.14;

Hemisphere::Hemisphere(int n, int  m) {

    int N = n * m + 1;

    double* phi = new double[n];
    for(int i = 0; i < n; i++) {
        phi[i] = (2 * pi) * i / n;
    }

    double* theta = new double[m];
    for(int i = 0; i < m; i++) {
        theta[i] = (pi / 2) * i / m;
    }

    points = new double*[N];

    for(int i = 0; i < N; i++) {
        points[i] = new double[3];
    }

    double r = 200;
    for(int i = 0; i < N - 1; i++) {

        double phi_curr = phi[i % n];
        double theta_curr = theta[i / n];

        points[i][0] = r * cos(theta_curr) * cos(phi_curr);
        points[i][1] = r * cos(theta_curr) * sin(phi_curr);
        points[i][2] = r * sin(theta_curr);
    }
    points[N - 1][0] = 0;
    points[N - 1][1] = 0;
    points[N - 1][2] = r;

}

double** Hemisphere::get_points(double a, double b, int N) {

    double** p = new double*[N];
    for(int i = 0; i < N; i++) {
        p[i] = new double[3];
        p[i][0] = a * points[i][0];
        p[i][1] = b * points[i][1];
        p[i][2] = points[i][2];

    }

    return p;
}

double* cross_product(double x[], double y[]) {

    double* z = new double[3];
    z[0] =   x[1] * y[2] - x[2] * y[1];
    z[1] = - x[0] * y[2] + x[2] * y[0];
    z[2] =   x[0] * y[1] - x[1] * y[0];
    return z;
}

double** Hemisphere::get_normals(double** points, int n, int m) {

    int N = n * m + 1;

    double** normals = new double*[N + 1];

    for(int i = 0; i < n * (m - 1); i++) {
        double p1[3] = {points[i + 1][0] - points[i][0],
                        points[i + 1][1] - points[i][1],
                        points[i + 1][2] - points[i][2]};

        double p2[3] = {points[i + n][0] - points[i][0],
                        points[i + n][1] - points[i][1],
                        points[i + n][2] - points[i][2]};

        normals[i] = cross_product(p1, p2);
        double norm = sqrt(normals[i][0] * normals[i][0] + normals[i][1] * normals[i][1] + normals[i][2] * normals[i][2]);
        for(int j = 0; j < 3; j++) {
            normals[i][j] /= norm;
        }
    }

    for(int i = n * (m - 1); i < n * m; i++) {

        int j = i;
        if((i + 1) % n == 0) {
            j = i - n;
        }

        double p1[3] = {points[j + 1][0] - points[i][0],
                        points[j + 1][1] - points[i][1],
                        points[j + 1][2] - points[i][2]};

        double p2[3] = {points[N - 1][0] - points[i][0],
                        points[N - 1][1] - points[i][1],
                        points[N - 1][2] - points[i][2]};

        normals[i] = cross_product(p1, p2);

        double norm = sqrt(normals[i][0] * normals[i][0] + normals[i][1] * normals[i][1] + normals[i][2] * normals[i][2]);
        for(int j = 0; j < 3; j++) {
            normals[i][j] /= norm;
        }
    }

    double p1[3] = {points[0][0], points[0][1], points[0][2]};
    double p2[3] = {points[1][0], points[1][1], points[1][2]};

    normals[N - 1] = cross_product(p1, p2);
    double norm = sqrt(normals[N - 1][0] * normals[N - 1][0] + normals[N - 1][1] * normals[N - 1][1] + normals[N - 1][2] * normals[N - 1][2]);
    for(int j = 0; j < 3; j++) {
        normals[N - 1][j] /= norm;
    }

    normals[N] = cross_product(p2, p1);
    norm = sqrt(normals[N][0] * normals[N][0] + normals[N][1] * normals[N][1] + normals[N][2] * normals[N][2]);
    for(int j = 0; j < 3; j++) {
        normals[N][j] /= norm;
    }

    return normals;
}

