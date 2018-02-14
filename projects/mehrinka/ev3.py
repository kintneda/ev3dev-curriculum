import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3
import robot_controller as robo

robot = robo.Snatch3r()


class MyDelegate(object):

    def __init__(self):
        self.running = True

    def drive_forward(self, left_speed, right_speed):
        robot.drive_forward(left_speed, right_speed)

    def turn_left(self, left_speed, right_speed):
        robot.turn_left(left_speed, right_speed)

    def stop(self):
        robot.stop()

    def turn_right(self, left_speed, right_speed):
        robot.turn_right(left_speed, right_speed)

    def drive_backward(self, left_speed, right_speed):
        robot.drive_backward(left_speed, right_speed)

    def arm_up(self):
        robot.arm_up()

    def arm_down(self):
        robot.arm_down()

    def shutdown(self):
        robot.shutdown()


def main():
    ev3.Sound.speak("Personal Project").wait()

    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_pc()

    btn = ev3.Button()
    btn.on_up = lambda state: colors(state, mqtt_client, robot)


def colors(button_state, mqtt_client,  bot):
    if button_state:
        color = bot.color_sensor.color
        mqtt_client.send_message("on_color_received", [color])