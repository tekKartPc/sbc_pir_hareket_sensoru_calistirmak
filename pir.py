# -*- coding: utf-8 -*- 
# tekKartPc.com
# twitter.com/tekKartPc
# facebook.com/tekKartPc
# -------------
# pir hareket alıglama sensörünü
# çalıştırma için önce
# gerekli bağlantıyı yapınız.
# detaylı bilgi için http://tekkartpc.com/hareket-algilama-sensoru-pir-hc-sr501-calistirma/ adresini ziyaret edip sorularınızı sorabilirsiniz.

import RPi.GPIO as GPIO
import time
import datetime

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "Hareket Algilandi!" if current_state else "beklemede"
        print("durum:   %s  -> %s " % (new_state,datetime.datetime.now()))
