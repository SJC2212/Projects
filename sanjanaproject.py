# Python Program for Internet speed test

# import neccesary modules
from tkinter import *
# from turtle import speed
import speedtest_cli


# function for speed check
def speedcheck():
    # Create an instance of Speedtest and call it sp
    sp = speedtest_cli.Speedtest()
    sp.get_servers()
    # converting to Mbps
    down = str(round(sp.download() / (10 ** 6), 3)) + "Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + "Mbps"
    # fetching download speed
    lab_down.config(text=down)
    # fetching upload speed
    lab_up.config(text=up)


# gui
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg="Black")
# designing label
# we use the label method to generate a label of text of internet speed test,download speed,upload speed
lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="Black", fg="White")
lab.place(x=60, y=30, height=50, width=380)
# making label to show download speed
lab = Label(sp, text="Download Speed ⏬", font=("Time New Roman", 20, "bold"))
lab.place(x=60, y=120, height=50, width=380)
lab_down = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
lab_down.place(x=60, y=190, height=50, width=380)
# making label to show upload speed
lab = Label(sp, text="Upload Speed ⏫", font=("Time New Roman", 20, "bold"))
lab.place(x=60, y=280, height=50, width=380)
lab_up = Label(sp, text="00", font=("Time New Roman", 20, "bold"))
lab_up.place(x=60, y=350, height=50, width=380)
# button for call to function
# we code a check button on which we click to check the speed of internet
# we give our button some styling along with the name-"Check Speed"
# We give our button some styling, along with the name – ‘Check Speed’. We use the ‘command‘ widget, which shows what
# function (here, speedcheck function) would run on the click (key press) of the button, as coded in the previous step.
button = Button(sp, text="Check Speed", font=("Time New Roman", 20, "bold"), bg="Red", fg="Black", relief=RAISED,
                command=speedcheck)
button.place(x=60, y=450, height=50, width=380)

sp.mainloop()
