from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from values import x_data, x2_data, y_data, y2_data, VIEW, VIEW2
from video import VideoPlayerApp

root=Tk()
FORM2 = False
ENROLL = False
PAUSE = 1

name=''
age=0

b_font = ('Arial', 18)

red_indicator = None
yellow_indicator = None
start_indicator = None
succes_indicator = None
fail_indicator = None

ekg_fig, (ax1) = plt.subplots(figsize=[3.5,2.5])
emg_fig, (ax2) = plt.subplots(figsize=[3.5,2.5])

line, = ax1.plot(x_data, y_data)

ax1.set_title("График ЭКГ")
ax1.set_xlim(0, VIEW)
ax1.set_ylim(0, 50)
ax1.set_xlabel("Время(с)")
ax1.set_ylabel("Напряжение(мВ)")

line2, = ax2.plot(x2_data, y2_data)

ax2.set_title("График ЭМГ")
ax2.set_xlim(0, VIEW2)
ax2.set_ylim(0, 50)
ax2.set_xlabel("Время(с)")
ax2.set_ylabel("Напряжение(мВ)")

def pause(event):
    global PAUSE
    PAUSE*=-1

root.bind("p", pause)

def getPause():
    global PAUSE
    return PAUSE

def start():
    global root, button, inst_1_2, inst_2_2, inst_3_2, FORM2, ekg_text, emg_text, info_t, dop_block, graphik_block
    
    root.title("modul B")

    root.geometry("1200x720+100+0")

    header = ttk.Frame(root, borderwidth=1, relief=SOLID, width=1200, height=120)
    header.grid(row=0, column=0, sticky=EW)
    header.grid_propagate(False)

    s_font = ('Arial', 14)
    b_font = ('Arial', 16)
    s_font_b = ('Arial', 14, 'bold')

    for a in range (0,3): header.columnconfigure(index=a, weight=1)
    for a in range (0,1): header.rowconfigure(index=a, weight=1)

    inf = ttk.Label(header, text="Информация о разработчике", font = s_font, anchor=CENTER, relief=SOLID)
    inf.grid(column=0, columnspan=3, row=0, sticky=NSEW)
    inf_college = ttk.Label(header, text="Институт среднего\nпрофессионального\nобразования Петра Великого", font = s_font, anchor=CENTER, relief=SOLID)
    inf_college.grid(column=0, row=1, sticky=NSEW)
    inf_name = ttk.Label(header, text="Производственная практика", font = s_font, anchor=CENTER, relief=SOLID)
    inf_name.grid(column=1, row=1, sticky=NSEW)
    inf_dev = ttk.Label(header, text="Малюк Дарья Антоновна", font = s_font, anchor=CENTER, relief=SOLID)
    inf_dev.grid(column=2, row=1, sticky=NSEW)
    inf_user = ttk.Label(header, text="", font = s_font, anchor=CENTER, relief=SOLID, width=30)
    inf_user.grid(column=3, row=0, sticky=NSEW)


    main_frame = ttk.Frame(root, borderwidth=1, relief=SOLID)
    main_frame.grid(sticky=NSEW)
    for a in range (0,1): main_frame.columnconfigure(index=a, weight=1)



    graphik_block = ttk.Frame(main_frame, borderwidth=1, relief=SOLID)
    graphik_block.grid(row=0, column=0)
    for a in range (0,1): main_frame.rowconfigure(index=a, weight=1)
    for a in range (0,2): main_frame.columnconfigure(index=a, weight=1)

    ekg_block = ttk.Frame(graphik_block, borderwidth=1, relief=SOLID)
    ekg_block.grid(row=0, column=0, sticky=NSEW, ipady=10)
    canvas = FigureCanvasTkAgg(ekg_fig, ekg_block)
    canvas.get_tk_widget().pack(padx=20, pady=(10,20))
    canvas.draw()

    ekg_text = ttk.Label(ekg_block, text="Мин.значение:\nСред.значение:\nМаксюзначение:")
    ekg_text.pack()

    emg_block = ttk.Frame(graphik_block, borderwidth=1, relief=SOLID)
    emg_block.grid(row=0, column=1, sticky=NSEW)
    canvas2 = FigureCanvasTkAgg(emg_fig, emg_block)
    canvas2.get_tk_widget().pack(padx=20, pady=(10,20))
    canvas2.draw()

    emg_text = ttk.Label(emg_block, text="Мин.значение:\nСред.значение:\nМаксюзначение:")
    emg_text.pack()

    info_block = ttk.Frame(graphik_block, borderwidth=1, relief=SOLID)
    info_block.grid(row=1, column=0, columnspan=2, sticky=NSEW)

    info_b_text = ttk.Label(info_block, text="Информационный блок", font=s_font, anchor=CENTER)
    info_b_text.pack(pady=(10,0))
    info_b_frame = ttk.Frame(info_block, borderwidth=1, relief=SOLID, height=200, width=500)
    info_b_frame.pack(pady=20)

    info_t = ttk.Label(info_b_frame, text="", font=s_font, anchor=CENTER)
    info_t.pack(pady=(10,0))
    info_b_frame.grid_propagate(False)
    info_b_frame.pack_propagate(False)

    dop_block = ttk.Frame(graphik_block, borderwidth=1, width=420)
    dop_block.grid(row=0,column=2, rowspan=2, sticky=NSEW)
    dop_block.grid_propagate(False)
    dop_block.pack_propagate(False)

    inst=ttk.Label(dop_block, text = "Инструкция", font = b_font, anchor=CENTER)
    inst.pack(pady=(0,10))

    inst_1=ttk.Label(dop_block, text = "1.Автоматическое определение COM-порта", font = b_font, anchor=W)
    inst_1.pack(anchor=W, padx=(10,0), pady=(0,10))
    inst_1_2=ttk.Label(dop_block, text = "Определен", font = b_font, anchor=CENTER,foreground='red')
    inst_1_2.pack(pady=(0,10))

    inst_2=ttk.Label(dop_block, text = "2.Подключите электроды ЭКГ", font = b_font, anchor=W)
    inst_2.pack(anchor=W, padx=(10,0), pady=(0,10))
    inst_2_2=ttk.Label(dop_block, text = "Подключено", font = b_font, anchor=CENTER,foreground='red')
    inst_2_2.pack(pady=(0,10))


    inst_3=ttk.Label(dop_block, text = "3.Подключите электроды ЭМГ", font = b_font, anchor=W)
    inst_3.pack(anchor=W, padx=(10,0), pady=(0,10))
    inst_3_2=ttk.Label(dop_block, text = "Подключено", font = b_font, anchor=CENTER,foreground='red')
    inst_3_2.pack(pady=(0,10))
# ACTIVEEEEEEEEEEEEE
# ACTIVEEEEEEEEEEEEE
# ACTIVEEEEEEEEEEEEE
# ACTIVEEEEEEEEEEEEE
    def next():
        global FORM2, dop_block
        FORM2=True
        dop_block = ttk.Frame(graphik_block, borderwidth=1, width=420)
        dop_block.grid(row=0,column=2, rowspan=2, sticky=NSEW)

        inf_user.config(text="Информация о операторе")
        enter_user = ttk.Frame(header, borderwidth=0, relief=SOLID)
        enter_user.grid(column=3, row=1, sticky=NSEW)

        name_l = ttk.Label(enter_user, text = "ФИО", font = b_font)
        name_l.grid( row=0, column=0)
        name_e=ttk.Entry(enter_user)
        name_e.grid(row=0, column=1)

        age_l = ttk.Label(enter_user, text = "Возраст", font = b_font)
        age_l.grid(row=1, column=0)
        age_e=ttk.Entry(enter_user)
        age_e.grid(row=1, column=1)

        enroll_text = ttk.Label(enter_user, text = "", font = b_font, foreground="red")
        enroll_text.grid(row=2, column=0)

        def enroll():
            global name, age, ENROLL
            if age_e.get() == '' or name_e.get()== '':
                enroll_text.config(text="error")
            else:
                name = name_e.get()
                try:
                    age = int(age_e.get())
                    ENROLL = TRUE
                    enroll_text.config(text="")
                except:
                    enroll_text.config(text="error")

        enroll_b = ttk.Button(enter_user,command=enroll, text="Записать")
        enroll_b.grid(row=2, column=2)
    next()



def video_block():
    global dop_block, graphik_block, v_frame
    dop_block = ttk.Frame(graphik_block, borderwidth=1, width=420)
    dop_block.grid(row=0,column=2, rowspan=2, sticky=NSEW)
    dop_block.pack_propagate(False)
    v_label = ttk.Label(dop_block, text="Видео блок", font=('Arial',14))
    v_label.pack(anchor=CENTER)
    v_frame = VideoPlayerApp(dop_block,"test.mp4", 360, 230)
    v_frame.frame_update()



def button_state(state):
    global button
    if button.winfo_exists():
        if state:
            button.config(state=ACTIVE)
        else:
            button.config(state=DISABLED)

def com_text(state):
    global inst_1_2
    if inst_1_2.winfo_exists():
        if state:
            inst_1_2.config(foreground="green")
        else:
            inst_1_2.config(foreground="red")

def ekg_text(state):
    global inst_2_2
    if inst_2_2.winfo_exists():
        if state:
            inst_2_2.config(foreground="green")
        else:
            inst_2_2.config(foreground="red")

def emg_text(state):
    global inst_3_2
    if inst_3_2.winfo_exists():
        if state:
            inst_3_2.config(foreground="green")
        else:
            inst_3_2.config(foreground="red")

def getForm2():
    global FORM2
    return FORM2

def getEnroll():
    global ENROLL
    return ENROLL

def emg_write(fist, emg_min, emg_mid, emg_max):
    global emg_text
    emg_text.config(text="Сжатия:"+str(fist) + "\nМин.значение:"+str(emg_min)+"\nСред.значение:"+str(emg_mid)+"\nМакс.значение:"+str(emg_max))

def ekg_write(pulse, ekg_min, ekg_mid, ekg_max):
    global ekg_text
    ekg_text.config(text="Пульс:"+str(pulse) + "\nМин.значение:"+str(ekg_min)+"\nСред.значение:"+str(ekg_mid)+"\nМакс.значение:"+str(ekg_max))

def status(pulse):
    global info_t
    if pulse>100:
        info_t.config(text="Пульс выходит за пределы нормы")
    elif pulse <60:
        info_t.config(text="Пульс отсутствует")
    else:
        info_t.config(text="Пульс в норме")

def research():
    global info_t
    # info_t.config(text="Исследование завершено - переход к подключению\nблока видео")

def indicator_red(state):
    global red_indicator
    if red_indicator is not None:
        if not state:
            red_indicator.destroy()
            red_indicator=None
    else:
        if state:
            red_indicator=ttk.Label(root, text="Засыпание оператора", font=b_font, background='red', foreground='white', anchor=CENTER)
            red_indicator.place(relx=0.5, rely=0.5, anchor=CENTER, height=150, width=1200)

def indicator_yellow(state):
    global yellow_indicator
    if yellow_indicator is not None:
        if not state:
            yellow_indicator.destroy()
            yellow_indicator=None
    else:
        if state:
            yellow_indicator=ttk.Label(root, text="Превышение пульса", font=b_font, background='yellow', foreground='white', anchor=CENTER)
            yellow_indicator.place(relx=0.5, rely=0.5, anchor=CENTER, height=100, width=1200)

def indicator_start(state):
    global start_indicator
    if start_indicator is not None:
        if not state:
            start_indicator.destroy()
            start_indicator=None
    else:
        if state:
            start_indicator=ttk.Label(root, text="Распознавание лица", font=b_font, background='yellow', foreground='white', anchor=CENTER)
            start_indicator.place(relx=0.5, rely=0.5, anchor=CENTER, height=100, width=1200)

def indicator_succes(state):
    global succes_indicator
    if succes_indicator is not None:
        if not state:
            succes_indicator.destroy()
            succes_indicator=None
    else:
        if state:
            succes_indicator=ttk.Label(root, text="Лицо распознано", font=b_font, background='green', foreground='white', anchor=CENTER)
            succes_indicator.place(relx=0.5, rely=0.5, anchor=CENTER, height=100, width=1200)

def indicator_fail(state):
    global fail_indicator
    if fail_indicator is not None:
        if not state:
            fail_indicator.destroy()
            fail_indicator=None
    else:
        if state:
            fail_indicator=ttk.Label(root, text="Лицо не распознано", font=b_font, background='red', foreground='white', anchor=CENTER)
            fail_indicator.place(relx=0.5, rely=0.5, anchor=CENTER, height=100, width=1200)

def play():
    global v_frame
    v_frame.play()

def stop():
    global v_frame
    v_frame.stop()