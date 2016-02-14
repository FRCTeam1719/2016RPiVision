# 2016RPiVision
We run our vision code on a Raspberry Pi 2, which is an ARM v7 processor with a 40-pin GPIO header, an ethernet port, and four USB ports.

We use [mjpg_streamer](https://sourceforge.net/projects/mjpg-streamer/) to stream from one of two LifeCam-3000 USB cameras, each ringed with green LEDs.
We use [GRIP](https://github.com/WPIRoboticsProjects/GRIP) to autonomously process the images from these cameras and output the contours of retroreflective tape to the networktables.
