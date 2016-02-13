#!/bin/sh
killall mjpg_streamer
export LD_LIBRARY_PATH=/home/pi/vision/mjpg-streamer/mjpg-streamer-experimental/
mjpg_streamer -o "output_http.so -w ./www -p 1180" -i "input_uvc.so -d /dev/video0 -f 15 -r 640x480 -y -n"
