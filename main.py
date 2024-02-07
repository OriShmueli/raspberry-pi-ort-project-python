import tkinter as tk
import serial

window = tk.Tk()
#window.attributes('-fullscreen', True)
#window.state('zoomed')
window.geometry("1024x600")

isConnected = False

def ConnectToArduino():
    connectButton["state"] = "disabled"
    startButton.config(bg='gray')
 
connectButton = tk.Button(window, text='Connect', command=ConnectToArduino, bg='green')
connectButton.place(x=80, y=110)


operation = True

def Operation():
    global operation
    print(bool(operation))
    if operation:
        
        startButton.config(text="Stop Operation", bg='red') 
        operation = not operation
        return
    
    if not operation:
        startButton.config(text="Start operation", bg='green')
        operation = not operation
    
   

startButton = tk.Button(window, text='Start operation', command=Operation, bg='green')
#startButton.pack()
startButton.place(x=50, y=50)

#list box
#serialPortListBox = tk.Listbox(window)


#Connecteion status Labels
connectionStatusLabelTitle = tk.Label(window, text = "Connection status: ")
connectionStatusLabelTitle.pack()

arduinoMotorConnectionStatusLabel = tk.Label(window, text = "arduino motor: ")
arduinoMotorConnectionStatusLabel.pack()

arduinoSensorsConnectionStatusLabel = tk.Label(window, text = "arduino sensors: ")
arduinoSensorsConnectionStatusLabel.pack()

#Connection status text
arduinoMotorConnectionStatusText = tk.Text(window)
arduinoSensorsConnectionStatusText = tk.Text(window)
    #TODO: place them together 

#distance sensor
distanceSensorLabel = tk.Label(window, text = "Distance: ")
distanceSensorLabel.pack()

distanceSensorText = tk.Text(window)

#color sensor
colorSensorLabel = tk.Label(window, text = "Color: ")
colorSensorLabel.pack()

colorSensorText = tk.Text(window)

#conveyor belt status
conveyorBeltStatusLabel = tk.Label(window, text = "Conveyor Belt Status: ")
conveyorBeltStatusLabel.pack()

conveyorBeltStatusText = tk.Text()

#error timer
errorTimerArduinoSensorsLabel = tk.Label(window, text = "Error Timer: ")
errorTimerArduinoMotorLabel = tk.Label(window, text = "Error Timer: ")

errorTimerArduinoSensorsText = tk.Label(window)
errorTimerArduinoMotorText = tk.Label(window)
window.mainloop()