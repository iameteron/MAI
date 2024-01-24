#include "panel.h"

#include <QLabel>
#include <QSlider>
#include <QVBoxLayout>

Panel::Panel(QWidget *parent)
    : QWidget{parent}
{
    QLabel* label_turn_OY = new QLabel("turn around OY: ", this);

    slider_turn_OY = new QSlider(Qt::Horizontal, this);
    slider_turn_OY->setRange(0, 360);
    slider_turn_OY->setTickInterval(5);
    slider_turn_OY->setValue(45);

    QLabel* label_turn_OX = new QLabel("turn around OX: ", this);

    slider_turn_OX = new QSlider(Qt::Horizontal, this);
    slider_turn_OX->setRange(0, 360);
    slider_turn_OX->setTickInterval(5);
    slider_turn_OX->setValue(35);

    QLabel* label_turn_OZ = new QLabel("turn around OZ: ", this);

    slider_turn_OZ = new QSlider(Qt::Horizontal, this);
    slider_turn_OZ->setRange(0, 360);
    slider_turn_OZ->setTickInterval(5);
    slider_turn_OZ->setValue(0);

    QLabel* label_distance = new QLabel("distance from pov: ", this);

    box_distance = new QSpinBox(this);
    box_distance->setRange(200, 1000);
    box_distance->setSingleStep(50);
    box_distance->setValue(500);

    QVBoxLayout* panel_layout(new QVBoxLayout);
    panel_layout->addWidget(label_turn_OY);
    panel_layout->addWidget(slider_turn_OY);
    panel_layout->addWidget(label_turn_OX);
    panel_layout->addWidget(slider_turn_OX);
    panel_layout->addWidget(label_turn_OZ);
    panel_layout->addWidget(slider_turn_OZ);
    panel_layout->addWidget(label_distance);
    panel_layout->addWidget(box_distance);
    panel_layout->addStretch();

    setLayout(panel_layout);

    connect(slider_turn_OY, SIGNAL(valueChanged(int)), this, SIGNAL(slider_turn_OY_changed(int)));
    connect(slider_turn_OX, SIGNAL(valueChanged(int)), this, SIGNAL(slider_turn_OX_changed(int)));
    connect(slider_turn_OZ, SIGNAL(valueChanged(int)), this, SIGNAL(slider_turn_OZ_changed(int)));
    connect(box_distance, SIGNAL(valueChanged(int)), this, SIGNAL(box_distance_changed(int)));

}

double Panel::angle_turn_OY() {

    return slider_turn_OY->value();
}

double Panel::angle_turn_OX() {

    return slider_turn_OX->value();
}

double Panel::angle_turn_OZ() {

    return slider_turn_OZ->value();
}

double Panel::distance() {

    return box_distance->value();
}
