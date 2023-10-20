# Imports libs 
import tkinter as tk

#========================================== Window config
window = tk.Tk()
window.geometry("750x480")
window.title('Macro Keyboard GUI')

#========================================== Creates Frame
content = tk.Frame(window) 
#========================================== Creates BTN 

content.grid(column = 0, row = 0)

btn1 = tk.Button(content, text = "BT1")
btn1.grid(column = 0, row = 0)
btn2 = tk.Button(content, text = "BT2")
btn2.grid(column = 1, row = 0)
btn3 = tk.Button(content, text = "BT3")
btn3.grid(column = 2, row = 0)

btn4 = tk.Button(content, text = "BT4")
btn4.grid(column = 0, row = 1)
btn5 = tk.Button(content, text = "BT5")
btn5.grid(column = 1, row = 1)
btn6 = tk.Button(content, text = "BT6")
btn6.grid(column = 2, row = 1)

btn7 = tk.Button(content, text = "BT7")
btn7.grid(column = 0, row = 3)
btn8 = tk.Button(content, text = "BT8")
btn8.grid(column = 1, row = 3)
btn9 = tk.Button(content, text = "BT9")
btn9.grid(column = 2, row = 3)


# main loop
window.mainloop()