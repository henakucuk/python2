import PySimpleGUI as sg 
import psutil

layout=[
    [sg.T("Cpu Sayisi:",size=(30,1)),sg.T("0",key="-cs-")],
    [sg.T("Cpu Kullanimi:",size=(30,1)),sg.T("0",key="-ck-")],
    [sg.T("RAM Miktari:",size=(30,1)),sg.T("0",key="-rm-")],
    [sg.T("RAM Kullanimi:",size=(30,1)),sg.T("0",key="-rk-")],
    [sg.T("WİFİ Durum:",size=(30,1)),sg.T("0",key="-wf-")],
    [sg.B("REFRESH"),sg.B("Exit")]
]

pen=sg.Window("DONANIM",layout)

while True:
    event,values = pen.read()
    if event in ("Exit",sg.WIN_CLOSED):
        break
    if event == "REFRESH":
        pen["-cs-"].update(psutil.cpu_count())
        pen["-ck-"].update(psutil.cpu_percent())
        pen["-rm-"].update(round(psutil.virtual_memory().total/(1024**3)))
        pen["-rk-"].update(psutil.virtual_memory().percent)
        pen["-wf-"].update(psutil.net_if_stats()["Wİ-Fİ"].isup)

pen.close()