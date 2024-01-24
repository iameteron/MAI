#ifndef WIDGET_H
#define WIDGET_H

#include "view.h"

#include <iostream>

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    View* view;

private slots:
    void redrawOnValueChange(int);


};

#endif // WIDGET_H
