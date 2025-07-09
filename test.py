from GUI import start, root, button_state, com_text, ekg_text, emg_text, getForm2, getEnroll, ekg_write, video_block, indicator_start, indicator_succes, indicator_fail
from face_rec import face_check
from functions import connect, is_connected, is_open
from animation import update
import time

start()
indicator_start(True)
root.update()
res=face_check()
indicator_start(False)
while not res:
    indicator_fail(True)
    root.update()
    res = face_check()
    indicator_fail(False)
indicator_succes(True)
root.update()
time.sleep(3)
indicator_succes(False)
time.sleep(1)


root.mainloop()
