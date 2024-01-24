#ifndef PANEL_H
#define PANEL_H

#include <QWidget>
#include <QDoubleSpinBox>

class Panel : public QWidget
{
    Q_OBJECT
public:
    explicit Panel(QWidget *parent = nullptr);

    double a_value();

private:
    QDoubleSpinBox* box_a;

signals:
    void box_a_changed(double);

};

#endif // PANEL_H
