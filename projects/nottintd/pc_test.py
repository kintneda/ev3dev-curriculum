import robot_controller as robo
import mqtt_remote_method_calls as com


mqtt_client = com.MqttClient()
mqtt_client.connect_to_ev3()

mqtt_client.send_message("make_burger")