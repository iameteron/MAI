#ifndef WINDOW_H
#define WINDOW_H

#include <QOpenGLWindow>
#include <QMouseEvent>
#include <QOpenGLShaderProgram>
#include <QOpenGLTexture>
#include <QOpenGLBuffer>
#include <QTimer>

#include <hemisphere.h>

class Window : public QOpenGLWindow
{
    Q_OBJECT

public:
    Window(int meridians, int parallels, int timer_status);
    ~Window();

protected:
    virtual void initializeGL();
    virtual void resizeGL(int w, int h);
    virtual void paintGL();

    virtual void mousePressEvent(QMouseEvent*);
    virtual void mouseMoveEvent(QMouseEvent*);

    void initShaders();
    void initHemisphere(int n, int m);

    QPoint mPos;

private:
    void drawCube(double a);

    QMatrix4x4 m_projectionMatrix;
    QOpenGLShaderProgram m_program;
    QOpenGLTexture* m_texture;
    QOpenGLBuffer m_arrayBuffer;
    QOpenGLBuffer m_indexBuffer;
    QQuaternion m_rotation;

    double rotOY;
    QTimer tmr;

    int n;
    int m;

public slots:
    void rotate_OY();

};
#endif // WINDOW_H
