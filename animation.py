from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from values import VIEW, VIEW2, STEP, trigger_pulse, x_data, x2_data, y_data, y2_data, trigger_emg
from functions import data, connect
import time
from GUI import ekg_fig, emg_fig, line, line2, ax1, ax2, root, ekg_write, emg_write, status, research, video_block 
from GUI import getPause, indicator_fail, indicator_succes, indicator_red, indicator_start, indicator_yellow, stop, play
from face_rec import face_check, isChecked


RESEARCH =False
START = 0 
END = 0
SYSTEM =False


video_status = False

START2=0
END2=0

stop_=0
play_=0

pulse = 0
timer = time.time()
pulse_min=2000
pulse_mid=0
pulse_max=0
ekg_mid=0

emg_min=2000
emg_mid=0
emg_max=0
up = False

signals =0
ind=0
fist=0
pause=0

def emg_data(emg, ekg):
    global ekg_mid, emg_min, emg_mid, emg_max, fist
    if ekg_mid == 0:
        ekg_mid = ekg
    else:
        ekg_mid=(ekg+ekg_mid)/2

    if emg_max<emg:
        emg_max=emg
    if emg_min > emg:
        emg_min = emg
    if emg_mid == 0:
        emg_mid = emg
    else:
        emg_mid=(emg+emg_mid)/2

    emg_write(fist, emg_min, emg_mid, emg_max)

def pulse_data(pulse):
    global pulse_min, pulse_mid, pulse_max
    if pulse_max<pulse:
        pulse_max=pulse
    if pulse_min > pulse:
        pulse_min = pulse
    if pulse_mid == 0:
        pulse_mid = pulse
    else:
        pulse_mid=(pulse+pulse_mid)/2

    ekg_write(pulse, pulse_min, pulse_mid, pulse_max)
    status(pulse)
    


def update():
    global START, END, START2, END2, x_data, x2_data, y_data, y2_data, y3_data, ekg_mid, emg_mid, timer, pulse, up, signals, ind, pause, fist, RESEARCH, video_status, stop_, play_, SYSTEM
    if video_status:
        play_+=1
        stop_=0
    else:
        stop_+=1
        play_=0

    if getPause() == 1:
        if END>VIEW:
            START+=STEP
            ax1.set_xlim([START, END])
            if x_data:
                x_data.pop(0)
                y_data.pop(0)
        if END2>VIEW2:
            START2+=STEP
            ax2.set_xlim([START2, END2])
            if x2_data:
                x2_data.pop(0)
                y2_data.pop(0)

        END+=STEP
        END2+=STEP
        try:
            result = data(ekg_mid, emg_mid)
        except:
            return None
        if result is not None:
            result_ekg = result[0]
            result_emg = result[1]

            emg_data(result_emg,result_ekg)

            if up==False and result_ekg>trigger_pulse:
                up=True
            if up==True and result_ekg<trigger_pulse:
                up=False
                pulse+=2


            if ind < 10:
                if result_emg > 28 or result_emg<22:
                    signals+=1
                ind+=1
                pause+=1
            else:
                ind=0
                if signals > 2:
                    fist+=1
                    
                    pause=0
                    if RESEARCH and signals>2:
                        if video_status and play_>20:
                            print("stop")
                            stop()
                            print("stop")
                            video_status=False
                        if not video_status and stop_>20:
                            print("play")
                            if not SYSTEM:
                                play()
                                video_status=True
                            elif signals>5:
                                play()
                                video_status=True
                            print("play")
                            
                            SYSTEM=False
                            indicator_red(False)

                    signals=0
                if pause>100:
                    fist=0
                    pause=0
            
            if RESEARCH==False:
                RESEARCH=True
                research()
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
                root.update()
                time.sleep(1)
                video_block()
                video_status = True
                
                

            if time.time() - timer > 15:
                pulse=pulse*4
                pulse_data(pulse)
                if RESEARCH and pulse>120:
                    indicator_yellow(True)
                else:
                    indicator_yellow(False)
                pulse=0
                timer=time.time()
            
            y_data.append(result_ekg)
            y2_data.append(result_emg)

            x_data.append(END)
            x2_data.append(END2)

        line.set_data(x_data, y_data)
        line2.set_data(x2_data, y2_data)

        if not RESEARCH:
            pass
        else:
            face_check()
            if not isChecked():
                SYSTEM = True
                video_status = False
                stop()
                print("System")
            else:
                indicator_red(False)
                
        if SYSTEM and video_status == False:
            indicator_red(True)
        ekg_fig.canvas.draw()
        emg_fig.canvas.draw()

    root.after(10, lambda:update())
  
  

