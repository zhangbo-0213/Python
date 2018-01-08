import Tkinter as tk
window=tk.Tk()
window.title('MajorTom')
window.geometry('400x400')
entry1=tk.Entry(window)
entry1.pack()
entry2=tk.Entry(window)
entry2.pack()

def hand():
    button.config(text='Yeah, you got it')

button=tk.Button(window,text='Try Click',command=hand)
button.pack()
window.mainloop()
