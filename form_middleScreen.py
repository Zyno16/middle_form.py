import tkinter

form = tkinter.Tk()

w = 500
h = 300
sw = form.winfo_screenwidth()
sh = form.winfo_screenheight()
x = (sw -w) / 2
y = (sh - h) / 2

form.geometry(' %dx%d+%d+%d ' % ( w, h, x, y))


form.mainloop()
