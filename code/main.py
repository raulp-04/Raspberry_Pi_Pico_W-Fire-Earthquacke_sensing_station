from machine import Pin
from time import sleep
import dht

active_buzzer = Pin(10, Pin.OUT)
vibration_sensor = Pin(11, Pin.IN)
atmospheric_sensor = dht.DHT11(Pin(12))

while True:
    atmospheric_sensor.measure()
    temperature = atmospheric_sensor.temperature()
    humidity = atmospheric_sensor.humidity()
    
    print("Temperature : {}C".format(str(temperature)))
    print("Humidity : {}%".format(str(humidity)))
    
    if temperature > 40:
        active_buzzer.value(1)
        sleep(0.5)
        active_buzzer.value(0)
    if vibration_sensor.value():
        active_buzzer.value(1)
        sleep(0.5)
        active_buzzer.value(0)
    sleep(1)
