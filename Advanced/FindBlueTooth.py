# sudo apt install bluetooth libbluetooth-dev
# pip3 install pybluez
# Reference: http://blog.kevindoran.co/bluetooth-programming-with-python-3/
# !/usr/bin/python3

# geektechstuff bluetooth

import bluetooth


def scan():
    print("Scanning for bluetooth devices:")

    devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)

    number_of_devices = len(devices)

    print(number_of_devices, "devices found")

    for addr, name, device_class in devices:
        print("\n")

        print("Device:")

        print("Device Name: %s" % (name))

        print("Device MAC Address: %s" % (addr))

        print("Device Class: %s" % (device_class))

        print("\n")

    return


def scan_services():
    print("Scanning for bluetooth devices: ")

    devices = bluetooth.discover_devices(lookup_names=True)

    number_of_devices = len(devices)

    print(number_of_devices, "devices found")

    for addr, name in devices:

        print("\n")

        print("Device Name: %s" % (name))

        print("Device MAC Address: %s" % (addr))

        print("Services Found:")

        services = bluetooth.find_service(address=addr)

        if len(services) <= 0:

            print("zero services found on", addr)

        else:

            for serv in services:
                print(serv['name'])

        print("\n")

    return ()


# scanning devices
scan()

# scand services
scan_services()
