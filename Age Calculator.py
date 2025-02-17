from tkinter import *
from tkinter import messagebox


def clearAll():
    # deleting the content from the entry box
    b_day_field.delete(0, END)
    b_month_Field.delete(0, END)
    b_year_field.delete(0, END)
    input_day_field.delete(0, END)
    input_month_field.delete(0, END)
    input_year_field.delete(0, END)
    res_day_field.delete(0, END)
    res_month_field.delete(0, END)
    res_year_field.delete(0, END)

# function for checking error
def checkError():
    # if any of the entry field is empty
    # then show an error message and clear all the entries
    if (b_day_field.get() == "" or b_month_field.get() == ""
            or b_year_field.get() == "" or input_day_field.get() == ""
            or input_month_field.get() == "" or input_year_field.get() == ""):
        messagebox.showerror("Error!", "Input Error")
        clearAll()
        return -1


# function to calculate Age
def calculateAge():
    # check for error
    value = checkError()

    # if error is occur then return
    if value == -1:
        return

    else:
        # take a value from the respective entry boxes
        # get method returns current text as string
        birth_day = int(b_day_field.get())
        birth_month = int(b_month_field.get())
        birth_year = int(b_year_field.get())

        given_day = int(input_day_field.get())
        given_month = int(input_month_field.get())
        given_year = int(input_year_field.get())

        # if birth date is greater then given birth_month
        # then donot count this month and add 30 to the date so
        # as to subtract the date and get the remaining days
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

            # if birth month exceeds given month, then
        # donot count this year and add 12 to the
        # month so that we can subtract and find out
        # the difference
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12

        # calculate day, month, year
        calculated_day = given_day - birth_day;
        calculated_month = given_month - birth_month;
        calculated_year = given_year - birth_year;

        # calculated day, month, year write back
        # to the respective entry boxes

        # insert method inserting the
        # value in the text entry box.

        res_day_field.insert(10, str(calculated_day))
        res_month_field.insert(10, str(calculated_month))
        res_year_field.insert(10, str(calculated_year))


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.configure(background="light blue")

    # set the name of tkinter GUI window
    gui.title("Age Calculator")

    # Set the configuration of GUI window
    gui.geometry("500x280")

    # Create a Date Of Birth : label
    dob = Label(gui, text="Date Of Birth", bg="yellow")

    # Create a Given Date : label
    givenDate = Label(gui, text="Input Date", bg="yellow")

    # Create a Day : label
    day = Label(gui, text="Day", bg="light blue")

    # Create a Month : label
    month = Label(gui, text="Month", bg="light blue")

    # Create a Year : label
    year = Label(gui, text="Year", bg="light blue")

    # Create a Given Day : label
    givenDay = Label(gui, text="Given Day", bg="light blue")

    # Create a Given Month : label
    givenMonth = Label(gui, text="Given Month", bg="light blue")

    # Create a Given Year : label
    givenYear = Label(gui, text="Given Year", bg="light blue")

    # Create a Years : label
    rsltYear = Label(gui, text="Years", bg="light blue")

    # Create a Months : label
    rsltMonth = Label(gui, text="Months", bg="light blue")

    # Create a Days : label
    rsltDay = Label(gui, text="Days", bg="light blue")

    # Create a Resultant Age Button and attached to calculateAge function
    calculate_Age = Button(gui, text="Calculate Age", fg="white", bg="Gray", command=calculateAge)

    # Create a Clear All Button and attached to clearAll function
    clearAllEntry = Button(gui, text="Clear All", fg="Black", bg="Red", command=clearAll)

    # Create a text entry box for filling or typing the information.
    b_day_field = Entry(gui)
    b_month_field = Entry(gui)
    b_year_field = Entry(gui)

    input_day_field = Entry(gui)
    input_month_field = Entry(gui)
    input_year_field = Entry(gui)

    res_day_field = Entry(gui)
    res_month_field = Entry(gui)
    res_year_field = Entry(gui)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    dob.grid(row=0, column=1)

    day.grid(row=1, column=0)
    b_day_field.grid(row=1, column=1)

    month.grid(row=2, column=0)
    b_month_field.grid(row=2, column=1)

    year.grid(row=3, column=0)
    b_year_field.grid(row=3, column=1)

    givenDate.grid(row=0, column=4)

    givenDay.grid(row=1, column=3)
    input_day_field.grid(row=1, column=4)

    givenMonth.grid(row=2, column=3)
    input_month_field.grid(row=2, column=4)

    givenYear.grid(row=3, column=3)
    input_year_field.grid(row=3, column=4)

    calculate_Age.grid(row=4, column=2)

    rsltYear.grid(row=5, column=2)
    res_year_field.grid(row=6, column=2)

    rsltMonth.grid(row=7, column=2)
    res_month_field.grid(row=8, column=2)

    rsltDay.grid(row=9, column=2)
    res_day_field.grid(row=10, column=2)

    clearAllEntry.grid(row=12, column=2)

    # Start the GUI
    gui.mainloop()
