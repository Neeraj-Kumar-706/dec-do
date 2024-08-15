#good to go 

import tkinter as tk
from tkinter import ttk
 
 # main app
app=tk.Tk(className='converter')
app.geometry("400x400")
app.resizable(False,False)
# converter widget
label_1=ttk.Label(app,text='convert Gib to Mib',font=('verdana',20,'bold'))
label_1.pack(side='top')
#input frame which contains input box and a button
input_frame=ttk.Frame(app)
entry=ttk.Entry(input_frame)
button=ttk.Button(input_frame,text='convert')
input_frame.pack(side='top')
entry.pack(side='left')
button.pack(side='left')

#result wiget
result=ttk.Label(app,text='result',font=('verdana',20,'bold'))
result.pack(side='center')




app.mainloop()