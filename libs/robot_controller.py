"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    """Creates instance variables and defines methods for the robot."""
    def __init__(self):
        """Establishes instance variables for the robot."""
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)

        assert self.left_motor.connected
        assert self.right_motor.connected

    def drive_inches(self, inches_target, speed_deg_per_second):
        """Method that takes in desired inches traveled and speed to move robot to desired position."""
        speed = speed_deg_per_second
        distance = inches_target
        position = (distance / 4) * 360
        self.left_motor.run_to_rel_pos(position_sp=position, speed_sp=speed)
        self.right_motor.run_to_rel_pos(position_sp=position, speed_sp=speed)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        """Method that takes in degrees and speed and turns the robot a desired amount."""
        speed = turn_speed_sp
        degrees = degrees_to_turn * 4

        if degrees > 0:
            self.left_motor.run_to_rel_pos(speed_sp=speed, position_sp=degrees)
            self.right_motor.run_to_rel_pos(speed_sp=speed, position_sp=-degrees)
            self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

        if degrees < 0:
            self.left_motor.run_to_rel_pos(speed_sp=speed, position_sp=degrees)
            self.right_motor.run_to_rel_pos(speed_sp=speed, position_sp=-degrees)
            self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
            self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)