import energenie
import sys

if __name__ == "__main__":

    argCount = len(sys.argv)
    if argCount < 3:
        print("usage: 'python switch.py DEVICE STATE' where DEVICE is a switch in registry and STATE is on or off")
        sys.exit(1)

    name = sys.argv[1]
    on = sys.argv[2] == "on"

    energenie.init()
    try:
        device = energenie.registry.get(name)
        if device.has_switch():
            print("Switch id %s" % device)
            device.set_switch(on)
    finally:
        energenie.finished()
        