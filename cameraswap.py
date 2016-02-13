#! /usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

subprocess.Popen("/home/pi/vision/start_mjpg.sh")

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(4, GPIO.BOTH)

def set_camera():
 if GPIO.input(4):
  print 'forward camera activated'
  subprocess.Popen("/home/pi/set_cam_fwd.sh")
 else:
  print 'backward camera activated'
  subprocess.Popen("/home/pi/set_cam_bck.sh")

GPIO.add_event_callback(4, set_camera)
