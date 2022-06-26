from tkinter import *

root = Tk()

root.title("Simple calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#e.insert(0, "Enter your name:")
def button_click(number):
	#e.delete(0,END)
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def button_clear():
	e.delete(0,END)


def button_add():
	first_number=e.get()
	global f_num
	global operation
	operation="add" 
	f_num=float(first_number)
	e.delete(0,END)

def button_mul():
	first_number=e.get()
	global f_num
	global operation
	operation="mul" 
	f_num=float(first_number)
	e.delete(0,END)

def button_sub():
	first_number=e.get()
	global f_num
	global operation
	operation="sub" 
	f_num=float(first_number)
	e.delete(0,END)

def button_div():
	first_number=e.get()
	global f_num
	global operation
	operation="div" 
	f_num=float(first_number)
	e.delete(0,END)

def button_equal():
	
	sec_num=e.get()
	e.delete(0,END)
	global s_num
	s_num=sec_num
	if operation=="add":
		total=f_num+float(s_num)
	if operation=="sub":	
		total=f_num-float(s_num)
	if operation=="mul":	
		total=f_num*float(s_num)
	if operation=="div":	
		total=f_num/float(s_num)

	e.insert(0,str(total))


button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
add_button=Button(root,text="+",padx=39,pady=20,command=lambda: button_add())
equal_button=Button(root,text="=",padx=39,pady=20,command=lambda: button_equal())
clear_button=Button(root,text="clear",padx=31,pady=20,command=lambda: button_clear())

sub_button=Button(root,text="-",padx=39,pady=20,command=lambda: button_sub())
mul_button=Button(root,text="*",padx=39,pady=20,command=lambda: button_mul())
div_button=Button(root,text="/",padx=39,pady=20,command=lambda: button_div())

#put buttons on the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=1)
add_button.grid(row=1,column=3)
equal_button.grid(row=4,column=2)
clear_button.grid(row=4,column=0)
sub_button.grid(row=2,column=3)
mul_button.grid(row=3,column=3)
div_button.grid(row=4,column=3)


root.mainloop()