
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
<<<<<<< HEAD
You can see our video here: https://www.youtube.com/watch?v=OvhNTrp6YjQ&t=57s
=======
You can see our video here: https://www.youtube.com/watch?v=OvhNTrp6YjQ

<<<<<<< HEAD
![IoT1 Exhibition](/docs/resources/images/poster.jpg)
=======
![IoT1 Exhibition](/docs/workshops/images/poster a1-01.jpg)
>>>>>>> fdbbd994d339afc9843c6f748030f1e5ccfeab80
>>>>>>> b4df906ad302ae56cc51b7c3f828dfa9cf5c34c9

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


## How to wire the hardware

### connect the orientation sensor to the Blue Feather
![IoT1 Exhibition](/docs/resources/images/orientation_2.png)

### connect the vibration motor to the Arduino Omega
![IoT1 Exhibition](/docs/resources/images/vibration_2.png) 


## Main Components

The main design includes a Raspberry Pi 3 and an Arduino Mega 2560 on the wheelchair frame.

The Arduino Mega is the micro-controller of the platform. Fixed on the main frame of the wheelchair,
it can collect data from sensors (e.g. force sensors, accelerometers), and trigger actions from actuators
(e.g. LEDs, vibration motors).

More on the Arduino Mega can be found [here](/docs/resources/arduino.md "Arduino resources").

Raspberry Pi is a small computer. It is also fixed to the main frame of the wheelchair,
where it can:
* interact with the Arduino Mega via USB to receive data and transmit commands;
* interact with the Internet to transmit commands and receive data;
* store data locally in files;
* run (machine learning) algorithms.

More on the Raspberry Pi can be found [here](/docs/resources/raspberrypi.md "Raspberry Pi resources").

These components fit together as shown on the following diagram. A large powerbank
powers the Raspberry Pi. The Arduino Mega communicates and receives power from the
Raspberry Pi via USB. A Feather (Arduino-like development board) on the wheel connects to
the Raspberry Pi via Bluetooth to sense and actuate from the wheel.

![Main Wheelchair components](/docs/workshops/images/wheechair-components.png)

### Step-by-step instructions
#### Create a project and repository in Github and clone repository
#### Sign up on the Data-Centric Design Hub
Create a thing in DCD hub and generates an access token for your Thing.
#### Install Python dependencies 
This Python dependency is a communication protocol to talk to the DCD hub.
#### Set environmental variables
It is to read the id and access token of our thing
#### Find and download the files (##fixme) from github and open in Arduino
#### Download libraries in Arduino
<open Arduino<Sketch<included library<manage libraries<search and download Adafruit BNO055, Adafruit BluefruitLE nRF51 #FIXME Proximity
#### Upload *** to the Arduino
#### Upload *** to the feather
#### Upload *** to the Raspberry Pi
#### Put the main components on the wheelchair
Put the Raspberry Pi and power bank to the right of wheelchair main frame
Put the Aurdino Mega, power bank, Feather and orientation sensor with breadboard to the left of wheelchair main frame
Put the proximity sensor on the back of the wheelchair
Put the vibration actuator on the front of the wheelchair where users can detect the vibration while leaning on it.
#### Wire the components ======> link to how to wire the hardware FIXMEXXXX
#### 



## Files in the directory 'wheelchair':

### bno055_gatt_service
This code is run on the Blue Feather to detect the orientation from the orientation sensor.
It writes the data to both the serial port of the laptop and the serial port of the bluetooth device. Anyone who subscribes to the bluetooth device can see the data.

### IRDistance_gatt_service
This code is run on the Blue Feather to detect the distance of an object to the proximity sensor.
It writes the data to both the serial port of the laptop and the serial port of the bluetooth device. Anyone who subscribes to the bluetooth device can see the data.

### push_button_led_log
This code is run on an arduino board to detect whether the button is pressed or not. If the button is pressed =, the LED goes on. If the button is not pressed the LED will be off. This code has been copied from the arduino example folder of the main repository to explore how activity of a
button can be detected and how to send a signal to the LED. For the project this code can be broken down into the a piece for warning the IKEA staff (button) and warning the user of the risk of falling (LED).

### dcd_hub.py
This code has been used to test the connection with the server used for this project. It will indicate whether the connection has been established successfully or not.

### get_started.py
This code has been used to test whether we were able to receive data on Grafana, a data visualisation tool connected to the dcd_hub (server). It generates a random property with a unique ID, which can be used to identify the property on Grafana.

### serial_example.py
This code is meant to read data from the serial port of your laptop and send it to the server, so that it can be visualised on Grafana.

### subscribe_gatt_orientation.py
This code is run on the raspberry pi to subscribe the pi to the Blue Feather. The raspberry pi will read the data from the orientation sensor that the Feather is sending and then the pi sends it to the dcd_hub server, so that it can be visualised on grafana.

### subscribe_gatt_proximity.py
This code is run on the raspberry pi to subscribe the pi to the Blue Feather. The raspberry pi will read the data from the proximity sensor that the Feather is sending and then the pi sends it to the dcd_hub server, so that it can be visualised on grafana.

### ml/1_collect_and_label.py
...


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
