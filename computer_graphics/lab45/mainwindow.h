#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSlider>
#include <QSpinBox>
#include <QCheckBox>
#include <QPushButton>

#include "window.h"

class MainWindow : public QMainWindow
{
    Q_OBJECT
public:
    explicit MainWindow(QWidget *parent = nullptr);
    double get_parallels();
    double get_meridians();
    double get_timer_status();

private:
    QPushButton* draw_button;
    QSpinBox* box_parallels;
    QSpinBox* box_meridians;
    QCheckBox* box_timer;
    int parallels;
    int meridians;
    int timer_status;

    Window* w;

private slots:
    void change_parallels(int);
    void change_meridians(int);
    void change_timer_status(int);
    void draw();

};

#endif // MAINWINDOW_H
