from tkinter import *
from time import sleep


x_axis=800
y_axis=480
gifdir="./"

def update(ind):
    global after_id

    frame = frames[ind]
    ind += 1
    if ind > 45:
        ind = 0
    canvas_image = canvas1.create_image(x_axis/2, y_axis/2, image=frame)
    after_id= win.after(75, update, ind)

def back(event):
    aboutus.destroy()
    main()

def pic(event):

    global aboutus
    global after_id
    if after_id:
        win.after_cancel(after_id)
        after_id = None
    win.destroy()
    aboutus = Tk()
    aboutus.geometry('{}x{}'.format(x_axis, y_axis))
    aboutus.resizable(width=False, height=False)
    aboutus.configure(background="black")
    canvas2 = Canvas(aboutus, width=x_axis, height=y_axis)
    canvas2.configure(background="black")
    abt = PhotoImage(file=gifdir + "images/har.gif")
    canvas_image = canvas2.create_image(x_axis / 2, y_axis / 2, image=abt)
    # Label(canvas2,text="HAR",fg="white",bg="black",font=("Helvetica", 32)).pack()
    # Label(canvas2, text="HAR is an human assistant robot that uses Amazon voice services\n to interact with you . Alexa  will love to answer your questions ,\n manage your emails , play music for you and help you with internet searches.\n The robot uses computer vision to detect obstacles and it can follow you if you will\n ask him to do so . You can put your goods in it and even you can use it as a photobooth\n The robot can rontrol your home appliances and you can also control your appliances\n using this app.   ", fg="white", bg="black", font=("Helvetica", 16)).pack()
    canvas2.bind("<Button-1>", back)
    canvas2.pack()
    aboutus.config(cursor="none")
    aboutus.mainloop()


def main():
    global win,frames
    win = Tk()
    frames = [PhotoImage(file='./images/exp.gif', format='gif -index %i' % (i)) for i in range(50)]
    global canvas1
    win.geometry('{}x{}'.format(x_axis, y_axis))
    win.resizable(width=False, height=False)
    win.configure(background="black")

    igm = PhotoImage(file=gifdir+"images/exp.gif")

    canvas1 = Canvas(win,width=x_axis,height=y_axis)
    canvas1.configure(background="black")
    canvas1.bind("<Button-1>", pic)
    win.after(100, update, 0)
    canvas1.pack()
    win.config(cursor="none")
    win.mainloop()

main()