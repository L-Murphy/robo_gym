import PySimpleGUI as sg
from datetime import date, time
import os.path
import web as web

#Want to create a calendar looking thing. 
WEEKEND_TIMESLOTS = ['7 - 9:30 AM', '9:30 - 11 AM', '11 AM - 12:30 PM', '12:30 - 2 PM', '2 - 3:30 PM', '3:30 - 5 PM', '5 - 6:30 PM', '6:30 - 8 PM', '8 - 9:30 PM']
WEEKDAY_TIMESLOTS = ['6 - 7:30 AM','7:30 - 9 AM','9 - 10:30 AM','10:30 AM - 12 PM','12 - 1:30 PM','1:30 - 3 PM','3 - 4:30 PM','4:30 - 6 PM','6 - 7:30 PM','7:30 - 9 PM','9 - 10:45 PM']

def make_login_window():
    login_layout = [ [sg.Text('Enter username:'), sg.InputText()],
                     [sg.Text('Enter username:'), sg.InputText()],
                     [sg.Button('Save'), sg.Button('Cancel')] ]

    return sg.Window("Login Screen", login_layout, finalize=True, modal=True)

def make_main_window():
    sg.theme('GrayGrayGray')
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")      
    col1 = [ [sg.Text('Choose the day')], [sg.Listbox(days, size=(20, len(days)), key='-day-', enable_events=True)] ]
    col2 = [ [sg.Text('Choose the timeslot')],[sg.Listbox(WEEKDAY_TIMESLOTS, size=(20, len(days)), key='-timeslot-')] ]

    layout = [[sg.Column(col1, element_justification='c'), sg.Column(col2, element_justification='c')],[sg.Button('Choose')]]

    return sg.Window('Choose a date and timeslot', layout, [1600,1600], finalize=True)

def make_calendar():
    layout = [[sg.Text("This is for the calendar"), 
             [sg.CalendarButton()]
    ]]
    return sg.Window("Calendar", layout, finalize=True, modal=True)

# def event(event, values):


def main():

    window1, window2 = make_main_window(), None
    if  not os.path.isfile('./login.txt'):
        window2 = make_login_window()


    while True:     
        window, event, values = sg.read_all_windows()
        if event in (None, 'Exit'): 
            window.close()
            if window == window2:
                window2 = None
            else:
                break

        if values['-day-']:
            if values['-day-'][0] in ('Saturday', 'Sunday'):
                window['-timeslot-'].update(WEEKEND_TIMESLOTS)
            else:
                window['-timeslot-'].update(WEEKDAY_TIMESLOTS)

        if event == 'Choose':
            # Do something with this data.
            if len(values['-day-']) == 0 or len(values['-timeslot-']) == 0:
                sg.popup("Please choose a day and timeslot")
            else:
                day = values['-day-'][0]
                time_slot = values['-timeslot-'][0]
                print(f"{day}, {time_slot}")
                if values['-day-'][0] in ('Saturday', 'Sunday'):
                    web.run(WEEKEND_TIMESLOTS.index(time_slot))
                else:                    
                    web.run(WEEKDAY_TIMESLOTS.index(time_slot))



        if event == 'Save':
            #Create the login.txt file
            print(f"Thank you {values[0]}")
            file = open("login.txt", "w")
            file.write(values[0] + "\n")
            file.write(values[1])
            file.close()

    window.close()

if __name__ == "__main__":
    main()

