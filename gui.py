# this for front end of app as for gui frame work we wil use tkinter 
from tkinter import * 
main=Tk(className='dec-do')
main.geometry("500x500")
b=Button(main,text="click me")
b.pack(side='bottom')

mainloop()