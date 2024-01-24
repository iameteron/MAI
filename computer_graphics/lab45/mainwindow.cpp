#include "mainwindow.h"

#include <QLabel>
#include <QSlider>
#include <QVBoxLayout>

#include "iostream"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow{parent}
{
    this->resize(300, 400);

    QLabel* label_parallels = new QLabel("amount of parallels: ", this);
    label_parallels->move(20, 50);

    box_parallels = new QSpinBox(this);
    box_parallels->move(140, 50);
    box_parallels->setRange(1, 25);
    box_parallels->setSingleStep(1);
    box_parallels->setValue(4);

    parallels = 4;

    QLabel* label_meridians = new QLabel("amount of meridians: ", this);
    label_meridians->move(20, 100);

    box_meridians = new QSpinBox(this);
    box_meridians->move(140, 100);
    box_meridians->setRange(1, 100);
    box_meridians->setSingleStep(1);
    box_meridians->setValue(12);

    meridians = 12;

    QLabel* label_timer = new QLabel("rotate OY: ", this);
    label_timer->move(20, 150);

    box_timer = new QCheckBox(this);
    box_timer->setChecked(false);
    box_timer->move(140, 150);

    draw_button = new QPushButton(this);
    draw_button->move(100, 350);
    draw_button->setText("Draw");

    connect(box_parallels, SIGNAL(valueChanged(int)), this, SLOT(change_parallels(int)));
    connect(box_meridians, SIGNAL(valueChanged(int)), this, SLOT(change_meridians(int)));
    connect(box_timer, SIGNAL(stateChanged(int)), this, SLOT(change_timer_status(int)));
    connect(draw_button, SIGNAL(clicked()), this, SLOT(draw()));

}


double MainWindow::get_parallels() {

    return box_parallels->value();
}

double MainWindow::get_meridians() {

    return box_meridians->value();
}

double MainWindow::get_timer_status() {

    return box_timer->isChecked();
}

void MainWindow::change_parallels(int)
{
    parallels = get_parallels();
}

void MainWindow::change_meridians(int)
{
    meridians = get_meridians();
}

void MainWindow::change_timer_status(int)
{
    timer_status = get_timer_status();
}

void MainWindow::draw()
{
    w = new Window(meridians, parallels, timer_status);
    w->show();
}
