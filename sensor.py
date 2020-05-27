import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
run = True

a = open('sensorlog.csv', 'w')
a.write('Time, Temperature, Humidity\n')

while run:
    try:
        humid, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humid is not None and temp is not None:
            print('Temp = ' + str(temp) + ' Humid = ' + str(humid))
            a.write('{0}, {1:0.1f}*C, {2:0.1f}%\r'.format(time.strftime('%m/%d/%y %H:%M:%S'),temp,humid))
            time.sleep(1)
        else:
            print("Fail to retrieve data from the sensor")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped")
        run = False
        a.close()