def on_button_pressed_a():
    servos.P0.set_angle(90)
input.on_button_pressed(Button.A, on_button_pressed_a)
