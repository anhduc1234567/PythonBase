import tkinter
from tkinter import ttk
from tkinter.ttk import Style

min = 400
max = 400

root = tkinter.Tk()
root.title('Heloo')
root.geometry(f'{min}x{max}')
root.maxsize(width=800,height=1000)
# root.configure(background='yellow')
frame = ttk.Frame(root,padding=10)
frame.configure(borderwidth=5)
frame.grid()
frame.place(anchor=tkinter.CENTER, rely=0.5, relx=0.5)


button = ttk.Button(frame,text='Thoát',command=root.destroy)
# button.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
button.grid(row=0,column=0)

button2 = ttk.Button(frame,text='Exit',command=root.destroy)
# button2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
button2.grid(row=2,column=0)
label_hello = ttk.Label(frame, text='Hello World!', font=('Arial', 24), foreground='yellow')
label_hello.grid(row=1,column=0)
root.mainloop()
