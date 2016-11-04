import energenie
import sys

socket1     = energenie.Devices.ENER002((0xBEEF1, 1))
socket2     = energenie.Devices.ENER002((0xBEEF1, 2))
socket3     = energenie.Devices.ENER002((0xBEEF1, 3))
socket4     = energenie.Devices.ENER002((0xBEEF1, 4))

if __name__ == "__main__":
    argCount = len(sys.argv)
    if argCount < 3:
        print("usage: 'python switch.py DEVICE STATE' where DEVICE is a number from 1 to 4 and STATE is on or off")
        sys.exit(1)

    name = sys.argv[1]
    on = sys.argv[2] == "on"

    energenie.init()
    try:
#        device = energenie.registry.get(name)
#        if device.has_switch():
#            print("Switch id %s" % device)
#            device.set_switch(on)
        if name == "1" : socket1.set_switch(on)
        if name == "2" : socket2.set_switch(on)
        if name == "3" : socket3.set_switch(on)
        if name == "4" : socket4.set_switch(on)

    finally:
        energenie.finished()
        