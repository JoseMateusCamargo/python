import pywhatkit as kit

# Documentation: https://pypi.org/project/pywhatkit
# Using Exception Handling to avoid unprecedented errors
try:

    number = '+55910123456789'

    # Send a WhatsApp Message to a Contact at 1:30 PM
    kit.sendwhatmsg(number, "Hi", 13, 30)

    # Same as above but Closes the Tab in 2 Seconds after Sending the Message
    kit.sendwhatmsg(number, "Hi", 13, 30, 15, True, 2)

    # Send an Image to a Group with the Caption as Hello
    kit.sendwhats_image(number, "Images/Hello.png", "Hello")

    # Send an Image to a Contact with the no Caption
    kit.sendwhats_image(number, "Images/Hello.png")

    # Send a WhatsApp Message to a Group at 12:00 AM
    kit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

    # Play a Video on YouTube
    kit.playonyt("PyWhatKit")

    print("Successfully Sent!")

except:
    # Handling exception and printing error message
    print("An Unexpected Error!")
