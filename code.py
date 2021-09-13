import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.5

while True:
    if cp.touch_A1:
        cp.pixels[6] = (255, 0, 0)
        cp.play_file("bird-0.wav")
        time.sleep(0.25)
        cp.pixels[6] = (0, 0, 0)
    if cp.touch_A2:
        cp.pixels[7] = (0, 255, 0)
        cp.play_file("bird-1.wav")
        time.sleep(0.25)
        cp.pixels[7] = (0, 0, 0)
    if cp.touch_A3:
        cp.pixels[8] = (0, 255, 0)
        cp.play_file("bird-2.wav")
        time.sleep(0.25)
        cp.pixels[8] = (0, 0, 0)
    if cp.touch_A4:
        cp.pixels[0] = (40, 15, 210)
        cp.play_file("bird-3.wav")
        time.sleep(0.25)
        cp.pixels[0] = (0, 0, 0)
    if cp.touch_A5:
        cp.pixels[1] = (255, 50, 55)
        cp.play_file("bird-4.wav")
        time.sleep(0.25)
        cp.pixels[1] = (0, 0, 0)
    if cp.touch_A6:
        cp.pixels[3] = (125, 0, 255)
        cp.play_file("bird-5.wav")
        time.sleep(0.25)
        cp.pixels[3] = (0, 0, 0)
    if cp.touch_A7:
        cp.pixels[4] = (0, 255, 55)
        cp.play_file("bird-6.wav")
        time.sleep(0.25)
        cp.pixels[4] = (0, 0, 0)
