from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import numpy as np
import math

root=Tk()
root.geometry('1070x400+0+0')
root.configure(bg='light yellow')   # '#ccccff' is light violet, '#99ffff' is neon sky, "#b3ff66" is neon green, #ff9966 is brownish orange

#________________________creating frames_______________________________
main_frame=LabelFrame(root)
main_frame.grid(row=0,column=0,sticky='N')

frame_btn=Frame(main_frame)
frame_btn.pack()

frame_canvas=LabelFrame(main_frame, bg='violet')
frame_canvas.pack()


big_frame=LabelFrame(root,bg='light blue')
big_frame.grid(row=0, column=1)

frame=Frame(big_frame, bg='light blue')
frame.grid(row=0, column=2, rowspan=4)
#_______________________________graph plotting_______________________

def plot(x,y,label):
    global plot_btn
    global can_wid
    
    
    fig = Figure(figsize=(5, 3), dpi=100)
    axis = fig.add_subplot(111)
        
    
    t=axis.plot(x,y, label='Graph of '+label)
    axis.legend()
    
    canvas = FigureCanvasTkAgg(fig, master= frame_canvas)
    can_wid=canvas.get_tk_widget() 
    can_wid.pack()
    if can_wid.winfo_exists()==1:
            plot_btn.config(state='disabled')
    
            
def clear():
    can_wid.destroy()
    plot_btn.config(state='active')
    
    
#_____________________________mathematical functions__________________

def trig_graph(event):
    
    try:
        coeff_func=int(e1.get())
        coeff_x=int(e2.get())
        start=int(e3.get())
        end=int(e4.get())
        
        x=coeff_x*(np.arange(start, end,0.1))
        if var.get()=='sin':
            y=coeff_func*(np.sin(x))
        
        if var.get()=='cos':
            y=coeff_func*(np.cos(x))
        
        if var.get()=='tan':
            y=coeff_func*(np.tan(x))
        
        if var.get()=='cosec':
            y=coeff_func*(1/np.sin(x))
    
        if var.get()=='sec':
            y=coeff_func*(1/np.cos(x))
    
        if var.get()=='cot':
            y=coeff_func*(1/np.tan(x))
        
        plot_btn.configure(command=lambda: plot(x,y, e1.get()+var.get()+e2.get()+'x'))
    
    
    
    except:
        messagebox.showerror("showerror", "Enter values first")
    
    
    
def exp_graph(event):
    try:
        coeff_func=int(e1.get())
        coeff_x=int(e2.get())
        start=int(e3.get())
        end=int(e4.get())
            
        x=coeff_x*(np.arange(start, end,0.1))
            
        if var.get()=='e^x':
            y=coeff_func*(np.exp(x))
            plot_btn.configure(command=lambda: plot(x,y, str(coeff_func)+'e^'+str(coeff_x)+'x'))
        
        if var.get()=='ln x':
            y=coeff_func*(np.log(x))
            plot_btn.configure(command=lambda: plot(x,y, str(coeff_func)+'ln '+str(coeff_x)+'x'))
        
    
    except:
        messagebox.showerror("Error", "Enter values first")
        

def power_graph(event):
    try:
        coeff_func=int(e1.get())
        coeff_x=int(e2.get())
        start=int(e3.get())
        end=int(e4.get())
        a=int(e5.get())
        
        x=coeff_x*(np.arange(start, end,0.1))
        
        if var.get()=='a^x':
            y=coeff_func*(a**x)
        
        if var.get()=='log':
            y=coeff_func*(np.log10(x)/np.log10(a))
        plot_btn.configure(command=lambda: plot(x,y, e1.get()+var.get()+e2.get()+'x'))
    
    except:
        messagebox.showerror("Error", "Enter values first")
            
    
def linear_graph(event):
    try:
        constant=int(e1.get())
        coeff_x=int(e2.get())
        start=int(e3.get())
        end=int(e4.get())
        
        x=np.arange(start, end,0.1)
        y=coeff_x*x + constant
        
        plot_btn.configure(command=lambda: plot(x,y, e2.get()+'x+'+e1.get()))
        
    except:
        messagebox.showerror("showerror", "Enter values first")


def quadratic_graph(event):
    try:
        constant=int(e1.get())
        coeff_x=int(e2.get())
        coeff_xsq=int(e5.get())
        start=int(e3.get())
        end=int(e4.get())
            
        x=np.arange(start, end,0.1)
        y=coeff_xsq*(x**2)+ coeff_x*x + constant
        
        plot_btn.configure(command=lambda: plot(x,y, e5.get()+'x^2+'+e2.get()+'x+'+e1.get()))
    
    except:
        messagebox.showerror("showerror", "Enter values first")

    
        
            
#______________________________data functions______________________
#------------------------------------------------------------------

def create_frame():
    global frame
    frame=Frame(big_frame, bg='light blue')
    frame.grid(row=0, column=2, rowspan=6, padx=10)



def trigonometry():
    global var
    global e1
    global e2
    global e3
    global e4
    
    if frame.winfo_exists()==1:
        frame.destroy()
        create_frame()
        
    options=['sin','cos','tan','cosec','sec','cot']
    var=StringVar()
    var.set("Select function")
    
    menu=OptionMenu(frame, var, *options, command=trig_graph)
    menu.grid(row=8, column=0, pady=10)
 

    label1=Label(frame, text='Enter coefficient of function', font=10).grid(row=0,column=0,sticky='ew')
    e1=Entry(frame, width=5, font=10)
    e1.grid(row=1, column=0)
    
    label2=Label(frame, text='Enter coefficient of x', font=10).grid(row=2, column=0,sticky='ew')
    e2=Entry(frame, width=5, font=10)
    e2.grid(row=3, column=0)
    
    label3=Label(frame, text='Enter the range of x-axis',font=10).grid(row=4, column=0,sticky='ew')
    label4=Label(frame, text='From:',font=10).grid(row=5, column=0 ,sticky='ew', pady=5)
    
    e3=Entry(frame, width=4, font=10)
    e3.grid(row=5, column=1)
    
    label5=Label(frame, text='To:',font=10).grid(row=6, column=0,sticky='ew', pady=5)
    
    e4=Entry(frame, width=4, font=10)
    e4.grid(row=6, column=1)
    
    
    

    
def exponential():
    global var
    global e1
    global e2
    global e3
    global e4
    
    if frame.winfo_exists()==1:
        frame.destroy()
        create_frame()
    
    options=['e^x','ln x']
    var=StringVar()
    var.set("Select function")
    
    menu=OptionMenu(frame, var, *options, command=exp_graph)
    menu.grid(row=7, column=0, sticky='ew', pady=10)
    
    label1=Label(frame, text='Enter coefficient of function', font=10).grid(row=0,column=0,sticky='ew')
    e1=Entry(frame, width=5, font=10)
    e1.grid(row=1, column=0)
    
    label2=Label(frame, text='Enter coefficient of x', font=10).grid(row=2, column=0,sticky='ew')
    e2=Entry(frame, width=5, font=10)
    e2.grid(row=3, column=0)
    
    label3=Label(frame, text='Enter the range of x-axis',font=10).grid(row=4, column=0,sticky='ew')
    label4=Label(frame, text='From:',font=10).grid(row=5, column=0,sticky='ew',pady=5)
    
    e3=Entry(frame, width=4, font=10)
    e3.grid(row=5, column=1)
    
    label5=Label(frame, text='To:',font=10).grid(row=6, column=0,sticky='ew',pady=5)
    
    e4=Entry(frame, width=4, font=10)
    e4.grid(row=6, column=1)
    
    
def power():
    global var
    global e1
    global e2
    global e3
    global e4
    global e5
    
    if frame.winfo_exists()==1:
        frame.destroy()
        create_frame()
    
    options=['a^x','log']
    var=StringVar()
    var.set("Select function")
    
    menu=OptionMenu(frame, var, *options, command=power_graph)
    menu.grid(row=9, column=0,sticky='ew', pady=10)
    
    label1=Label(frame, text='Enter coefficient of function', font=10).grid(row=2,column=0,sticky='ew')
    e1=Entry(frame, width=5, font=10)
    e1.grid(row=3, column=0)
    
    label2=Label(frame, text='Enter coefficient of x', font=10).grid(row=4, column=0,sticky='ew')
    e2=Entry(frame, width=5, font=10)
    e2.grid(row=5, column=0)
    
    label3=Label(frame, text='Enter the range of x-axis',font=10).grid(row=6, column=0,sticky='ew')
    label4=Label(frame, text='From:',font=10).grid(row=7, column=0 ,sticky='ew',pady=5)
    
    e3=Entry(frame, width=4, font=10)
    e3.grid(row=7, column=1)
    
    label5=Label(frame, text='To:',font=10).grid(row=8, column=0,sticky='ew',pady=5)
    
    e4=Entry(frame, width=4, font=10)
    e4.grid(row=8, column=1)
    
    label6=Label(frame, text='Enter the value of a',font=10).grid(row=0, column=0,sticky='ew')
    
    e5=Entry(frame, width=5, font=10)
    e5.grid(row=1, column=0)
    
    
def linear():
    global e1
    global e2
    global e3
    global e4
    
    if frame.winfo_exists()==1:
        frame.destroy()
        create_frame()
    
    options=['y=ax+b']
    var=StringVar()
    var.set("Select function")
    
    menu=OptionMenu(frame, var, *options, command=linear_graph)
    menu.grid(row=8, column=0,sticky='ew', pady=10)
    
    
    label1=Label(frame, text='Enter constant value', font=10).grid(row=0,column=0,sticky='ew')
    e1=Entry(frame, width=5, font=10)
    e1.grid(row=1, column=0)
    
    label2=Label(frame, text='Enter coefficient of x', font=10).grid(row=2, column=0,sticky='ew')
    e2=Entry(frame, width=5, font=10)
    e2.grid(row=3, column=0)
    
    label3=Label(frame, text='Enter the range of x-axis',font=10).grid(row=4, column=0,sticky='ew')
    label4=Label(frame, text='From:',font=10).grid(row=5, column=0,sticky='ew',pady=5)
    
    e3=Entry(frame, width=4, font=10)
    e3.grid(row=5, column=1)
    
    label5=Label(frame, text='To:',font=10).grid(row=6, column=0,sticky='ew',pady=5)
    
    e4=Entry(frame, width=4, font=10)
    e4.grid(row=6, column=1)
    
    
 
    
def quadratic():
    global e1
    global e2
    global e3
    global e4
    global e5
    
    if frame.winfo_exists()==1:
        frame.destroy()
        create_frame()
    
    options=['y=ax^2+bx+c']
    var=StringVar()
    var.set("Select function")
    
    menu=OptionMenu(frame, var, *options, command=quadratic_graph)
    menu.grid(row=9, column=0, pady=10)
    
    
    label1=Label(frame, text='Enter constant value', font=10).grid(row=0,column=0,sticky='ew')
    e1=Entry(frame, width=5, font=10)
    e1.grid(row=1, column=0)
    
    label2=Label(frame, text='Enter coefficient of x', font=10).grid(row=2, column=0,sticky='ew')
    e2=Entry(frame, width=5, font=10)
    e2.grid(row=3, column=0)
    
    label6=Label(frame, text='Enter coefficient of x^2', font=10).grid(row=4, column=0,sticky='ew')
    e5=Entry(frame, width=5, font=10)
    e5.grid(row=5, column=0)
    
    label3=Label(frame, text='Enter the range of x-axis',font=10).grid(row=6, column=0,sticky='ew')
    label4=Label(frame, text='From:',font=10).grid(row=7, column=0 ,sticky='ew',pady=5)
    
    e3=Entry(frame, width=2, font=10)
    e3.grid(row=7, column=1)
    
    label5=Label(frame, text='To:',font=10).grid(row=8, column=0,sticky='ew',pady=5)
    
    e4=Entry(frame, width=2, font=10)
    e4.grid(row=8, column=1)
    
      
#-------------------------------buttons ---------------------------------------------    
                            
    
plot_btn=Button(frame_btn, text='PLOT',width=35, command=lambda: plot(0,0,''))
plot_btn.grid(row=0,column=0)
clr_btn=Button(frame_btn, text='CLEAR CANVAS',width=35,command=clear).grid(row=0,column=1)
#------------------------------main--------------------------------------------

v=StringVar()

Rd1=Radiobutton(big_frame, text='Trigonometrical functions', variable=v,value='1', 
                indicator=0,bg='pink',font=30, command=trigonometry)
Rd2=Radiobutton(big_frame, text='Exponential functions',  variable=v,value='2',
                indicator=0,bg='pink',font=30, command=exponential)
Rd3=Radiobutton(big_frame, text='Logarithmic functions',  variable=v,value='3',
                indicator=0,bg='pink',font=30, command=power)
Rd4=Radiobutton(big_frame, text='Linear functions',  variable=v,value='4',
             indicator=0,bg='pink',font=30, command=linear)
Rd5=Radiobutton(big_frame, text='Quadratic functions',  variable=v,value='5',
             indicator=0,bg='pink',font=30, command=quadratic)

    
Rd1.grid(row=0, column=0, sticky='ew')
Rd2.grid(row=1, column=0, sticky='ew', pady=20)
Rd3.grid(row=2, column=0, sticky='ew', pady=20)
Rd4.grid(row=3, column=0, sticky='ew', pady=20)
Rd5.grid(row=4, column=0, sticky='ew')


root.mainloop()







