#ifndef HEMISPHERE_H
#define HEMISPHERE_H

#include "window.h"

struct VertexData {

    VertexData() {

    }
    VertexData(QVector3D p, QVector2D t, QVector3D n) :
        position(p), texCoord(t), normal(n)
    {

    }
    QVector3D position;
    QVector2D texCoord;
    QVector3D normal;

};

class Hemisphere
{
public:
    Hemisphere(int n, int m);
    double** get_points(double a, double b, int n);
    double** get_normals(double** points, int n, int m);

    QVector<VertexData> get_vertices();
    QVector<GLuint> get_indices();

private:
    double** points;
    double** normals;

    QVector<VertexData> vertices;
    QVector<GLuint> indices;

};

#endif // HEMISPHERE_H
