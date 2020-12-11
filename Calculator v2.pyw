from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Calculator GUI")
root.iconbitmap('icon.ico')
root.config(bg='#1F1F1F')
root.geometry('322x390')
root.resizable(False, False)
myFont = Font(family="Bahnschrift SemiBold", size=14)
enterFont = Font(family="Bahnschrift SemiBold", size=35)

def button_click(number):

        if enter.get() == '0':
                enter.delete(0, END)
        current = enter.get()
        enter.delete(0, END)
        enter.insert(0, current + number)

def button_calc(calculation):

	global num1
	num1 = enter.get()
	global calc
	calc = calculation
	enter.delete(0, END)

def button_equal():

	global num1
	global calc
	if calc=="+":
		answer = int(num1)+ int(enter.get())
	if calc=="-":
		answer = int(num1)- int(enter.get())
	if calc=="*":
		answer = int(num1)* int(enter.get())
	if calc=="/":
		answer = int(num1)/ int(enter.get())
	if calc=="power":
		answer = int(num1)** int(enter.get())
	if calc=="root":
		answer=int(num1)**(1./int(enter.get()))

	enter.delete(0, END)
	enter.insert(0, answer)

def button_clear():

        enter.delete(0, END)

def button_bs():

        txt = enter.get()[:-1]
        enter.delete(0, END)
        enter.insert(0, txt)

enter = Entry(root, width=12, borderwidth=0, font=enterFont, bg='#1F1F1F', fg='white', justify=RIGHT, insertbackground='white')
enter.grid(row=0, column=0, columnspan=3, padx=0, pady=10)

def button_on_enter(e):
        if e.widget in [button_percent, button_clear, button_bs, button_add, button_minus, button_multiply, button_divide, button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0, button_root, button_power]:
                e.widget['background'] = '#4D4D4D'
        if e.widget == button_equal:
                e.widget['background'] = '#1f7ac4'
def button_on_leave(e):
        if e.widget in [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0, button_root, button_power]:
                e.widget['background'] = '#060606'
        if e.widget in [button_percent, button_clear, button_bs, button_add, button_minus, button_multiply, button_divide]:
                e.widget['background'] = '#131313'
        if e.widget == button_equal:
                e.widget['background'] = '#134369'
        
button_root = Button(root, borderwidth=0, fg='white', text="√", width=6, height=1, pady=5.7, font=myFont, bg="#060606", relief=FLAT, padx=3)
button_0 = Button(root, borderwidth=0, text="0", width=6, height=1, pady=5.7, command=lambda: button_click("0"), font=myFont, bg="#060606", fg='white', relief=FLAT, padx=3)
button_power = Button(root, borderwidth=0, text='square',fg='white', relief=FLAT, width=6, height=1, pady=5.8, command=lambda: button_calc("power"), font=myFont, bg="#060606", padx=3)
button_equal = Button(root, borderwidth=0, text="=", width=6, height=1, pady=5.8, command=button_equal, font=myFont, bg="#134369", fg='white', relief=FLAT, padx=3)

button_1 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF', text="1", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("1"), font=myFont, bg="#060606", fg='white', relief=FLAT)
button_2 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="2", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("2"), font=myFont, bg="#060606", fg='white', relief=FLAT)
button_3 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="3", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("3"), font=myFont, bg="#060606", fg='white', relief=FLAT)

button_4 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="4", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("4"), font=myFont, bg="#060606", fg='white', relief=FLAT)
button_5 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="5", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("5"), font=myFont, bg="#060606", fg='white', relief=FLAT)
button_6 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="6", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("6"), font=myFont, bg="#060606", fg='white', relief=FLAT)

button_7 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="7", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("7"), font=myFont, bg="#060606", fg='white', relief=FLAT)
button_8 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="8", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("8"), font=myFont, bg="#060606", fg='white', relief=FLAT)
button_9 = Button(root, borderwidth=0, activebackground='#4D4D4D', activeforeground='#FFFFFF',text="9", width=6, height=1, pady=5.7, padx=3, command=lambda: button_click("9"), font=myFont, bg="#060606", fg='white', relief=FLAT)

button_add = Button(root, text="+", relief=FLAT, width=6, height=1, pady=4, command=lambda: button_calc("+"), font=myFont, bg="#131313", fg='white')
button_minus = Button(root, text="-", width=6, height=1, pady=4, relief=FLAT, fg='white', command=lambda: button_calc("-"), font=myFont, bg="#131313")
button_multiply = Button(root, text="×", width=6, relief=FLAT, fg='white', height=1, pady=4, command=lambda: button_calc("*"), font=myFont, bg="#131313")

button_divide = Button(root, text="÷", width=6, relief=FLAT, fg='white', height=1, pady=5.7, command=lambda: button_calc("/"), font=myFont, bg="#131313")
button_percent = Button(root, text="%", width=6, relief=FLAT, fg='white', height=1, pady=5.7, command=lambda: button_calc("%"), font=myFont, bg="#131313")
button_clear = Button(root, text="CE", width=6, relief=FLAT, fg='white', height=1, pady=5.7, command=button_clear, font=myFont, bg="#131313")
button_bs = Button(root, text="⌫", width=6, relief=FLAT, fg='white', height=1, pady=5.7, command=button_bs, font=myFont, bg="#131313")

button_root.place(x=5, y=338)
button_0.place(x=84, y=338)
button_power.place(x=163, y=338)
button_equal.place(x=242, y=338)

button_1.place(x=5, y=289)
button_2.place(x=84, y=289)
button_3.place(x=163, y=289)
button_add.place(x=242, y=289)

button_4.place(x=5, y=240)
button_5.place(x=84, y=240)
button_6.place(x=163, y=240)
button_minus.place(x=242, y=240)

button_7.place(x=5, y=191)
button_8.place(x=84, y=191)
button_9.place(x=163, y=191)
button_multiply.place(x=242, y=191)

button_divide.place(x=242, y=138)
button_percent.place(x=163, y=138)
button_clear.place(x=84, y=138)
button_bs.place(x=5, y=138)

root.bind('<Enter>', button_on_enter)
root.bind('<Leave>', button_on_leave)

while True:
        if enter.get() == '':
                enter.insert(END, '0')
        root.update()
