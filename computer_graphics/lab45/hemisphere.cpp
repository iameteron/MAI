#include "hemisphere.h"
#include "cmath"
#include "iostream"

const double pi = 3.14;

QVector3D cross_product(QVector3D x, QVector3D y);

Hemisphere::Hemisphere(int n, int  m) {

    QVector<double> phi;
    for(int i = 0; i < n; i++) {
        phi.append((2 * pi) * i / n);
    }

    QVector<double> theta;
    for(int i = 0; i < m; i++) {
        theta.append((pi / 2) * i / m);
    }

    // positions

    QVector<QVector3D> points;

    double r = 1.5;
    for(int i = 0; i < n * m; i++) {

        double phi_curr = phi[i % n];
        double theta_curr = theta[i / n];

        QVector3D point_curr(r * cos(theta_curr) * cos(phi_curr),
                             r * cos(theta_curr) * sin(phi_curr),
                             r * sin(theta_curr) - r / 2);

        points.append(point_curr);
    }

    QVector3D top_point(0, 0, r / 2);
    QVector3D bottom_point(0, 0, - r / 2);

    points.append(top_point);
    points.append(bottom_point);

    // normals

    QVector<QVector3D> normals;

    for(int i = 0; i < n * (m - 1); i++)  {

        QVector3D p1(points[i + 1][0] - points[i][0],
                     points[i + 1][1] - points[i][1],
                     points[i + 1][2] - points[i][2]);

        QVector3D p2(points[i + n][0] - points[i][0],
                     points[i + n][1] - points[i][1],
                     points[i + n][2] - points[i][2]);

        QVector3D curr_normal = cross_product(p1, p2);
        curr_normal = curr_normal.normalized();

        normals.append(curr_normal);

    }

    for(int i = n * (m - 1); i < n * m; i++) {

        int j = i;
        if(i == n * m - 1) {
            j = i - n;
        }

        QVector3D p1(points[j + 1][0] - points[i][0],
                     points[j + 1][1] - points[i][1],
                     points[j + 1][2] - points[i][2]);

        QVector3D p2(top_point[0] - points[i][0],
                     top_point[1] - points[i][1],
                     top_point[2] - points[i][2]);

        QVector3D curr_normal = cross_product(p1, p2);
        curr_normal = curr_normal.normalized();

        normals.append(curr_normal);

    }

    QVector3D top_normal 	= QVector3D(0, 0, +1);
    QVector3D bottom_normal = QVector3D(0, 0, -1);

    normals.append(top_normal);
    normals.append(bottom_normal);

    // vertices in a needed format

    // main hool

    for(int i = 0; i < n * (m - 1); i++) {

        VertexData curr_vertex;

        int j = i;
        if((i + 1) % n == 0) {
            j = i - n;
        }

        QVector3D curr_point(points[i][0], points[i][1], points[i][2]);
        QVector3D curr_normal(normals[i][0], normals[i][1], normals[i][2]);
        QVector2D curr_texcoord(0.0, 0.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(points[j + 1][0], points[j + 1][1], points[j + 1][2]);
        curr_normal = QVector3D(normals[j + 1][0], normals[j + 1][1], normals[j + 1][2]);
        curr_texcoord = QVector2D(1.0, 0.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(points[j + n + 1][0], points[j + n + 1][1], points[j + n + 1][2]);
        curr_normal = QVector3D(normals[j + n + 1][0], normals[j + n + 1][1], normals[j + n + 1][2]);
        curr_texcoord = QVector2D(1.0, 1.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(points[i + n][0], points[i + n][1], points[i + n][2]);
        curr_normal = QVector3D(normals[i + n][0], normals[i + n][1], normals[i + n][2]);
        curr_texcoord = QVector2D(0.0, 1.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);


    }

    // upper part

    for(int i =  n * (m - 1); i < n * m; i++) {

        VertexData curr_vertex;

        int j = i;
        if((i + 1) % n == 0 && i != n * (m - 1)) {
            j = i - n;
        }

        QVector3D curr_point(points[i][0], points[i][1], points[i][2]);
        QVector3D curr_normal(normals[i][0], normals[i][1], normals[i][2]);
        QVector2D curr_texcoord(0.0, 0.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(points[j + 1][0], points[j + 1][1], points[j + 1][2]);
        curr_normal = QVector3D(normals[j + 1][0], normals[j + 1][1], normals[j + 1][2]);
        curr_texcoord = QVector2D(1.0, 0.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(top_point[0], top_point[1], top_point[2]);
        curr_normal = QVector3D(top_normal[0], top_normal[1], top_normal[2]);
        curr_texcoord = QVector2D(0.5, 1.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(top_point[0], top_point[1], top_point[2]);
        curr_normal = QVector3D(top_normal[0], top_normal[1], top_normal[2]);
        curr_texcoord = QVector2D(0.5, 1.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

    }

    // lower part

    for(int i = 0; i < n; i++) {

        VertexData curr_vertex;

        int j = i;
        if((i + 1) % n == 0) {
            j = i - n;
        }

        QVector3D curr_point(points[i][0], points[i][1], points[i][2]);
        QVector3D curr_normal(bottom_normal[0], bottom_normal[1], bottom_normal[2]);
        QVector2D curr_texcoord(0.0, 0.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(points[j + 1][0], points[j + 1][1], points[j + 1][2]);
        curr_normal = QVector3D(bottom_normal[0], bottom_normal[1], bottom_normal[2]);
        curr_texcoord = QVector2D(1.0, 0.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(bottom_point[0], bottom_point[1], bottom_point[2]);
        curr_normal = QVector3D(bottom_normal[0], bottom_normal[1], bottom_normal[2]);
        curr_texcoord = QVector2D(0.5, 1.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

        curr_point = QVector3D(bottom_point[0], bottom_point[1], bottom_point[2]);
        curr_normal = QVector3D(bottom_normal[0], bottom_normal[1], bottom_normal[2]);
        curr_texcoord = QVector2D(0.5, 1.0);
        curr_vertex = VertexData(curr_point, curr_texcoord, curr_normal);
        vertices.append(curr_vertex);

    }



    // indices

    for(int i = 0; i < 4 * n * m; i++) {

        indices.append(i);
    }


}

QVector<VertexData> Hemisphere::get_vertices() {

    return vertices;
}

QVector<GLuint> Hemisphere::get_indices() {

    return indices;
}

QVector3D cross_product(QVector3D x, QVector3D y) {

    QVector3D z;
    z[0] =   x[1] * y[2] - x[2] * y[1];
    z[1] = - x[0] * y[2] + x[2] * y[0];
    z[2] =   x[0] * y[1] - x[1] * y[0];
    return z;
}

