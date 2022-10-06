import tkinter

window = tkinter.Tk()
window.title("Trivia Game")
window.minsize(height=400, width=500)
window.resizable(False, False)

question_box = tkinter.Label(window, text='hi')
question_box.pack()

button1 = tkinter.Button(window, text='Button1')
button2 = tkinter.Button(window, text='button2')
button3 = tkinter.Button(window, text='button3')
button4 = tkinter.Button(window, text='button4')
button1.pack()
button2.pack()
button3.pack()
button4.pack()
window.mainloop()