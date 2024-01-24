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
    slider_turn_OY->setTickInterval(3);
    slider_turn_OY->setValue(45);

    QLabel* label_turn_OX = new QLabel("turn around OX: ", this);

    slider_turn_OX = new QSlider(Qt::Horizontal, this);
    slider_turn_OX->setRange(0, 360);
    slider_turn_OX->setTickInterval(3);
    slider_turn_OX->setValue(35);

    QLabel* label_turn_OZ = new QLabel("turn around OZ: ", this);

    slider_turn_OZ = new QSlider(Qt::Horizontal, this);
    slider_turn_OZ->setRange(0, 360);
    slider_turn_OZ->setTickInterval(3);
    slider_turn_OZ->setValue(0);

    QLabel* label_distance = new QLabel("distance from pov: ", this);

    box_distance = new QSpinBox(this);
    box_distance->setRange(500, 1000);
    box_distance->setSingleStep(50);
    box_distance->setValue(500);

    QLabel* label_parallels = new QLabel("amount of parallels: ", this);

    box_parallels = new QSpinBox(this);
    box_parallels->setRange(1, 25);
    box_parallels->setSingleStep(1);
    box_parallels->setValue(4);

    QLabel* label_meridians = new QLabel("amount of meridians: ", this);

    box_meridians = new QSpinBox(this);
    box_meridians->setRange(1, 100);
    box_meridians->setSingleStep(1);
    box_meridians->setValue(12);

    box_frame = new QCheckBox("frame", this);
    box_frame->setChecked(true);

    box_illuminated_figure = new QCheckBox("illuminated figure", this);
    box_illuminated_figure->setChecked(false);

    QVBoxLayout* panel_layout(new QVBoxLayout);
    panel_layout->addWidget(label_turn_OY);
    panel_layout->addWidget(slider_turn_OY);
    panel_layout->addWidget(label_turn_OX);
    panel_layout->addWidget(slider_turn_OX);
    panel_layout->addWidget(label_turn_OZ);
    panel_layout->addWidget(slider_turn_OZ);
    panel_layout->addWidget(label_distance);
    panel_layout->addWidget(box_distance);
    panel_layout->addWidget(label_parallels);
    panel_layout->addWidget(box_parallels);
    panel_layout->addWidget(label_meridians);
    panel_layout->addWidget(box_meridians);
    panel_layout->addWidget(box_frame);
    panel_layout->addWidget(box_illuminated_figure);
    panel_layout->addStretch();

    setLayout(panel_layout);

    connect(slider_turn_OY, SIGNAL(valueChanged(int)), this, SIGNAL(slider_turn_OY_changed(int)));
    connect(slider_turn_OX, SIGNAL(valueChanged(int)), this, SIGNAL(slider_turn_OX_changed(int)));
    connect(slider_turn_OZ, SIGNAL(valueChanged(int)), this, SIGNAL(slider_turn_OZ_changed(int)));
    connect(box_distance, SIGNAL(valueChanged(int)), this, SIGNAL(box_distance_changed(int)));
    connect(box_parallels, SIGNAL(valueChanged(int)), this, SIGNAL(box_parallels_changed(int)));
    connect(box_meridians, SIGNAL(valueChanged(int)), this, SIGNAL(box_meridians_changed(int)));
    connect(box_frame, SIGNAL(stateChanged(int)), this, SIGNAL(box_frame_changed(int)));
    connect(box_illuminated_figure, SIGNAL(stateChanged(int)), this, SIGNAL(box_illuminated_figure_changed(int)));

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

double Panel::parallels() {

    return box_parallels->value();
}

double Panel::meridians() {

    return box_meridians->value();
}

int Panel::frame_state() {

    return box_frame->isChecked();
}

int Panel::illustrated_figure_state() {

    return box_illuminated_figure->isChecked();
}
