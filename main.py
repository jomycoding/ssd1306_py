from machine import Pin
from machine import I2C

import ssd1306
from time import sleep


#i2c = I2C(-1, scl=Pin(22), sda=Pin(21)) #For ESP32: pin initializing
#i2c = I2C(-1, scl=Pin(5), sda=Pin(4))  #For ESP8266: pin initializing
i2c = I2C( sda=Pin(4), scl=Pin(5))  

print(i2c)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Welcome to Lab1!', 0, 0)
oled.text('Welcome to Lab!', 0, 16)
oled.text('Welcome to Lab!', 0, 32)
        
oled.show()
