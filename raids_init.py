from tkinter import *
import serial
import datetime

# Global Variables
data_logging = False

# Creating a text file every time  the program runs
file_name = str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
save_file_name = file_name + '-' + 'meta_data_info' + '.txt'
file_name = file_name + '-' + 'data_logger' + '.txt'
file = open(f"F:\\AVIRA\\Data_logger\\{file_name}", 'a+')
file.close()

# Serial Port Parameters Declaration
try:
    stream_1 = serial.Serial('COM3', baudrate=9600, timeout=2)
except Exception as e:
    print(e)

# saving seperate meta data
def save_meta_data():
    global logged_for_entry
    global file_name
    global save_file_name
    global result_entry
    global analysis_entry
    global x_axis
    global y_axis
    global comment_label_text
    save_file = open(f"F:\\AVIRA\\Data_logger\\{save_file_name}", 'a+')
    info_1 = logged_for_entry.get()
    info_2 = result_entry.get()
    info_3 = analysis_entry.get()
    info_4 = x_axis.get()
    info_5 = y_axis.get()
    info = file_name + ',' + info_1 + ',' + info_2 + ',' + info_3 + ',' + info_4 + ',' + info_5
    save_file.write(info)
    save_file.close()
    db_data = '\n' + save_file_name + ',' + info
    with open(f"F:\\AVIRA\\meta_db.csv", 'a') as meta_db_file:
        meta_db_file.write(db_data)
        meta_db_file.close()
        comment_label_text.config(text = 'Saved')

# Enable data logging
def enable_data_logging():
    global file
    global data_logging
    global log_file_name_text_var
    global file_name
    global comment_label_text
    if data_logging == False:
        data_logging = True
        try:
            stream_1.write(b'#')
        except Exception as e:
            print(e)
            comment_label_text.config(text = e)
        log_file_name_text_var.set(file_name)
        file = open(f"F:\\AVIRA\\Data_logger\\{file_name}", 'a')
    else:
        data_logging = False
        try:
            stream_1.write(b'!')
            comment_label_text.config(text = 'Log stop success')
        except Exception as e:
            print(e)
        file.close()

# Storing meta data
def store_meta_data():
    global result_label
    global result_entry
    global analysis_entry
    global analysis_label
    global analyze_for_label
    global x_axis
    global vs_label
    global y_axis
    result_label.config(state = 'normal')
    result_entry.config(state = 'normal')
    analysis_label.config(state = 'normal')
    analysis_entry.config(state = 'normal')
    analyze_for_label.config(state = 'normal')
    x_axis.config(state = 'normal')
    y_axis.config(state = 'normal')
    vs_label.config(state = 'normal')

# Data Logging to file line by line
def log_data():
    file.write(serial_data)

# Exit program
def exit_program():
    global comment_label_text
    global data_logging
    if data_logging == 0:
        root.destroy()
    else:
        comment_label_text.config(text = 'Stop Data logging and save meta data')

# Delaring Screen Parameters
# ----- Screen Declaration -----
root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("1200x700")
root.title("RAIDS")
root.iconbitmap("F:\\AVIRA\Images\\elements\\avira_icon.ico")
root_image = PhotoImage(file="F:\\AVIRA\Images\\elements\\root_bg.png")
quad_icon = PhotoImage(file="F:\\AVIRA\Images\\elements\\quad_icon.gif")
bg_image = Label(root, image=root_image)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)
# Setting up butttons
program_label = Label(root, text='Data Logger', font='Broadway 20',fg='#000000', bg='#a09898')
connect_button = Button(root, image=quad_icon, command=enable_data_logging, bg='#4d3535')
logged_for_entry = Entry(root, width=20)
meta_data_button = Button(root, text="Meta-Data", command=store_meta_data, font='Arial 10', bg='#4d3535')
label1 = Label(root, text='Logging data for:', bg='#f2842b', font='Arial 10', fg='#000000')
log_file_name = Label(root, text='Log file name:', bg='#f2842b', font='Arial 10', fg='#000000')
log_file_name_text_var = StringVar()
log_file_name_text_var.set('NaN')
log_file_name_text = Label(root, textvariable=log_file_name_text_var, bg='#f2842b', font='Arial 10', fg='#000000')
log_file_size = Label(root, text='Log file size:', bg='#f2842b', font='Arial 10', fg='#000000')
log_file_size_text = Label(root, text='NaN', bg='#f2842b', font='Arial 10', fg='#000000')
meta_data_save = Button(root, text="Save", font='Arial 10', bg='#4d3535', command=save_meta_data)
comment_label = Label(root, text='______Comments______', bg='#4d3535', font='Arial 10', fg='#f94444')
comment_label_text = Label(root, text='NaN', bg='#4d3535', font='Arial 10', fg='#f94444')
# Meta data elements
result_label = Label(root, text='Result:', bg='#4d3535', font='Arial 10', fg='white', state=DISABLED)
result_entry = Entry(root, width=20, state=DISABLED)
analysis_label = Label(root, text='Analyze', bg='#4d3535', font='Arial 10', fg='white', state=DISABLED)
analysis_entry = Entry(root, width=20, state=DISABLED)
analyze_for_label = Label(root, text='Analyze for', bg='#4d3535', font='Arial 10', fg='white', state=DISABLED)
x_axis = Entry(root, width=20, state=DISABLED)
vs_label = Label(root, text='vs', bg='#4d3535', font='Arial 10', fg='white', state=DISABLED)
y_axis = Entry(root, width=20, state=DISABLED)
# Exit elements
exit_button = Button(root, text = 'Exit', font='Arial 20', fg='black', bg='#a09898', command=exit_program)
# ------- Placing elements on screen -------
program_label.place(x = 550, y = 10)
logged_for_entry.place(x = 140, y = 50)
# meta data elements
meta_data_button.place(x = 950, y = 50)
result_label.place(x = 850, y = 120)
result_entry.place(x = 950, y = 120)
analysis_label.place(x = 850, y = 160)
analysis_entry.place(x = 950, y = 160)
analyze_for_label.place(x = 900, y = 200)
x_axis.place(x = 875, y = 240)
vs_label.place(x = 925, y = 280)
y_axis.place(x = 875, y = 320)
meta_data_save.place(x = 975, y = 400)
# general elements
label1.place(x = 20, y = 50)
log_file_name.place(x = 20, y = 80)
log_file_name_text.place(x = 140, y = 80)
log_file_size.place(x = 20, y = 110)
log_file_size_text.place(x = 140, y = 110)
connect_button.place(x = 550, y = 600)
comment_label.place(x = 800, y = 600)
comment_label_text.place(x = 800, y = 630)
# exit element
exit_button.place(x = 50, y = 600)

while True:
    while data_logging == False:
        root.update()
    try:
        serial_data = stream_1.readline().decode('utf-8')
        log_data()
        print(serial_data)
    except Exception as e:
        print(e)
    root.update()
