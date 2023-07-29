# This code creates a simple GUI calendar using Tkinter and tkcalendar.

# Import the necessary modules.
import tkinter
import tkcalendar

# Create root window 
rootW=tkinter.Tk()

# Create a function to choose a date from calendar
def chooseDate():
    currentDate=displayCalender.get_date()
    # Create a label to display the selected date.
    global selectedDate
    selectedDate = tkinter.Label(text="Today's Date => " + currentDate)  
    selectedDate.pack(padx= 3,pady= 3)
# Create a calendar widget. 
displayCalender = tkcalendar.Calendar(rootW, setmode = "day", date_patter="dd/mm/yyyy")
displayCalender.pack(padx= 15 ,pady= 15)

# Set the background color of the calendar widget to black.
displayCalender.config(background="black")

# Set the text color of the dates to white.
displayCalender.configure(foreground="white")

# Create a button to open the calendar.
openCalender = tkinter.Button(rootW, text= " Select The Date", command= chooseDate)
openCalender.pack(padx= 14,pady= 14) 

# Set the size,bg colour and title of the window.
rootW.geometry('400x400') 
rootW.title("tkinter GUI Calendar") 
rootW.configure(bg ="green")

# Start the main loop.
rootW.mainloop()
