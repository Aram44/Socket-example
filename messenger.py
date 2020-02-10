import socket, threading
from PySide import QtCore, QtGui
import sys
from ui import Ui_Form

app = QtGui.QApplication(sys.argv)
#host = socket.gethostbyname(socket.gethostname())
host = ''
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
ui.ipadr.setText(host)
ui.ipadr.setDisabled(1)
#client
shutdown = False
key = 4581
def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				ui.textBrowser.append("<p style=\"font-size:14px; padding: 0px; margin: 0px; color:#ffffff;\">"+decrypt+"</p>")
		except:
			pass
#host = socket.gethostbyname(socket.gethostname())
host = ''
port = 0
server = (host,9090)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()
#end
initk = True
def sendmsg():
        message = ui.msge.text()
        user = ui.names.text()
        ui.msge.setText("")
        global initk
        if initk:
        	ui.names.setDisabled(1)
        	ui.keys.setDisabled(1)
        	s.sendto(("["+user + "] -> join ").encode("utf-8"),server)
        	initk = False
        if message != "":
	        ui.textBrowser.append("<p style=\"font-size:14px; padding: 0px; margin: 0px; color:#ffffff;\">["+user+"] :: "+message+"</p>")
	        crypt = ""
	        for i in message:
	            crypt += chr(ord(i)^key)
	        message = crypt
	        if message != "":
	            s.sendto(("["+user + "] :: "+message).encode("utf-8"),server)
ui.sendbtn.clicked.connect(sendmsg)
sys.exit(app.exec_())
rT.join()
s.close()
