import serial.tools.list_ports


ser: serial.Serial
port=''

def connect():
    global ser, port
    list = serial.tools.list_ports.comports()
    for p in list:
        if p.hwid.startswith("USB VID:PID=2341:0043"):
            try:
                port = p.name
                ser = serial.Serial(port, 115200)
                return True
            except:
                pass
    return False

def is_open():
    global ser, port
    list = serial.tools.list_ports.comports()
    for p in list: 
        if port == p.name and p.hwid.startswith("USB VID:PID=2341:0043"):
           return True
    return False

def data(ekg_mid,emg_mid):
    global ser
    try:
        result = ser.readline().decode()
        result = result.split()
    except:
        return None
    if result!=None:
        try:
            result_ekg = float(result[0])
        except:
            result_ekg = ekg_mid

        try:
            result_emg = float(result[1])
        except:
            result_emg = emg_mid

        return result_ekg, result_emg
    else:
        return None


def is_connected():
    j=10
    k=True
    m=True
    ekg=0
    emg=0
    for i in range (0,j):
        try:
            tmp=data(0,0)
         
            if tmp[0]>=48:
                ekg+=1
            if tmp[1]>=48 or tmp[1]<=2:
                emg+=1
        except:
            j+=1
    
    if ekg>5:
        k=False
    if emg>6:
        m=False   
    return k,m