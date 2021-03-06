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
import time
import math


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    """Creates instance variables and defines methods for the robot."""
    def __init__(self):
        """Establishes instance variables for the robot."""
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_D)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_A)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_C)
        self.touch_sensor = ev3.TouchSensor()
        self.color_sensor = ev3.ColorSensor()
        self.ir_sensor = ev3.InfraredSensor()
        self.pixy = ev3.Sensor(driver_name="pixy-lego")
        self.messenger = None

        assert self.arm_motor.connected
        assert self.touch_sensor
        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.color_sensor
        assert self.ir_sensor
        assert self.pixy

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

    def arm_down(self):
        """Moves the Snatch3r arm to the down position."""
        self.arm_motor.run_to_abs_pos(position_sp=0)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)  # Blocks until the motor finishes running
        ev3.Sound.beep()

    def arm_calibration(self):
        """Runs the arm up until the touch sensor is hit then back to the bottom again, beeping at both locations.
        Once back at in the bottom position, gripper open, set the absolute encoder position to 0.  You are calibrated!
        The Snatch3r arm needs to move 14.2 revolutions to travel from the touch sensor to the open position."""
        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)

        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep()

        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep()
        self.arm_motor.position = 0  # Calibrate the down position as 0 (this line is correct as is).

    def arm_up(self):
        """Moves the Snatch3r arm to the up position"""

        self.arm_motor.run_forever(speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep()

    def shutdown(self):
        """Stops everything and turns LEDs green."""
        self.left_motor.stop(stop_action="brake")
        self.right_motor.stop(stop_action="brake")
        self.arm_motor.stop(stop_action="brake")
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        print("Goodbye")
        ev3.Sound.speak("Goodbye")

    def loop_forever(self):
        # This is a convenience method that I don't really recommend for most programs other than m5.
        #   This method is only useful if the only input to the robot is coming via mqtt.
        #   MQTT messages will still call methods, but no other input or output happens.
        # This method is given here since the concept might be confusing.
        self.running = True
        while self.running:
            time.sleep(0.1)  # Do nothing (except receive MQTT messages) until an MQTT message calls shutdown.

    def drive_forward(self, left_speed_entry, right_speed_entry):
        """Drives the robot forward"""
        self.right_motor.run_forever(speed_sp=right_speed_entry)
        self.left_motor.run_forever(speed_sp=left_speed_entry)

    def turn_left(self, left_speed_entry, right_speed_entry):
        """Turns the robot left"""
        self.right_motor.run_forever(speed_sp=right_speed_entry)
        self.left_motor.run_forever(speed_sp=-left_speed_entry)

    def turn_right(self, left_speed_entry, right_speed_entry):
        """Turns the robot right"""
        self.right_motor.run_forever(speed_sp=-right_speed_entry)
        self.left_motor.run_forever(speed_sp=left_speed_entry)

    def drive_backward(self, left_speed_entry, right_speed_entry):
        """Drives the robot backwards"""
        self.right_motor.run_forever(speed_sp=-right_speed_entry)
        self.left_motor.run_forever(speed_sp=-left_speed_entry)

    def stop(self):
        """Stops the driving motors"""
        self.right_motor.run_forever(speed_sp=0)
        self.left_motor.run_forever(speed_sp=0)

    def seek_beacon(self):
        beacon_seeker = ev3.BeaconSeeker()  # Assumes remote is set to channel 1

        forward_speed = 300
        turn_speed = 100
        found = False

        while not self.touch_sensor.is_pressed:
            # The touch sensor can be used to abort the attempt (sometimes handy during testing)

            # Done: 3. Use the beacon_seeker object to get the current heading and distance.
            current_heading = beacon_seeker.heading  # use the beacon_seeker heading
            current_distance = beacon_seeker.distance  # use the beacon_seeker distance
            if current_distance == -128:
                # If the IR Remote is not found just sit idle for this program until it is moved.
                print("IR Remote not found. Distance is -128")
                self.stop()
            else:

                # Here is some code to help get you started
                if math.fabs(current_heading) < 2:
                    # Close enough of a heading to move forward
                    print("On the right heading. Distance: ", current_distance)
                    # You add more!
                    if current_distance > 0:
                        self.left_motor.run_forever(speed_sp=forward_speed)
                        self.right_motor.run_forever(speed_sp=forward_speed)
                    if current_distance <= 1:
                        self.left_motor.run_forever(speed_sp=forward_speed)
                        self.right_motor.run_forever(speed_sp=forward_speed)
                        time.sleep(1)
                        self.left_motor.stop()
                        self.right_motor.stop()
                        found = True
                        break
                if math.fabs(current_heading) > 2 < 10:
                    print("Ajusting Heading", current_heading)
                    if current_heading < 0:
                        self.left_motor.run_forever(speed_sp=turn_speed)
                        self.right_motor.run_forever(speed_sp=forward_speed)
                    if current_heading > 0:
                        self.left_motor.run_forever(speed_sp=forward_speed)
                        self.right_motor.run_forever(speed_sp=turn_speed)
                if math.fabs(current_heading) > 10:
                    self.left_motor.stop()
                    self.right_motor.stop()
                    print("Heading is too far off to fix")

            time.sleep(0.2)

        # The touch_sensor was pressed to abort the attempt if this code runs.
        print("Abandon ship!")
        self.stop()
        return found

    def make_burger(self):
        ev3.Sound.speak("Going to make your burger")
        time.sleep(1)
        self.right_motor.run_forever(speed_sp=-100)
        self.left_motor.run_forever(speed_sp=100)
        while True:
            self.pixy.mode = "SIG1"
            width = self.pixy.value(3)
            print(width)
            if width > 50:
                ev3.Sound.beep()
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=0)
                break
            time.sleep(.1)
        ev3.Sound.speak("Making your burger")
        time.sleep(3)
        ev3.Sound.speak("Your burger is ready")
        time.sleep(1)

        self.right_motor.run_forever(speed_sp=100)
        self.left_motor.run_forever(speed_sp=-100)
        while True:
            self.pixy.mode = "SIG4"
            width = self.pixy.value(3)
            print(width)
            if width > 50:
                ev3.Sound.beep()
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=0)
                break
            time.sleep(.1)
        ev3.Sound.speak("Here is your burger")
        time.sleep(1)
    #     I need pc code to wait until this code gets here.  Want person to have to push button to take burger and
    # set robot to get the fries.  Maybe flip burger while making it

    def get_fries(self):
        ev3.Sound.speak("Going to get your fries")
        time.sleep(1)
        self.right_motor.run_forever(speed_sp=-100)
        self.left_motor.run_forever(speed_sp=100)
        while True:
            self.pixy.mode = "SIG2"
            width = self.pixy.value(3)
            print(width)
            if width > 50:
                ev3.Sound.beep()
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=0)
                break
            time.sleep(.1)
        ev3.Sound.speak("Getting your fries")
        time.sleep(3)

        self.right_motor.run_forever(speed_sp=100)
        self.left_motor.run_forever(speed_sp=-100)
        while True:
            self.pixy.mode = "SIG4"
            width = self.pixy.value(3)
            print(width)
            if width > 50:
                ev3.Sound.beep()
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=0)
                break
            time.sleep(.1)
        ev3.Sound.speak("Here are your fries")
        time.sleep(1)

    def get_drink(self):
        ev3.Sound.speak("Going to get your drink")
        time.sleep(1)
        self.right_motor.run_forever(speed_sp=100)
        self.left_motor.run_forever(speed_sp=-100)
        while True:
            self.pixy.mode = "SIG3"
            width = self.pixy.value(3)
            print(width)
            if width > 50:
                ev3.Sound.beep()
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=0)
                break 
            time.sleep(.1)
        ev3.Sound.speak("Filling up your cup")
        time.sleep(3)

        self.right_motor.run_forever(speed_sp=-100)
        self.left_motor.run_forever(speed_sp=100)
        while True:
            self.pixy.mode = "SIG4"
            width = self.pixy.value(3)
            print(width)
            if width > 50:
                ev3.Sound.beep()
                self.right_motor.run_forever(speed_sp=0)
                self.left_motor.run_forever(speed_sp=0)
                break
            time.sleep(.1)
        ev3.Sound.speak("Here is your drink")
        time.sleep(1)

    def get_touch_sensor(self):
        self.messenger.send_message("take_order", [self.touch_sensor.is_pressed])

    def set_messenger(self, messenger):
        self.messenger = messenger

    def enjoy_meal(self):
        ev3.Sound.speak("Enjoy your meal")