from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(bg="#17161b")
root.resizable(False,False)

e = Entry(root,width=45,borderwidth=3)

expression = ''
result=''
def button_click(item):
    global expression 
    expression += str(item)
    label.config(text=expression)
def clear():
    global expression 
    expression = ''
    label.config(text=expression)
def calculate():
    global expression
    result = eval(expression)
    label.config(text=result)


label = Label(root,width=20,height=2,text="",fg="#fff",bg="#17161b")
label.grid(row=0,column=1,columnspan=4)
button1 = Button(root,text="1",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(1))
button2 = Button(root,text="2",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(2))
button3 = Button(root,text="3",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(3))
button4 = Button(root,text="4",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(4))
button5 = Button(root,text="5",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(5))
button6 = Button(root,text="6",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(6))
button7 = Button(root,text="7",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(7))
button8 = Button(root,text="8",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(8))
button9 = Button(root,text="9",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(9))
button0 = Button(root,text="0",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(0))

button_plus =  Button(root,text="+",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click('+'))
button_sub =   Button(root,text="-",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click('-'))
button_mul =   Button(root,text="*",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click('*'))
button_div =   Button(root,text="/",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click('/'))
button_equal = Button(root,text="=",padx=30,pady=15,fg="#fff",bg="#fe9037",command=lambda: calculate())
button_clear = Button(root,text="clear",padx=58,pady=15,fg="#fff",bg="#3697f5",command=lambda: clear())
button_dot =   Button(root,text=".",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click('.'))
button_lb =    Button(root,text="(",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click('('))
button_rb =    Button(root,text=")",padx=30,pady=15,fg="#fff",bg="#2a2d36",command=lambda: button_click(')'))

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_plus.grid(row=1,column=3)

button_lb.grid(row=4,column=0)
button0.grid(row=4,column=1)
button_rb.grid(row=4,column=2)
button_div.grid(row=4,column=3)

button_clear.grid(row=5,column=0,columnspan=2)
button_dot.grid(row=5,column=2)
button_equal.grid(row=5,column=3)


root.mainloop()