import qrcode
from tkinter import *
from tkinter import messagebox

def reset():
	webEntry.delete(0,END)
	webEntry.config(bg='white')
	QR.config(image='',text='',width=20,height=20)

def QRCode():
	website = webEntry.get()
	try:
		website = webEntry.split('.')
		if website.startswith('www.') or website.endswith('.com'):
			filename = web[1]+'.jpg'
		else:
			filename = web[0]+'.jpg'
	except:
		filename=website

	if len(website)<1:
		messagebox.showwarning('Warning,Enter your website name first')
		webEntry.config(bg='red')
		QR.config(text='there is an error occured in generating QR code',fg='red')
	else:
		img = qrcode.make(website)
		img.save(filename)
		root.photo = PhotoImage(file=filename)
		QR.config(image=root.photo,text='QRCode Generated Successfully', fg='green', compound=TOP,width=300,height=300)
		messagebox.showinfo('Saved','QRCode Saved as " ' +filename+' " Successfull')

# GUI Dessign
root=Tk()
root.title('QR Code Generator')
root.config(bg='Black')
root.geometry('500x550')
root.resizable(0,0)
try:
	root.wm_iconbitmap('cc.ico')
except:
	pass
appName = Label(root,text='QRCode Generator',bg='black',fg='blue',font=('forte',25,'underline','bold','italic'))
appName.pack(side=TOP,fill=BOTH)
website=Label(root,text="Enter website name:",font=('impact',10))
website.place(x=10,y=70)
webEntry = Entry(root,fg='blue',bd=3,width=40)
webEntry.place(x=170,y=72)
getQRCode = Button(root,text="Get QR Code",bg='green',fg='white',activebackground='Green',width=30,activeforeground='yellow',command=QRCode)
getQRCode.place(x=180,y=100)
resetApp = Button(root,text='Reset',bg='black',fg='white',width=15,bd=3,command=reset)
resetApp.place(x=230,y=130)
QR=Label(root,image='',bg='black')
QR.place(x=100,y=170)
copyri8 = Label(root, text="App Developed: Harshad",bg='blue',fg='red',font=('arial',15,'bold')).pack(side=BOTTOM)
root.mainloop()