# SMotor
Control a stepper motor using a raspberry PI. The main purpose of this
project was to develop an API to control a stepper motor on a Raspberry
Pi platform. The smotor command line tool provides an example of how this
API may be used.

## Install
Run the install script after cloning the repo

```
./install.sh
```

Once push to github the project could be installed using the following command.

```
sudo python3 -m pip install git+https://github.com/pjaos/rpi_stepper_motor.git
```

## Uninstall
Run the install script

```
./uninstall.sh
```
## Connections to Raspberry PI

The raspberry PI should be connected to a 4 wire bipolar stepper motor as detailed in the
schematic.

![alt text](images/schematic.png" "image Title")

## Using smotor
The following command line help is available.

```
smotor -h
usage: smotor.py [-h] [-d] [-a ANGLE] [-m MODE] [-s SPEED] [-o] [-f] [-r] [-z] [-p] [-n]

Example interface to drive a stepper motor.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable debugging.
  -a ANGLE, --angle ANGLE
                        Set the angle to move the motor spindle. Set a -ve angle to reverse the motor direction (anti clockwise). If the -r option is not used then the angle set is an absolute angle with reference to the
                        zero/reference position.
  -m MODE, --mode MODE  The mode of the stepper motor. 1 = Full Step, 2 = 1/2 step, 4 = 1/4 step, 8 = 1/8 step, 16 = 1/16 step, 32 = 1/32 step (default=2).
  -s SPEED, --speed SPEED
                        Set the speed of the motor in revolutions per second (default=1.0).
  -o, --on              Turn the motor current on. The motor will hold it's position and can be moved.
  -f, --off             Turn the motor current off. The motor will not draw power and can be manually moved.
  -r, --relative        Turn relative to the current position. By default the absolute position of the motor spindle is set.
  -z, --zero            Set the rzero/reference position of the motor to it's current position.
  -p, --stop            Stop the motor if it is running. If this option is used then the absolute position of the motor is lost.
  -n, --non_stop        Run the motor non stop. If this option is used then the absolute position of the motor is lost.
```


### Move relative to the current position
To move the motor spindle 90 degrees.

```
smotor -a 90 -r
INFO:  Set Mode to 1/2.
INFO:  Moving 90.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now 270.0°
```

### Set zero position
To set the current position as reference/zero position.

```
smotor -z
INFO:  Set Mode to 1/2.
INFO:  Set the current motor position to the zero/reference position.
```

### Absolute move
Move relative to the zero position

```
smotor -a 90 -r
INFO:  Set Mode to 1/2.
INFO:  Moving 90.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now 90.0°
pi@raspberrypi:~/pip/smotor $ smotor -a 90 -r
INFO:  Set Mode to 1/2.
INFO:  Moving 90.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now 180.0°
pi@raspberrypi:~/pip/smotor $ smotor -a 90 -r
INFO:  Set Mode to 1/2.
INFO:  Moving 90.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now 270.0°
pi@raspberrypi:~/pip/smotor $ smotor -z
INFO:  Set Mode to 1/2.
INFO:  Set the current motor position to the zero/reference position.
pi@raspberrypi:~/pip/smotor $ smotor -a 90
INFO:  Set Mode to 1/2.
INFO:  Moving 90.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now 90.0°
pi@raspberrypi:~/pip/smotor $ smotor -a 180
INFO:  Set Mode to 1/2.
INFO:  Moving 180.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now 180.0°
pi@raspberrypi:~/pip/smotor $ smotor -a 0
INFO:  Set Mode to 1/2.
INFO:  Moving 0.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now 0.0°
pi@raspberrypi:~/pip/smotor $ smotor -a -90
INFO:  Set Mode to 1/2.
INFO:  Moving -90.0° at 1.0 revs/sec.
INFO:  The absolute position of the motor is now -90.0°

```
