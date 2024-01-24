#ifndef PANEL_H
#define PANEL_H

#include <QWidget>
#include <QSlider>
#include <QSpinBox>

class Panel : public QWidget
{
    Q_OBJECT
public:
    explicit Panel(QWidget *parent = nullptr);

    double accuracy();

private:
    QSpinBox* box_accuracy;

signals:
    void box_accuracy_changed(int);

};

#endif // PANEL_H
