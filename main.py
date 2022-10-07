import tkinter

window = tkinter.Tk()
window.title("Trivia Game")
window.minsize(height=400, width=500)
window.resizable(False, False)

question_box = tkinter.Label(window, text='hi', background='red')
question_box.grid(columnspan=2)

button1 = tkinter.Button(window, text='Button1')
button2 = tkinter.Button(window, text='button2')
button3 = tkinter.Button(window, text='button3')
button4 = tkinter.Button(window, text='button4')
button1.grid(row=1, column=0, padx=20, pady=20)
button2.grid(row=1, column = 1, padx=20, pady=20)
button3.grid(row=2, column=0, padx=20, pady=20)
button4.grid(row=2, column=1, padx=20, pady=20)
window.mainloop()