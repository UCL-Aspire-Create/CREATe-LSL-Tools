from LSL_controller import LSL_controller

running = True

print("LSL custom marker for openvibe ")
print("enter a number between 0 and 9")
controller = LSL_controller()

while(running):

    marker = input(">>").strip()
    controller.send_marker(marker)

