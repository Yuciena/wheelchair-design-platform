
# Magic Wheelchair
### Connected smart wheelchair for IKEA customers

### Purpose of your prototype
“Make the IKEA shopping experience accessible for the customers on wheelchairs”

### Context:
the disabled buying (small) furniture in IKEA by themselves

## Brief context
IKEA vision:
“To create a better everyday life for the many people”

### Current situation
IKEA stores are huge. These sprawling stores easily take up the length of a football field. It also has very narrow pathways and is often very crowded.Therefore, this makes it difficult to manoeuvre through the shop. In the storage pickup, customers often cannot reach the products on the shelf and need help from IKEA staff. Things are more severe for the customers on the wheelchairs.

### Our vision:
For the considerable size of IKEA, having electric powered wheelchairs with gps navigations on them would make it easier for the customers on wheelchairs to get around;
To help customers be aware of the surrounding situations when they are going around would make their IKEA journey more guaranteed;
To warn customers the risk of flipping over simultaneously could ensure a safe and friendly IKEA journey;
To provide help whenever it is needed.

### Stakeholders:
Ikea customers, wheelchair company, Ikea staff, furnitures etc.

### Ikea Journey on The Wheelchair Alone / Ikea Magic Wheelchair:
Entrance → Find Elevator and find routes(GPS) → Visit sample room(Proximity / Vibration / Speaker / Camera) → Scan the barcode of furniture → Look for the furniture in the warehouse(Proximity / Bluetooth / Button) → Checkout

### Poster and video
You can see our video here: https://www.youtube.com/watch?v=OvhNTrp6YjQ&t=57s

![IoT1 Exhibition](/docs/resources/images/poster.jpg)
=======

### Sensors:
#### - Sensor1: Proximity
Detect surrounding objects and people in order to avoid accidents when navigating through the shop. We set the proximity sensor on the back of the wheelchair as the disabled normally cannot notice the objects and people back.
#### - Sensor 2: Network detection with beacon
Navigate the visiting routes and to specific areas inside of the IKEA building in order to help the disabled find the right places where they want to visit.

#### - Sensor 3: Orientation
To detect the Z axis of the wheelchair and to predict/give warning whether it is going to flip.
#### - Sensor 4: Button
Activate the button and send the signal to the IKEA staff that they need help when they cannot reach products on the shelf.



### Actuator:
#### - Actuator 2: Vibration
Combined with the proximity sensor, it gives warning for disabled people when the wheelchair is detected to be too close to surrounding objects.
#### - Actuator 1: Speaker
Combined with the network detection sensor, the speaker guides the disabled direction verbally.
#### - Actuator3: Light
Flashing the light to warn the risk of flipping over when the angle of the wheelchair dumping to one side is too large.


## components

### ARDUINO MEGA
Location: the wheelchair main frame
Script:	arduino_prox_vibr.ino
Connected to: Vibration motor (Physical, wires) on the back of the wheelchair seat | Powerbank (Physical, USB B)

### ADAFRUIT FEATHER BLUEFRUIT 32u4
Location: breadboard on the wheelchair main frame
Script: bno055_gatt_service.ino
Connected to: RASPBERRY PI (Bluetooth connection)  | BNO055 (Physical, wires) | POWERBANK (Physical, Micro USB)

### RASPBERRY PI
Location: the wheelchair main frame
Script: subscribe_gatt_orientation0.py
Connected to: POWERBANK (Physical, Micro USB)

### BNO055 IMU x2
Location: breadboard on the wheelchair main frame
Connected to:	ADAFRUIT FEATHER (Physical, wires)

### POWERBANK x3
Location:	3x the wheelchair main frame
Connected to:	RASPBERRY PI (Physical, USB) | ADAFRUIT FEATHER (Physical, Micro USB) | ARDUINO MEGA (Physical, USB B)

### USB CABLE
Location: between Raspberry Pi and Powerbank

### MICRO USB CABLE
Location: between Adafruit Bluefruit and Powerbank

### USB B CABLE
Location: between Raspberry Pi and powerbank.



## Step-by-step instructions
#### Create a project and repository in Github and clone repository
#### Sign up on the Data-Centric Design Hub and install the dependencies in Atom
Create a thing in DCD hub and generates an access token for your Thing. This Python dependency is a communication protocol to talk to the DCD hub.
#### Set environmental variables
Find the .env file and set the thing id and token
#### Connect your raspberry pi to the network
Plug in the Micro SD card into your laptop, create a file for setting up your network details and connect the pi to the power bank
#### Log into the Pi with ssh and clone the repository on your Pi
#### Set the thing Id and token on your Pi
#### Install Python dependencies on the Pi
#### Install feather dependencies in Python
#### Download libraries in Arduino
<open Arduino<Sketch<included library<manage libraries<search and download Adafruit BNO055, Adafruit BluefruitLE nRF51
#### Open and upload the file (arduino_prox_vibr.info) from github and open in Arduino Mega
#### Open the file of bno055_gatt_service.ino, set the name of the feather and Setup Orientation GATT service with UUID
#### Upload the file(bno055_gatt_service.ino) to the feather
#### Find the MAC address of your feather and add it to the .env file
#### Put the main components on the wheelchair and wire the components
see the previous chapter (Components)
#### Run the code from the file of subscrib_gatt_orientation.py
#### GO to Grafana, select the property ID and set the value of your data and then you can see the data visualization in Grafana


## Remaining files in the directory 'wheelchair':

### dcd_hub.py
This code can be used to test the connection with the server used for this project. It will indicate whether the connection has been established successfully or not.

### get_started.py
This code can be used to test whether you are able to receive data on Grafana, a data visualisation tool connected to the dcd_hub (server). It generates a random property with a unique ID, which can be used to identify the property on Grafana.



# Wheelchair Design Platform

Wheelchair Design Platform is a repository that contains some resources to help
designers and developers speak the same language, and work together towards
addressing relevant challenges for wheelchair users. It is a collection of
workshop materials, code examples and also a compilation of resources to foster
a prospering research and design community around wheelchair users.


![IoT1 Exhibition](/docs/workshops/images/iot1_exhibition.jpg)

## Workshops


* [Getting started](/docs/workshops/GettingStarted.md)
* [Workshop 1: Building an Internet-Connected Wheelchair](/docs/workshops/Workshop1.md)
* [Workshop 2: Integrating and Visualising Sensor-Based Data](/docs/workshops/Workshop2.md)
* [Workshop 3: Developing Algorithms and Controlling Actuators](/docs/workshops/Workshop3.md)
* [Workshop 4: Developing and Conducting a Data Collection Campaign](/docs/workshops/Workshop4.md)
* [Workshop 5: Implementing a Machine Learning Pipeline](/docs/workshops/Workshop5.md)
* [Workshop 6: Developing a Product Analytics Dashboard](/docs/workshops/Workshop6.md)

## Resources

* This platform uses two programming languages, Python on computers and C on
micro-controllers. While descriptions and examples of code should help you
get started, you can find some additional resources
[here](/docs/resources/software.md "Python and C resources").

* Documentation of your project is key,
[here are some tips and examples](/docs/resources/documentation.md "Documentation tips and examples").

* [Git manipulation such as Pull Request](/docs/resources/git.md "Git manipulation").



## List of suggested components:

On the frame:

* 1 Raspberry Pi 3B;
* 1 SD card (Some come directly with NOOBS installed);
* 1 Arduino Mega;
* 1 Large power bank;
* 1 large breadboard;
* 1 USB cable A/micro (Powerbank to Raspberry Pi);
* 1 USB cable A/B (Raspberry Pi to Arduino Mega).

On the wheel:

* 1 Feather (Bluetooth enabled);
* 1 small power bank;
* 1 small breadboard;
* 1 USB cable A/B (power bank to Arduino Uno).


## Contact and Existing projects

* [The hiking wheelchair](https://github.com/cprecioso/wheelchair-design-platform)
* [The EDU wheelchair](https://github.com/ctsai-1/wheelchair-design-platform)
* [Weelchair tracking for basketball players](https://github.com/FabianIDE/wheelchair-design-platform)
* [Disco Wheelchair](https://github.com/MatthijsBrem/wheelchair-design-platform)
* [Wheelchair Madness 2222](https://github.com/pherkan/wheelchair-design-platform/tree/master/wheelchair)
* [Who is sitting?](https://github.com/Rosanfoppen/wheelchair-design-platform/tree/master/wheelchair)
* [Magic Wheelchair](https://github.com/Yuciena/wheelchair-design-platform)
* [Yoga Wheelchair](https://github.com/artgomad/wheelchair-design-platform)


Feel free to contact us at jacky@datacentricdesign.org. We welcome feedback, pull requests
or links to your project.
