import PySimpleGUI as sg

def screensignin():
    look1=[
        [sg.T("User Name"),sg.I(key="-user-")],
        [sg.T("password"),sg.I(key="-pass-")],
        [sg.B("LOGIN")]
    ]
    return sg.Window("test",layout=look1,finalize=True)
def afterlogin():
    look2=[
        [sg.T("After Login")],
        [sg.B("Return")]
    ]
    return sg.Window("test",layout=look2,finalize=True)

screen1=screensignin()
screen2=None

while True:
    window,event,values=sg.read_all_windows()
    
    if event==sg.WIN_CLOSED:
        break
    if window==screen1 and event=="LOGIN":
        if values["-user-"]=="admin" and values["-pass-"]=="123456":
            screen2=afterlogin()
            screen1.hide()
        else:
            sg.popup("Wrong")
    if window==screen2 and event=="Return":
        screen1.un_hide()
        screen1["-user-"].update("")
        screen1["-pass-"].update("") #geri döndüğümüzde boş ekran versin diye,çünkü yazmadığımızda önceki yazdıklarımız duruyor oluyor
        screen2.hide()
window.close()