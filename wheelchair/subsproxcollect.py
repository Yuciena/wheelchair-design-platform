#!/usr/bin/env python3

# Import required library
import pygatt  # To access BLE GATT support
import signal  # To catch the Ctrl+C and end the program properly
import os  # To access environment variables
from dotenv import \
    load_dotenv  # To load the environment variables from the .env file
import time

# DCD Hub
from dcd.entities.thing import Thing
from dcd.entities.property_type import PropertyType

# The thing ID and access token
load_dotenv()
THING_ID = os.environ['THING_ID']
THING_TOKEN = os.environ['THING_TOKEN']
BLUETOOTH_DEVICE_MAC = os.environ['BLUETOOTH_DEVICE_MAC']


# UUID of the GATT characteristic to subscribe
GATT_CHARACTERISTIC_ORIENTATION = "02118833-4455-6677-8899-AABBCCDDEEFF"

# Many devices, e.g. Fitbit, use random addressing, this is required to connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random


def find_or_create(property_name, property_type):
    """Search a property by name, create it if not found, then return it."""
    if my_thing.find_property_by_name(property_name) is None:
        my_thing.create_property(name=property_name,
                                 property_type=property_type)
    return my_thing.find_property_by_name(property_name)


def handle_orientation_data(handle, value_bytes):
    """
    handle -- integer, characteristic read handle the data was received on
    value_bytes -- bytearray, the data returned in the notification
    """
    print("Received data: %s (handle %d)" % (str(value_bytes), handle))
    values = [float(x) for x in value_bytes.decode('utf-8').split(",")]
    find_or_create("Distance",
                   PropertyType.ONE_DIMENSION).update_values(values)


def discover_characteristic(device):
    """List characteristics of a device"""
    for uuid in device.discover_characteristics().keys():
        try:
            print("Read UUID" + str(uuid) + "   " + str(device.char_read(uuid)))
        except:
            print("Something wrong with " + str(uuid))


def read_characteristic(device, characteristic_id):
    """Read a characteristic"""
    return device.char_read(characteristic_id)


def keyboard_interrupt_handler(signal_num, frame):
    """Make sure we close our program properly"""
    print("Exiting...".format(signal_num))
    left_wheel.unsubscribe(GATT_CHARACTERISTIC_ORIENTATION)
    exit(0)




# Sitting classes
CLASSES = ["Close", "Medium", "Far away"]

LABEL_PROP_NAME = "dhaval"
DATA_PROP_NAME = "fsr"

# How many samples do we want for each class
MAX_SAMPLES = 2000
# How much time (in seconds) to leave between the collection of each class
DELAY_BETWEEN_POSTURE = 7

# Collect data for a given posture
# posture_index: index of the class in the array CLASSES
def collect(class_index):
    # if we covered all classes, stop the program
    if class_index >= len(CLASSES):
        print("Data collection done.")
        exit()

    # Prompt the user to get ready and wait
    print("Get ready to collect the posture: " + CLASSES[class_index]
          + " in " + str(DELAY_BETWEEN_POSTURE) + " seconds!")
    time.sleep(DELAY_BETWEEN_POSTURE)

    # Open the serial connection
    print("Collecting data for posture " + CLASSES[class_index])
    my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)
    my_thing.read()

    # Start a BLE adapter
    bleAdapter = pygatt.GATTToolBackend()
    bleAdapter.start()

    # Use the BLE adapter to connect to our device
    left_wheel = bleAdapter.connect(BLUETOOTH_DEVICE_MAC, address_type=ADDRESS_TYPE)

    # Subscribe to the GATT service
    left_wheel.subscribe(GATT_CHARACTERISTIC_ORIENTATION,
                         callback=handle_orientation_data)

    # Start reading serial port with the posture index, start at sample 0.
    sample = 0
    while sample < MAX_SAMPLES:
        if my_thing.read():
            sample += 1
            print()
    collect(class_index + 1)




# Register our Keyboard handler to exit
signal.signal(signal.SIGINT, keyboard_interrupt_handler)
