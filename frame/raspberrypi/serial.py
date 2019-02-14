# This example shows how to forward serial data from
# the Arduino to the DCD HUB using the credentials
# of a thing.

# This is a typical case for a Python code running
# on a Raspberry Pi to collect data.

from random import random
import time

from dcd.entities.thing import Thing
from dcd.entities.property_type import PropertyType

# The thing ID and the path of file containing the private key
THING_ID = "YOUR-THING-ID"
THING_TOKEN = "REPLACE-WITH-YOUR-TOKEN"

# Instantiate a thing with its credential
my_thing = Thing(thing_id=THING_ID, token=THING_TOKEN)

# We can fetch the details of our thing
my_thing.read()

# If you just registered your Thing on the DCD Hub,
# it has only an id, a name and a type.
print(my_thing.to_json())

# If we have no properties, let's create a random one
if len(my_thing.properties) == 0:
    # By specifying a property type, the DCD Hub will
    # automatically generate the property dimensions
    # (in this case, 3 generic dimensions)
    my_property = my_thing.create_property(name="My Random Property",
                                           property_type=PropertyType.THREE_DIMENSIONS)

    # Let's have a look at the property, it should
    # contains the name, a unique id and the dimensions
    print(my_property.to_json())

# Whether you have just created a property or you retrieved it
# from the DCD Hub (with my_thing.read), you can look for it by name
# WARNING: if you name two property with the same name, the Hub will
# create them both, but this function will randomly return the first
# it finds.
my_property = my_thing.find_property_by_name("My Random Property")


import serial



