from tkinter import *

class Pong(Frame):
    player1 = 0
    player2 = 0
    ballX=50
    ballY=50
    ball = 0
    paddle1 = 0
    paddle2 = 0
    paddle1X = 2
    paddle1Y = 2
    paddle2X = 0
    paddle2Y = 2
    canvas = 0
    ballDX = 2
    ballDY = -2
    winHEIGHT = 0;
    winWIDTH = 0;
    paddleSpeed = 15
    player1Points = 0
    player2Points = 0
    textLabel = 0
    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()

    def key(self, event):
        global player1,player2
        print ("pressed", repr(event.char))
        if event.char == 'z':
            if self.canvas.coords(self.paddle1)[1]>=0:
                self.canvas.move(self.paddle1,0,-self.paddleSpeed)
        if event.char == 's':
            if self.canvas.coords(self.paddle1)[3]<=self.winHEIGHT:
                self.canvas.move(self.paddle1,0,self.paddleSpeed)
        if event.char == 'o':
            if self.canvas.coords(self.paddle2)[1]>=0:
                self.canvas.move(self.paddle2,0,-self.paddleSpeed)
        if event.char == 'l':
            if self.canvas.coords(self.paddle2)[3]<=self.winHEIGHT:
                self.canvas.move(self.paddle2,0,self.paddleSpeed)
        if event.char == 'q':
            self.parent.destroy()

    def callback(self, event):
        self.focus_set()
        print ("clicked at", event.x, event.y)

    def motion(self, event):
        coords1 = self.canvas.coords(self.paddle1)
        height1 = coords1[3]-coords1[1]
        coords1[1] = event.y
        coords1[3] = event.y+height1
        self.canvas.coords(self.paddle1,coords1[0],coords1[1],coords1[2],coords1[3])
        
    def initUI(self):

        self.paddle2X = self.parent.winfo_screenwidth() - 15
        self.parent.title("Pong")        
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

        self.winHEIGHT = self.parent.winfo_screenheight()
        self.winWIDTH = self.parent.winfo_screenwidth()

        self.ball = self.canvas.create_oval(0+self.ballX, 0+self.ballY, 10+self.ballX, 10+self.ballY, outline="black", 
            fill="red", width=1)
        self.paddle1 = self.canvas.create_rectangle(0+self.paddle1X, 0+self.paddle1Y, 10+self.paddle1X, 50+self.paddle1Y, outline="black", fill="black")
        self.paddle2 = self.canvas.create_rectangle(0+self.paddle2X, 0+self.paddle2Y, 10+self.paddle2X, 50++self.paddle2Y, outline="black", fill="black")
        self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
        
        self.parent.bind("<Key>", self.key)
        self.parent.bind("<Button-1>", self.callback)
        self.parent.bind("<Motion>", self.motion)
        
        self.canvas.pack(fill=BOTH, expand=1)
        self.after(200, self.doMove)
        

    def doCollide(self,coords1,coords2):
        height1 = coords1[3]-coords1[1]
        width1 = coords1[2]-coords1[0]
        height2 = coords2[3]-coords2[1]
        width2 = coords2[2]-coords2[0]
        return not (coords1[0] + width1 < coords2[0] or coords1[1] + height1 < coords2[1] or coords1[0] > coords2[0] + width2 or coords1[1] > coords2[1] + height2)

    def doMove(self):
        self.canvas.move(self.ball,self.ballDX, self.ballDY)
        if self.canvas.coords(self.ball)[1] <= 0:
            self.ballDY = -self.ballDY
        if self.canvas.coords(self.ball)[3] >= self.winHEIGHT:
            self.ballDY = -self.ballDY
        if self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle1)) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle2)):
            self.ballDX = -self.ballDX
        if self.canvas.coords(self.ball)[0] <= 0:
            self.ballDX = -self.ballDX
            self.player2Points+=1
            self.canvas.delete(self.textLabel)
            self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
            self.canvas.coords(self.ball,self.winWIDTH/2,self.winHEIGHT/2,self.winWIDTH/2+10,self.winHEIGHT/2+10)
        if self.canvas.coords(self.ball)[2] >= self.winWIDTH:
            self.ballDX = -self.ballDX
            self.player1Points+=1
            self.canvas.delete(self.textLabel)
            self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
            self.canvas.coords(self.ball,self.winWIDTH/2,self.winHEIGHT/2,self.winWIDTH/2+10,self.winHEIGHT/2+10)
        self.after(10, self.doMove)

def main():
  
    root = Tk()
    ex = Pong(root)
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()  


if __name__ == '__main__':
    main()  