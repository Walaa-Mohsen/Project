from tkinter import *
import calendar

window = Tk()
window.title("Calender")
window.geometry("320x200")
window.config(bg='grey')

cal = Label(window, text="Calender", bg="grey", font="Times 22 bold")
cal.grid(row=0, column=0)
year = Label(window, text="Enter year", fg="white", bg="grey", font="Times 22 bold")
year.grid(row=1, column=0)
year_field=Entry(window, width=20, bg="white", fg="black", borderwidth=10, font="Times 22 bold")
year_field.grid(row=2, column=0)

def showCalender():
    window2 = Tk()
    window2.title('Calender for the year')
    window2.geometry("550x600")
    window2.config(bg="grey")

    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(window2, text= gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)

button = Button(window, text="Show Calender",fg="white",bg="Blue", borderwidth=5, command=showCalender)
button.grid(row=3, column=0)

window.mainloop()