#include "window.h"

#include "iostream"

Window::Window(int meridians, int parallels, int timer_status)
    : QOpenGLWindow(), m_texture(0), m_indexBuffer(QOpenGLBuffer::IndexBuffer)
{
    setGeometry(400, 200, 800, 600);

    n = meridians;
    m = parallels;

    rotOY = 0;
    connect(&tmr, SIGNAL(timeout()), this, SLOT(rotate_OY()));

    if(timer_status == 1) {
        tmr.start(100);
    }
}

Window::~Window()
{
}

void Window::initializeGL() {

    glClearColor(0.0, 0.0f, 0.0f, 0.0f);
    glEnable(GL_DEPTH_TEST);

    initShaders();
    initHemisphere(n, m);
}

void Window::resizeGL(int w, int h) {

    double aspect = w / (float)h;

    m_projectionMatrix.setToIdentity();
    m_projectionMatrix.perspective(45, aspect, 0.1f, 10.0f);
}

void Window::paintGL() {

     glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
     glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);

     QMatrix4x4 viewMatrix;
     viewMatrix.setToIdentity();
     viewMatrix.translate(0.0, 0.0, -5.0);

     viewMatrix.rotate(m_rotation);
     viewMatrix.rotate(rotOY, 0, 1, 0);

     QMatrix4x4 modelMatrix;
     modelMatrix.setToIdentity();

     m_texture->bind(0);

     m_arrayBuffer.bind();
     m_indexBuffer.bind();

     m_program.bind();
     m_program.setUniformValue("u_projectionMatrix", m_projectionMatrix);
     m_program.setUniformValue("u_viewMatrix", viewMatrix);
     m_program.setUniformValue("u_modelMatrix", modelMatrix);
     m_program.setUniformValue("u_texture", 0);
     m_program.setUniformValue("u_lightPosition", QVector4D(0, 0, 0, 1));
     m_program.setUniformValue("u_lightPower", 5.0f);

     int offset = 0;

     int vertLoc = m_program.attributeLocation("a_position");
     m_program.enableAttributeArray(vertLoc);
     m_program.setAttributeBuffer(vertLoc, GL_FLOAT, offset, 3, sizeof(VertexData));

     offset += sizeof(QVector3D);

     int texLoc = m_program.attributeLocation("a_texcoord");
     m_program.enableAttributeArray(texLoc);
     m_program.setAttributeBuffer(texLoc, GL_FLOAT, offset, 2, sizeof(VertexData));

     offset += sizeof(QVector2D);

     int normLoc = m_program.attributeLocation("a_normal");
     m_program.enableAttributeArray(normLoc);
     m_program.setAttributeBuffer(normLoc, GL_FLOAT, offset, 3, sizeof(VertexData));

     glDrawArrays(GL_QUADS, 0, m_indexBuffer.size());
}

void Window::mousePressEvent(QMouseEvent* mo) {

    if(mo->buttons() == Qt::LeftButton) {
        mPos = mo->pos();
    }
    mo->accept();
}

void Window::mouseMoveEvent(QMouseEvent* mo) {

    if(mo->buttons() != Qt::LeftButton) {
        return;
    }

    QVector2D diff = QVector2D(mo->localPos() - mPos);
    mPos = mo->pos();
    double angle = diff.length() / 2.0;
    QVector3D axis = QVector3D(diff.y(), diff.x(), 0);
    m_rotation = QQuaternion::fromAxisAndAngle(axis, angle) * m_rotation;

    update();
}

void Window::initShaders() {

    if(!m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, ":/vshader.vsh")) {
        close();
    }
    if(!m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, ":/fshader.fsh")) {
        close();
    }
    if(!m_program.link()) {
        close();
    }

}

void Window::initHemisphere(int n, int m)
{

    Hemisphere hemisphere(n, m);

    QVector<VertexData> vertices = hemisphere.get_vertices();

    QVector<GLuint> indices = hemisphere.get_indices();

    m_arrayBuffer.create();
    m_arrayBuffer.bind();
    m_arrayBuffer.allocate(vertices.constData(), vertices.size() * sizeof(VertexData));
    m_arrayBuffer.release();

    m_indexBuffer.create();
    m_indexBuffer.bind();
    m_indexBuffer.allocate(indices.constData(), indices.size() * sizeof(GLuint));
    m_arrayBuffer.release();

    m_texture = new QOpenGLTexture(QImage(":/concrete").mirrored());

    m_texture->setMinificationFilter(QOpenGLTexture::Nearest);
    m_texture->setMagnificationFilter(QOpenGLTexture::Linear);
    m_texture->setWrapMode(QOpenGLTexture::Repeat);

}

void Window::rotate_OY()
{
    rotOY += 4;
    update();
}

