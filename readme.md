# Aquarium
A home automation project. 

The goal:

*'To take sensor readings from the aquarium using hardware & Raspberry Pi, store
those readings and make them available via an API to a frontend, for example an
Android or iOS app'.*

This project is based on Adafruit's excellent temperature sensor tutorial, over
at https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing?view=all. Go check it out; if you get that far, then the rest of this repository should
make a lot more sense ;-)

# Repo Structure

The repository is organised into several major layers or areas of concern. These
are:

- Hardware
- Backend
- Frontend

These are detailed below.

## The Hardware
This contains the low level stuff, circuit information, physical assets, etc.

The schematic for this project is as follows:

![schematic](Hardware/schematic.png)

This schematic was made with Fritzing http://fritzing.org/home/. I also used
additional parts from the Adafruit fritzing library at https://github.com/adafruit/Fritzing-Library.

#### Raspberry Pi
My Raspberry Pi 3 is based on Raspbian GNU/Linux version 9.

#### The Breadboard
Next to the (half size) breadboard itself, the bill of materials is as follows:

| Part                                          | Notes                        |
| --------------------------------------------- |:----------------------------:|
| DS18B20 1-Wire Temperature Sensor Probe Cable |                              | 
| Adafruit Pi Cobbler                           | Be careful; I bought an old style 26pin cobbler, but for the Raspberry Pi 3 you should get the newer T-shaped 40 pin breakout! I was still able to use the cobbler I bought, by also purchasing a downgrade ribbon cable. |
| 4.7kΩ Resistor                                |                              |
| Jumper wires                                  |                              |

For a more detailed list, see [Hardware/schematic_bom.html](Hardware/schematic_bom.html).

## The Backend
Database, server, API.
- Install peewee, 'pip install peewee'.
- Install pymysql, 'pip install pymysql'.

## The Frontend
API consumer, GUI, client.

# Ideas

- Build process should be able to create DB, deploy necessary artifacts to the 
Pi.