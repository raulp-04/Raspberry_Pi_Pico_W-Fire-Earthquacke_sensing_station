import socket
import network
from machine import Pin
from time import sleep
from webpage import generate_html
import dht

active_buzzer = Pin(10, Pin.OUT)
vibration_sensor = Pin(11, Pin.IN)
atmospheric_sensor = dht.DHT11(Pin(12))
red_led = Pin(16, Pin.OUT)
green_led = Pin(17, Pin.OUT)
blue_led = Pin(18, Pin.OUT)


# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Tenda_84B8E8", "Alex2024")

while not wlan.isconnected():
    sleep(1)

print("Connected, IP address:", wlan.ifconfig()[0])

# Setup server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)


red_led.value(0)
green_led.value(0)
blue_led.value(0)
while True:
    green_led.value(1)
    atmospheric_sensor.measure()
    temperature = atmospheric_sensor.temperature()
    humidity = atmospheric_sensor.humidity()
    response = generate_html(temperature, humidity, vibration_sensor.value())
    
    print("Temperature : {}C".format(temperature))
    print("Humidity : {}%".format(humidity))
    
    if (temperature > 40 or humidity > 80) or vibration_sensor.value():
        active_buzzer.value(1)
        green_led.value(0)
        if temperature > 40 or humidity > 80:
            red_led.value(1)
        if vibration_sensor.value():
            blue_led.value(1)
        sleep(1)
        active_buzzer.value(0)
        red_led.value(0)
        blue_led.value(0)
        green_led.value(1)

    cl, addr = s.accept()
    print('Client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    
    request = cl_file.readline().decode('utf-8')
    if "buzzer=on" in request:
        active_buzzer.value(1)
        sleep(1)
        active_buzzer.value(0)
        cl.send(b"HTTP/1.1 302 Found\r\n")
        cl.send(b"Location: /\r\n")
        cl.send(b"Connection: close\r\n")
        cl.send(b"\r\n")
        cl.close()
        continue
        
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break

    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()

    sleep(1)