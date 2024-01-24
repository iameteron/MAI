#ifndef PANEL_H
#define PANEL_H

#include <QWidget>
#include <QSlider>
#include <QSpinBox>
#include <QCheckBox>

class Panel : public QWidget
{
    Q_OBJECT
public:
    explicit Panel(QWidget *parent = nullptr);

    double angle_turn_OY();
    double angle_turn_OX();
    double angle_turn_OZ();
    double distance();
    double parallels();
    double meridians();
    int frame_state();
    int illustrated_figure_state();

private:
    QSlider* slider_turn_OY;
    QSlider* slider_turn_OX;
    QSlider* slider_turn_OZ;
    QSpinBox* box_distance;
    QSpinBox* box_parallels;
    QSpinBox* box_meridians;
    QCheckBox* box_frame;
    QCheckBox* box_illuminated_figure;

signals:
    void slider_turn_OY_changed(int);
    void slider_turn_OX_changed(int);
    void slider_turn_OZ_changed(int);
    void box_distance_changed(int);
    void box_parallels_changed(int);
    void box_meridians_changed(int);
    void box_frame_changed(int);
    void box_illuminated_figure_changed(int);

};

#endif // PANEL_H
