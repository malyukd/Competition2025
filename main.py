from GUI import start, root, button_state, com_text, ekg_text, emg_text, getForm2, getEnroll
from functions import connect, is_connected, is_open
from animation import update

def check_connection():
    if getForm2() and getEnroll():
        root.after(10, lambda:update())
    else:
        root.after(100, check_connection)


start()
connect()
root.after(100, check_connection())


root.mainloop()
