from tkinter import *
 
PosX=60
PosY=10
PosX2=200
PosY2=480
dx=10
dy=7
score=0
 
def jouer():
    global menu
   
    def deplacement():
        global dx, dy, PosX2, PosY2, score
        if canvas.coords(balle)[1]<0:
            dy=-1*dy
        if canvas.coords(balle)[2]>500:
            dx=-1*dx
        if canvas.coords(balle)[0]<0:
            dx=-1*dx
        if canvas.coords(balle)[3]>=PosY2 and canvas.coords(balle)[2]>=canvas.coords(raquette)[0] and canvas.coords(balle)[0]<=canvas.coords(raquette)[2] and canvas.coords(balle)[3]<=490:
            dy=-1*dy
            score=score+1
            TextGame.set("Score : "+ str(score))
        if canvas.coords(balle)[3]<550:
            tk.after(10,deplacement)
        canvas.move(balle,dx,dy)
 
    def KeyBoard(event):
        global PosX2, menu
        Key = event.keysym
 
        if Key == 'Right':
            canvas.move(raquette,30,0)
        if Key == 'Left':
            canvas.move(raquette,-30,0)
   
    menu.destroy()#Detruire le menu pour utiliser le score
    tk = Tk()
    tk.title("[New Game]")
 
    canvas = Canvas(tk,width = 500, height = 500 , bd=0, bg="grey")
    canvas.pack(padx=10,pady=10)
 
    balle = canvas.create_oval(PosX,PosY,PosX+20,PosY+20,fill='white')
    raquette = canvas.create_rectangle(PosX2,PosY2,PosX2+100,PosY2+10,fill='black')
 
    TextGame = StringVar()
    LabelGame = Label(tk, textvariable = TextGame , bg ="grey")
    TextGame.set("Score : "+ str(score))
    LabelGame.pack(padx = 15, pady = 5)
 
    canvas.focus_set()
 
    canvas.bind('<Key>',KeyBoard)
 
    deplacement()
   
    tk.mainloop()
 

def start():
    global menu
    
    menu = Tk()
    menu.title("[Squash Pong]")
    menu.geometry("260x90")
     
    ButtonJouer = Button(menu, text ="   Play   ", command = jouer)
    ButtonJouer.pack(padx = 5, pady = 5)
     
    ButtonQuitter = Button(menu, text ="   Exit    ", command = menu.destroy)
    ButtonQuitter.pack(padx = 5, pady = 5)
     
    menu.mainloop()




if __name__ == '__main__':
    start()