
# Magic Wheelchair

## Assignment 1

### Context:
the disabled buying (small) furniture in IKEA by themselves

### User:
Needs to navigate through the shop, which has very narrow pathways and is often very crowded. This makes it difficult to manoeuvre through the shop. Also finding and using the trolley to pick up products becomes a problem since the user cannot push it forward. Then in the storage pickup, the user often cannot reach the products on the shelf and needs help from the staff.

### Stakeholders:
Ikea customers, wheelchair company, Ikea stuff, Ikea trolley, furnitures etc.

### Ikea Journey on The Wheelchair Alone / Ikea Magic Wheelchair:
Entrance → Find Elevator and find routes(GPS) → Visit sample room(Proximity / Vibration / Speaker / Camera) → Scan the barcode of furniture → Look for the furniture in the warehouse(Proximity / Bluetooth / Button) → Checkout

### Sensors:
#### - GPS (Beacon) = not implemented：
Navigate the visiting routes and to specific areas inside of the IKEA building in order to help the disabled find the right places where they want to visit. (Network detection in building with beacons?)
#### - Proximity sensors:
Detect surrounding objects and people in order to avoid accidents when navigating through the shop. This sensor can also be used for a follow-me system build in the trolley, which can follow the wheelchair, so that the wheelchair user does not have to push the trolley.
#### - Accelerator sensor
To detect whether the wheelchair user is going to fall. For example when riding on a slope or over a bump the wheelchair might get tilted.
#### - Button:
Activate the button and send the signal to the IKEA staff that they need help when they cannot get the stuff by themselves

## Assignment 2:

### Actuator:
#### - Vibration：
Combined with GPS and give the disabled command of directions through either a vibration actuator or a speaker actuator
#### - speaker = not implemented:  
To give verbal guidance for disabled people when the wheelchair is detected to be too close to surrounding objects.
#### - Light (LED):
The light is showing the wheelchair user whether the wheelchair is tilted to much: (risk of falling)

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

## Main Components

__**Disclaimer:**__ the design of this platform focuses on flexibility and
technology exploration rather than optimisation.

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
