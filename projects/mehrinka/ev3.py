import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3
import time
import robot_controller as robo


class MyDelegate(object):

    def __init__(self):
        self.running = True
        self.robot = robo.Snatch3r()

    def drive_forward(self, left_speed, right_speed):
        ev3.Sound.speak('drive forward')
        self.robot.drive_forward(left_speed, right_speed)

    def turn_left(self, left_speed, right_speed):
        self.robot.turn_left(left_speed, right_speed)

    def stop(self):
        self.robot.stop()

    def turn_right(self, left_speed, right_speed):
        self.robot.turn_right(left_speed, right_speed)

    def drive_backward(self, left_speed, right_speed):
        self.robot.drive_backward(left_speed, right_speed)

    def arm_up(self):
        self.robot.arm_up()

    def arm_down(self):
        self.robot.arm_down()

    def shutdown(self):
        self.robot.shutdown()

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.1)


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self):
        self.running = True


def main():
    ev3.Sound.speak("Personal Project").wait()
    robot = robo.Snatch3r()
    dc = DataContainer()

    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_pc()

    btn = ev3.Button()

    btn.on_up = lambda state: colors(state, mqtt_client, robot)

    while dc.running:
        btn.process()
        time.sleep(0.01)


def colors(button_state, mqtt_client,  bot):
    ev3.Sound.speak("colors")
    if button_state:
        color = bot.color_sensor.color
        mqtt_client.send_message("on_color_received", [color])


main()