from BaguetteEngine import *
import Model 

MAXSCORE = 10

app = Application.Application()
app.Client = None

app.Menu = True
app.InGame = False
app.CurrentGame = None

app.Owner = False

app.Score_L = 0
app.Score_R = 0

app.Time = Application.time.time()
app.lastTime = app.Time
app.timeD = (app.Time-app.lastTime)

class WindowAskIp(object):
    def __init__(self):
        self.ip = "0.0.0.0"
        self.default_ip = "0.0.0.0"
        self.lock = False

    def Show(self):
        self.lock = True
        self.screen = Application.tk.Tk()
        self.input = Application.tk.Entry(self.screen)
        self.input.pack()
        self.button = Application.tk.Button(self.screen,text="Ok",command = self.get_answer)
        self.button.pack()
        self.screen.update()

    def get_answer(self):
        answer = self.input.get()
        if len(answer.split(".")) != 4:
            self.ip = "0.0.0.0"
        else:
            self.ip = "0.0.0.0"
        self.screen.destroy()
        self.lock = False

app.WAI = WindowAskIp()

class Title(Application.Label):
    def update(self,app):
        if app.Menu:
            self.visible = True
        else:
            self.visible = False

class EndLabel(Application.Label):
    def start(self,app):
        self.visible = False

    def MakeMyThingSolo(self):
        app.canvas.delete("all")
        self.text = "Game over"
        self.visible = True
        app.drawn_element()
        app.screen.update()
        Application.time.sleep(2)
        app.canvas.delete("all")
        self.text = f"your score is {app.Score_L}"
        app.drawn_element()
        app.screen.update()
        self.visible = False
        Application.time.sleep(2)

class ScoreLeft(Application.Label):
    def update(self,app):
        if app.Menu:
            self.visible = False
        else:
            if app.CurrentGame == "Solo" or app.CurrentGame == "Local":
                if MoveCameraTo(app,[50,10,20]):
                    self.visible = True
                    self.text = f"Score : {app.Score_L}"

class ScoreRight(Application.Label):
    def update(self,app):
        if app.Menu:
            self.visible = False
        else:
            if app.CurrentGame == "Solo":
                self.visible = False
            elif app.CurrentGame == "Local":
                if MoveCameraTo(app,[50,10,20]):
                    self.visible = True
                    self.text = f"Score : {app.Score_R}"

class ButtonPlaySolo(Application.Button):
    def update(self,app):
        if app.Menu:
            self.visible = True
        else:
            self.visible = False

    def NotMouseOver(self,app):
        self.background_enable = False
        self.text_color = "white"
    
    def OnMouseOver(self,app):
        self.background_enable = True
        self.text_color = "Black"

    def OnClick(self,app):
        app.Menu = False
        app.CurrentGame = "Solo"

class ButtonPlayLocal(Application.Button):
    def update(self,app):
        if app.Menu:
            self.visible = True
        else:
            self.visible = False

    def NotMouseOver(self,app):
        self.background_enable = False
        self.text_color = "white"
    
    def OnMouseOver(self,app):
        self.background_enable = True
        self.text_color = "Black"

    def OnClick(self,app):
        try:
            app.WAI.Show()
            while app.WAI.lock:
                app.canvas.delete("all")
                app.Time = Application.time.time()
                app.timeD = (app.Time-app.lastTime)
                app.screen.update()
                app.drawn_element()
                app.lastTime = app.Time
            
            app.Client = ClientPonc(ip = app.WAI.ip)
            app.Client.run()
            app.Menu = False
            app.CurrentGame = "Local"
            app.Client.send("TOTAL_CLIENT")
            while not app.Client.VCN:
                pass
            print(app.Client.ClientNumber)
            if app.Client.ClientNumber > 2:
                print("party full")
                ee
            app.Client.VCN = False

            print("waiting for player")
            while app.Client.ClientNumber < 2:
                app.canvas.delete("all")
                app.Time = Application.time.time()
                app.timeD = (app.Time-app.lastTime)
                app.Client.send("TOTAL_CLIENT")
                while not app.Client.VCN:
                    pass
                app.Client.VCN = False
                app.screen.update()
                app.drawn_element()
                app.lastTime = app.Time

            print("the party can start")
        except:
            app.Menu = True
            print("server off line")

class ButtonStartServer(Application.Button):
    def update(self,app):
        if app.Menu:
            self.visible = True
        else:
            self.visible = False

    def NotMouseOver(self,app):
        self.background_enable = False
        self.text_color = "white"
    
    def OnMouseOver(self,app):
        self.background_enable = True
        self.text_color = "Black"

    def OnClick(self,app):
        try:
            app.ServerL = Server.Server(ip = "0.0.0.0")
            app.ServerL.start()
            app.Owner = True
        except:
            print("the ip is already use")

class Cup(Application.Model):
    def start(self,app):
        for voxel in self.model:
            voxel.north_enable = False
            voxel.east_enable = False
            voxel.west_enable = False
            voxel.top_enable = False
            voxel.bottom_enable = False

class PaddlePlayer(Application.Model):
    def start(self,app):
        for voxel in self.model:
            voxel.north_enable = False
            voxel.east_enable = False
            voxel.west_enable = False
            voxel.top_enable = False
            voxel.bottom_enable = False
    
    def update(self,app):
        if app.Menu == False:
            if app.CurrentGame == "Solo":
                if Application.keyboard.is_pressed('z'):
                    self.position[1]+=app.timeD*10
                if self.position[1] > 15:
                    self.position[1]=15
                
                if Application.keyboard.is_pressed('s'):
                    self.position[1]-=app.timeD*10
                if self.position[1] < 5:
                    self.position[1]=5

            if app.CurrentGame == "Local":
                if Application.keyboard.is_pressed('z'):
                    self.position[1]+=app.timeD*10
                if self.position[1] > 15:
                    self.position[1]=15
                
                if Application.keyboard.is_pressed('s'):
                    self.position[1]-=app.timeD*10
                if self.position[1] < 5:
                    self.position[1]=5
                app.Client.send("ne|"+str(self.position[1]))

class PaddleEnnemi(Application.Model):
    def start(self,app):
        for voxel in self.model:
            voxel.north_enable = False
            voxel.east_enable = False
            voxel.west_enable = False
            voxel.top_enable = False
            voxel.bottom_enable = False

    def update(self,app):
        if app.Menu == False:
            if app.CurrentGame == "Solo":
                self.visible = False
            if app.CurrentGame == "Local":
                self.visible = True
                self.position[1] = app.Client.EnnemiY

class Ball(Application.Model):
    def start(self,app):
        for voxel in self.model:
            voxel.north_enable = False
            voxel.east_enable = False
            voxel.west_enable = False
            voxel.top_enable = False
            voxel.bottom_enable = False
        self.speed = 2
        self.increase = 0.1
        self.A = 1
        self.B = Application.choice([-1,1])
        self.onPaddle = False

    def update(self,app):
        if app.Menu == False:
            if app.CurrentGame == "Solo":
                if MoveCameraTo(app,[50,10,20]):
                    self.position[0]-=self.speed*self.A*app.timeD
                    if self.position[0] <= 40.5 and self.position[0] >= 39.5 and self.position[1]>=Player.position[1]-1.5 and self.position[1]<=Player.position[1]+1.5:
                        self.A=-1
                        self.speed+=0.1
                        if not self.onPaddle:
                            app.Score_L += 1
                            self.onPaddle = True
                    else:
                        self.onPaddle = False
                    
                    if self.position[0] <= 60.5 and self.position[0] >= 59.5:
                        self.A=1
                        self.speed+=0.1
                        
                    if self.position[0]<=38:
                        self.position = [50,10,22.5]
                        self.speed = 2
                        self.increase = 0.1
                        self.A = 1
                        self.B = Application.choice([-1,1])
                        self.visible = False
                        app.EndTitle.MakeMyThingSolo()
                        self.visible = True
                        app.InGame=False
                        app.Menu = True
                        app.Score_L = 0
                        app.Score_R = 0
                        
                    self.position[1]-=self.speed*self.B*app.timeD
                    if self.position[1] >= 16:
                        self.B=1
                    if self.position[1] <= 4:
                        self.B=-1

            elif app.CurrentGame == "Local":
                if app.InGame:
                        if app.Owner:
                            self.position[0]-=self.speed*self.A*app.timeD
                            if self.position[0] <= 40.5 and self.position[0] >= 39.5 and self.position[1]>=Player.position[1]-1.5 and self.position[1]<=Player.position[1]+1.5:
                                self.A=-1
                                self.speed+=0.1
                                if not self.onPaddle:
                                    self.onPaddle = True
                            else:
                                self.onPaddle = False
                            
                            if self.position[0] <= 60.5 and self.position[0] >= 59.5 and self.position[1]>=Ennemi.position[1]-1.5 and self.position[1]<=Ennemi.position[1]+1.5:
                                self.A=1
                                self.speed+=0.1
                            
                            self.position[1]-=self.speed*self.B*app.timeD
                            if self.position[1] >= 16:
                                self.B=1
                            if self.position[1] <= 4:
                                self.B=-1

                            if self.position[0] < 38:
                                app.Score_R += 1
                                self.speed = 2
                                self.increase = 0.1
                                self.A = 1
                                self.B = Application.choice([-1,1])
                                self.position = [50,10,22.5]

                            if self.position[0] > 62:
                                app.Score_L += 1
                                self.speed = 2
                                self.increase = 0.1
                                self.A = 1
                                self.B = Application.choice([-1,1])
                                self.position = [50,10,22.5]

                            app.Client.send("bx|"+str(self.position[0]))
                            app.Client.send("by|"+str(self.position[1]))
                            app.Client.send("sl|"+str(app.Score_R))
                            app.Client.send("sr|"+str(app.Score_L))
                        else:
                            try:
                                x = 50 - float(app.Client.BallX)
                                x += 50
                                
                                self.position[0] = x
                                self.position[1] = float(app.Client.BallY)
                            except:
                                pass

class ClientPonc(Client.Client):
    def UpdateValue(self,lm):
        if lm[0] == "ne":
            self.EnnemiY = float(lm[1])
        if lm[0] == "sl":
            app.Score_L = int(lm[1])
        if lm[0] == "sr":
            app.Score_R = int(lm[1])
        if lm[0] == "bx":
            self.BallX = lm[1]
        if lm[0] == "by":
            self.BallY = lm[1]

    def start(self):
        self.EnnemiY = 0
        self.BallX = 0
        self.BallY = 0

def MoveCameraTo(app,position):
    if app.distance(position)>=0.2:
        x = (position[0]-app.camera[0])*app.timeD
        app.camera[0]+=x
        y = (position[1]-app.camera[1])*app.timeD
        app.camera[1]+=y
        z = (position[2]-app.camera[2])*app.timeD
        app.camera[2]+=z
        Ok = False
    else:
        Ok = True

    return Ok

Title(x=20,y=100,size=[400,120],text="Ponc",background_enable=False,text_color = "white",police_size = 35)
ButtonPlaySolo(x=120,y=240,size=[120,60],text="Solo",text_color="white",color_background="white")
ButtonPlayLocal(x=120,y=320,size=[120,60],text="Local",text_color="white",color_background="white")
ButtonStartServer(x=120,y=420,size=[320,60],text="Start server",text_color="white",color_background="white")
ScoreLeft(x=600,y=50,background_enable = False,text_color = "white")
ScoreRight(x=1000,y=50,background_enable = False,text_color = "white")
app.EndTitle = EndLabel(x=810,y=540,visible =False,background_enable = False,text_color = "white")

Cup(z=5,x=0,model=Model.cup)
Ball(x=50,y=10,z=22.5,model=Model.cube)
Player=PaddlePlayer(x=40,y=10,z=22.5,model=Model.paddle)
Ennemi = PaddleEnnemi(x=60,y=10,z=22.5,model=Model.paddle)

app.screen_distance=160

app.run()
while True:
    app.canvas.delete("all")
    app.Time = Application.time.time()
    app.timeD = (app.Time-app.lastTime)

    if not app.Menu:
        if app.CurrentGame == "Solo":
            if MoveCameraTo(app,[50,10,20]):
                app.InGame = True

        elif app.CurrentGame == "Local":
            if MoveCameraTo(app,[50,10,20]):
                if not app.InGame:
                    app.InGame = True
        
    else:
        MoveCameraTo(app,[0,0,0])
    
    app.Update()
    app.drawn_element()
    app.screen.update()
    app.lastTime = app.Time
