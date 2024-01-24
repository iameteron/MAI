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

    double angle_turn_OY();
    double angle_turn_OX();
    double angle_turn_OZ();
    double distance();

private:
    QSlider* slider_turn_OY;
    QSlider* slider_turn_OX;
    QSlider* slider_turn_OZ;
    QSpinBox* box_distance;

signals:
    void slider_turn_OY_changed(int);
    void slider_turn_OX_changed(int);
    void slider_turn_OZ_changed(int);
    void box_distance_changed(int);

};

#endif // PANEL_H
