#include "widget.h"

#include "view.h"
#include <QHBoxLayout>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    Panel* panel(new Panel);

    view = new View;
    view->setControlPanel(panel);

    QHBoxLayout* widget_layout(new QHBoxLayout);
    widget_layout->addWidget(view, 4);
    widget_layout->addWidget(panel, 1);

    setLayout(widget_layout);

    this->resize(750, 600);

    connect(panel, SIGNAL(box_accuracy_changed(int)), this, SLOT(redrawOnValueChange(int)));

}

Widget::~Widget()
{
}

void Widget::redrawOnValueChange(int)
{
    view->update();
}

