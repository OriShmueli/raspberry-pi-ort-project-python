import tkinter as tk
import serial

window = tk.Tk()
#window.attributes('-fullscreen', True)
window.state('zoomed')

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
serialPortListBox = tk.Listbox(window)


window.mainloop()