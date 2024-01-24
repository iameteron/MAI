#include "panel.h"

#include <QLabel>

Panel::Panel(QWidget *parent)
    : QWidget(parent)
{
    QLabel *label_a = new QLabel("a: ", this);
    label_a->move(10, 10);

    box_a = new QDoubleSpinBox(this);
    box_a->move(40, 10);
    box_a->setRange(50, 200);
    box_a->setSingleStep(5);
    box_a->setValue(100);

    connect(box_a, SIGNAL(valueChanged(double)), this, SIGNAL(box_a_changed(double)));

}

double Panel::a_value() {

    return box_a->value();
}
