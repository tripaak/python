from tkinter import *



root = Tk()  # start

root.geometry("600x400")
root.minsize(300,200)
root.maxsize(1200,800)

photo = PhotoImage(file="up.gif")
my_label = Label(root,text="Akash TripTthiiiii" ,image=photo)
my_label.pack()


root.mainloop() # end 