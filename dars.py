from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont , QColor
from PyQt5.QtCore import Qt
 



app = QApplication([])
oyna = QWidget()
oyna.setStyleSheet("""
    background-color: rgb(0,0,0)                   
""")

input = QLineEdit(oyna)
input.setStyleSheet("""
    QLineEdit{
        border-radius: 15px;
        font-size: 30px;
        border: 2px solid black;
        background-color: rgb(0, 0, 0);
        color: white;
    }
""")
input.setAlignment(Qt.AlignRight)
input.setGeometry(10, 25,360,90)
oyna.setWindowTitle("Calculator")
oyna.move(1200,200)
oyna.setFixedSize(460,590)
nolga=QLabel("nolga bolmidi", oyna)



def birBosildi():
    txt = input.text() + "1"
    input.setText(txt)
    
def ikkiBosildi():
    txt = input.text() + "2"
    input.setText(txt)

def uchBosildi():
    txt = input.text() + "3"
    input.setText(txt)
    
def tortBosildi():
    txt = input.text() + "4"
    input.setText(txt)

def beshBosildi():
    txt = input.text() + "5"
    input.setText(txt)

def oltiBosildi():
    txt = input.text() + "6"
    input.setText(txt)
    
def yettiBosildi():
    txt = input.text() + "7"
    input.setText(txt)

def sakkizBosildi():
    txt = input.text() + "8"
    input.setText(txt)

def toqqizBosildi():
    txt = input.text() + "9"
    input.setText(txt)

def nolBosildi():
    txt = input.text() + "0"
    input.setText(txt)

def musbat_manfiy():
    txt = -1* int(input.text())
    input.setText(str(txt))


def plusBosildi():
    txt = input.text()
    if txt[-1] == "+":
        return
    if txt[-1] in ["-", "*", "/"]:
        txt = txt[:-1]
    input.setText(txt + "+")


def minus():
    txt = input.text()
    if txt[-1]=="-":
        return 
    if txt[-1]in ["+", "*", "/"]:
        txt=txt[:-1]
    input.setText(txt + "-")

def kopaytir():
    txt = input.text()
    if txt[-1]=="*":
        return 
    if txt[-1]in ["+", "-", "/"]:
        txt=txt[:-1]
    input.setText(txt + "*")

def bol():
    txt = input.text()
    if txt[-1]=="/":
        return 
    if txt[-1]in ["+", "*", "-"]:
        txt=txt[:-1]
    input.setText(txt + "/")



def tengla():
    
    txt=input.text()
    if txt:
        try:
            natija=str(eval(txt))
        except ZeroDivisionError:
            input.setText("nolga bolinmaydi")
            tozala()
        except Exception:
            input.setText("Biron belgi qolib ketdi")
        else:
            input.setText(natija)        
    

def rQavsBosildi():
    txt = input.text() + ")"
    input.setText(txt)

def nuqta():
    txt=input.text()
    if txt[-1].isalnum():
        txt+="."
    else :
        return 
    input.setText(txt)
def lQavsBosildi():
    txt = input.text() + "("
    input.setText(txt)

def tozala():
    txt=input.text()
    txt=""
    input.setText(txt)

def daraja():
    txt=input.text()
    m=str(eval(txt)**2)
    input.setText(str(m))

def ildiz():
    txt=input.text()
    m=str(eval(txt)**0.5)
    input.setText(str(m))
    
def ochir():
    txt=input.text()
    txt=txt[:-1]
    input.setText(txt)    


tenglik = QPushButton("=", oyna)
tenglik.setGeometry(370, 410, 80, 80)
tenglik.setStyleSheet("""
    QPushButton{
        color: white;
        background-color: rgb(255, 153, 51);
        font-size: 25px;
        border-radius: 40px;
        border: 2px solid black;
    }
""")
tenglik.clicked.connect(tengla)


raqam_1=QPushButton(oyna)
raqam_1.setText("1")
raqam_1.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77, 77, 77)
    }
""")
raqam_1.setGeometry(10, 140, 80, 80)
raqam_1.clicked.connect(birBosildi)



raqam_2=QPushButton(oyna)
raqam_2.setText("2")
raqam_2.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77, 77, 77)
    }
          
""")

raqam_2.setGeometry(100, 140, 80, 80)
raqam_2.clicked.connect(ikkiBosildi)


raqam_3=QPushButton(oyna)
raqam_3.setText("3")
raqam_3.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77, 77, 77)
    }
""")
raqam_3.setGeometry(190, 140, 80, 80) 
raqam_3.clicked.connect(uchBosildi)


raqam_4=QPushButton(oyna)
raqam_4.setText("4")
raqam_4.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77, 77, 77)
    }                  
""")
raqam_4.setGeometry(10, 230, 80, 80)
raqam_4.clicked.connect(tortBosildi)

raqam_5=QPushButton(oyna)
raqam_5.setText("5")
raqam_5.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77, 77, 77)
    }                    
""")
raqam_5.setGeometry(100, 230, 80, 80)
raqam_5.clicked.connect(beshBosildi)

raqam_6=QPushButton(oyna)
raqam_6.setText("6")
raqam_6.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77,77,77);
    }                
""")
raqam_6.setGeometry(190, 230, 80, 80) 
raqam_6.clicked.connect(oltiBosildi)


raqam_7=QPushButton(oyna)
raqam_7.setText("7")
raqam_7.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77,77,77);
    }           
""")
raqam_7.setGeometry(10, 320, 80, 80)
raqam_7.clicked.connect(yettiBosildi)


raqam_8=QPushButton(oyna)
raqam_8.setText("8")
raqam_8.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77,77,77);
    }                      
""")
raqam_8.setGeometry(100, 320, 80, 80)
raqam_8.clicked.connect(sakkizBosildi)

raqam_9=QPushButton(oyna)
raqam_9.setText("9")
raqam_9.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77,77,77);
    } 
""")
raqam_9.setGeometry(190, 320, 80, 80) 
raqam_9.clicked.connect(toqqizBosildi)


raqam_0=QPushButton(oyna)
raqam_0.setText("0")
raqam_0.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77,77,77);
    }                      
""")
raqam_0.setGeometry(100, 410, 80, 80)
raqam_0.clicked.connect(nolBosildi)


raqam_musbat_manfiy=QPushButton(oyna)
raqam_musbat_manfiy.setText("+/-")
raqam_musbat_manfiy.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        font-size:25px;
        color: white;
        background-color: rgb(77, 77, 77)
        
    }                                  
""")
raqam_musbat_manfiy.setGeometry(10, 410, 80, 80)
raqam_musbat_manfiy.clicked.connect(musbat_manfiy)


raqam_nuqta=QPushButton(oyna)
raqam_nuqta.setText(".")
raqam_nuqta.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        color: white;
        font-size: 25px;
        border: 2px solid black;
        background-color: rgb(77,77,77);
    }  
""")
raqam_nuqta.setGeometry(190, 410, 80, 80) 
raqam_nuqta.clicked.connect(nuqta)


amal_qoshuv=QPushButton(oyna)
amal_qoshuv.setText("+")
amal_qoshuv.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        border: 2px solid black;
        font-size: 30px;
        background-color: rgb(255, 153, 51);
        color: white;
    }
""")
amal_qoshuv.setGeometry(280, 140, 80, 80)
amal_qoshuv.clicked.connect(plusBosildi)

amal_ayiruv=QPushButton(oyna)
amal_ayiruv.setText("-")
amal_ayiruv.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        border: 2px solid black;
        font-size: 30px;
        background-color: rgb(255, 153, 51);
        color: white;
    }
""")
amal_ayiruv.setGeometry(280, 230, 80, 80)
amal_ayiruv.clicked.connect(minus)


amal_kopaytruv=QPushButton(oyna)
amal_kopaytruv.setText("*")
amal_kopaytruv.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        border: 2px solid black;
        font-size: 25px;
        background-color: rgb(255, 153, 51);
        color: white;
    }
""")
amal_kopaytruv.setGeometry(280, 320, 80, 80)
amal_kopaytruv.clicked.connect(kopaytir)


amal_boluv=QPushButton(oyna)
amal_boluv.setText("/")
amal_boluv.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        border: 2px solid black;
        font-size: 25px;
        background-color: rgb(255, 153, 51);
        color: white;
    }
""")
amal_boluv.setGeometry(280, 410, 80, 80)
amal_boluv.clicked.connect(bol)

left_qavs=QPushButton("(", oyna)
left_qavs.setGeometry(370, 140, 80, 80)
left_qavs.setStyleSheet("""
    QPushButton{
        border-radius: 40px;
        border: 2px black solid;
        background-color: rgb(255, 153, 51);
        color: white;
        font-size: 25px;
    }
""")
left_qavs.clicked.connect(lQavsBosildi)

right_qavs=QPushButton(")", oyna)
right_qavs.setGeometry(370, 230, 80, 80)
right_qavs.setStyleSheet("""
    QPushButton{
        border: 2px solid black;
        border-radius: 40px;
        color: white;
        font-size: 25px;
        background-color: rgb(255, 153, 51)
    }
""")
right_qavs.clicked.connect(rQavsBosildi)

clear=QPushButton("AC", oyna)
clear.setGeometry(370, 320, 80, 80)
clear.setStyleSheet("""
    QPushButton{
        color: white;
        border-radius: 40px;
        border: 2px;
        font-size:20px;
        background-color: rgb(255, 153, 51)
    }
""")
clear.clicked.connect(tozala)


kvadrat=QPushButton("kv", oyna)
kvadrat.setGeometry(10, 500, 80, 80)
kvadrat.setStyleSheet("""
    QPushButton{
        color: white;
        border-radius: 40px;
        border: 2px solid black;
        font-size: 20px;
        background-color: rgb(255, 153, 51);
    }♣
""")
kvadrat.clicked.connect(daraja)

tag=QPushButton("V2", oyna)
tag.setGeometry(100, 500, 80, 80)
tag.setStyleSheet("""
    QPushButton{
        color: white;
        border-radius: 40px;
        border: 2px solid black;
        font-size: 20px;
        background-color: rgb(255, 153, 51);
    }♣
""")
tag.clicked.connect(ildiz)

backspace=QPushButton("backspace", oyna)
backspace.setGeometry(190, 500, 140, 80)
backspace.setStyleSheet("""
    QPushButton{
        color: white;
        border-radius: 10px;
        border: 2px solid black;
        font-size: 20px;
        background-color: rgb(255, 153, 51);
    }♣
""")
backspace.clicked.connect(ochir)

oyna.show()
app.exec()


