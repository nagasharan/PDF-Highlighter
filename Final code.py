from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from tkinter import messagebox


root=Tk()
"""creating the first page of the user interface"""
root.title("PDF highlighter")
# creating a label for first screen
myLabel = Label(root,text="Welcome to the pdf phrase highlighter\n click on next to continue", font=("Helvetica", 16))
myLabel1 = Label(root,text="            ")
myLabel.grid(row=0,column=1,padx=200,pady=200)
myLabel1.grid(row=0,column=0)
# creating a frame

frame1=LabelFrame(root,text="",padx=2,pady=2)
frame1.grid(row=1,column=2,pady=10,padx=10)

#adding a function
def page1():
	next_Button1.grid_forget()
	myLabel.grid_forget()
	myLabel1.grid_forget()
	frame1.grid_forget()
	global myLabel1_1
	global myLabel1_2
	global myLabel1_3
	global myLabel1_4
	global enterpdf
	global enterexcel
	global frame2
	global frame3
	global frame4
	global browse_Button1
	global browse_Button2
	global next_Button2
	# texts
	myLabel1_1 = Label(root,text="            ")
	myLabel1_2=Label(root,text="Please select or give file path for PDF file")
	myLabel1_1.grid(row=0,column=0,padx=200,pady=50)
	myLabel1_2.grid(row=1,column=0)

	myLabel1_3 = Label(root,text="            ")
	myLabel1_3.grid(row=3,column=0,padx=200,pady=50)

	myLabel1_4=Label(root,text="Please select or give file path for Excel file")
	myLabel1_4.grid(row=4,column=0)

	myLabel1_5 = Label(root,text="            ")
	myLabel1_5.grid(row=6,column=0,padx=200,pady=50)

	myLabel1_6 = Label(root,text="            ")
	myLabel1_6.grid(row=2,column=2,padx=25)

	#entry
	enterpdf=Entry(root,width=55,borderwidth=5)
	enterpdf.grid(row=2,column=0,columnspan=25,padx=10,pady=10)

	enterexcel=Entry(root,width=55,borderwidth=5)
	enterexcel.grid(row=5,column=0,columnspan=25,padx=10,pady=10)

	#adding frame
	frame2=LabelFrame(root,text="",padx=4,pady=4)
	frame2.grid(row=2,column=1,pady=4,padx=4)

	frame3=LabelFrame(root,text="",padx=4,pady=4)
	frame3.grid(row=5,column=1,pady=4,padx=4)

	frame4=LabelFrame(root,text="",padx=2,pady=2)
	frame4.grid(row=7,column=2,pady=2,padx=2)


	# adding functions
	
	def browse1():
		global name1
		root.filename = filedialog.askopenfilename(title="Select a file")
		name1=str(root.filename)
		enterpdf.insert(0,name1)

	def browse2():
		global name2
		root.filename = filedialog.askopenfilename(title="Select a file")
		name2=str(root.filename)
		enterexcel.insert(0,name2)


	def next2():
		try:
			output1=name1
			output2=name2 
			

		except:
			messagebox.showwarning("No file selected","Please select the file or provide file path")
		else:
			output1=name1
			output2=name2 
			myLabel1_1.grid_forget()
			myLabel1_2.grid_forget()
			myLabel1_3.grid_forget()
			myLabel1_4.grid_forget()
			myLabel1_5.grid_forget()
			myLabel1_6.grid_forget()
			enterpdf.grid_forget()
			enterexcel.grid_forget()
			frame2.grid_forget()
			frame3.grid_forget()
			frame4.grid_forget()
			browse_Button1.grid_forget()
			browse_Button2.grid_forget()
			next_Button2.grid_forget()
			myLabel19 = Label(root,text="PLEASE WAIT....", font=("Helvetica", 16))
			myLabel19.grid(row=0,column=1,padx=200,pady=200)


	# adding browse button
	browse_Button1 = Button(frame2, text="Browse",command=browse1)
	browse_Button1.grid(row=2,column=1,padx=2,pady=2)

	browse_Button2 = Button(frame3, text="Browse",command=browse2)
	browse_Button2.grid(row=5,column=1,padx=2,pady=2)

	next_Button2 = Button(frame4, text="Next",command=next2)
	next_Button2.grid(row=7,column=2,padx=2,pady=2)




# adding a next button

next_Button1 = Button(frame1, text="Next",command=page1)

next_Button1.grid(row=0,column=0)

root.mainloop()