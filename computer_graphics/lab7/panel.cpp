#include "panel.h"

#include <QLabel>
#include <QSlider>
#include <QVBoxLayout>

Panel::Panel(QWidget *parent)
    : QWidget{parent}
{

    QLabel* label_accuracy = new QLabel("accuracy: ", this);

    box_accuracy = new QSpinBox(this);
    box_accuracy->setRange(1, 1000);
    box_accuracy->setSingleStep(1);
    box_accuracy->setValue(10);

    QVBoxLayout* panel_layout(new QVBoxLayout);
    panel_layout->addWidget(label_accuracy);
    panel_layout->addWidget(box_accuracy);
    panel_layout->addStretch();

    setLayout(panel_layout);

    connect(box_accuracy, SIGNAL(valueChanged(int)), this, SIGNAL(box_accuracy_changed(int)));

}

double Panel::accuracy() {

    return box_accuracy->value();
}
