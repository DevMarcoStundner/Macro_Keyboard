# Imports libs 
import tkinter as tk


# Consts
ROW1 = 0
ROW2 = 1
ROW3 = 2
BTIPADY = 20
BTPADX = 5
BTPADY = 5

#========================================== Window config
window = tk.Tk()
window.geometry("750x480")
window.title('Macro Keyboard GUI')

#========================================== Frames
btn_frm = tk.Frame(master = window)
btn_frm.pack()

#========================================== Creats BTN and sorts it in a grid

btn_frm.grid(row = ROW1, column = 0, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn1 = tk.Button(master = btn_frm, text = "BT1")
btn1.pack()

btn_frm.grid(row = ROW1, column = 1, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn2 = tk.Button(master = btn_frm, text = "BT2")
btn2.pack()

btn_frm.grid(row = ROW1, column = 2, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn3 = tk.Button(master = btn_frm, text = "BT3")
btn3.pack()

btn_frm.grid(row = ROW2, column = 0, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn4 = tk.Button(master = btn_frm, text = "BT4")
btn4.pack()

btn_frm.grid(row = ROW2, column = 1, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn5 = tk.Button(master = btn_frm, text = "BT5")
btn5.pack()

btn_frm.grid(row = ROW2, column = 2, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn6 = tk.Button(master = btn_frm, text = "BT6")
btn6.pack()

btn_frm.grid(row = ROW3, column = 0, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn7 = tk.Button(master = btn_frm, text = "BT7")
btn7.pack()

btn_frm.grid(row = ROW3, column = 1, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn8 = tk.Button(master = btn_frm, text = "BT8")
btn8.pack()

btn_frm.grid(row = ROW3, column = 2, ipady = BTIPADY, padx = BTPADX, pady = BTPADY)
btn9 = tk.Button(master = btn_frm, text = "BT9")
btn9.pack()



# main loop
window.mainloop()