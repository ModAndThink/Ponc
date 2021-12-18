from Library.BaguetteEngine import Application

MAXSCORE = 10

app = Application.Application()
app.Time = Application.time.time()
app.lastTime = app.Time
app.timeD = (app.Time-app.lastTime)
class TitleScreen(Application.Label):
    def update(self,app):
        if app.InGame:
            self.visible = False
        else:
            self.visible = True

class RightScore(Application.Label):
    def update(self,app):
        if app.CanPlay:
            self.visible = True
            self.text = f"ball lost : {app.R}"
        else:
            self.visible = False

class LeftScore(Application.Label):
    def update(self,app):
        if app.CanPlay:
            self.visible = True
            self.text = f"ball lost : {app.L}"
        else:
            self.visible = False

class ButtonPlay(Application.Button):
    def update(self,app):
        if app.InGame:
            self.visible = False
        else:
            self.visible = True
    def OnClick(self,app):
        app.R=0
        app.L=0
        app.InGame = True

class ButtonReturn(Application.Button):
    def Show(self,app):
        self.visible=True
        app.CanPlay=False
    def OnClick(self,app):
        app.InGame=False
        self.visible=False

class Terrain(Application.Model):
    def update(self,app):
        if app.InGame:
            self.visible = True
        else:
            self.visible = False

class PaddlePB(Application.Model):
    def NewGame(self):
        self.position[1]=0
    def start(self,app):
        for i in self.model:
            i.north_enable=False
            i.east_enable=False
            i.west_enable=False
            i.top_enable=False
            i.bottom_enable=False
    def update(self,app):
        if app.CanPlay:
            if Application.keyboard.is_pressed('up_arrow'):
                self.position[1]+=8*app.timeD
                if self.position[1]>=8:
                    self.position[1]=8
            elif Application.keyboard.is_pressed('down_arrow'):
                self.position[1]-=8*app.timeD
                if self.position[1]<=-8:
                    self.position[1]=-8

class PaddlePA(Application.Model):
    def NewGame(self):
        self.position[1]=0
    def start(self,app):
        for i in self.model:
            i.north_enable=False
            i.east_enable=False
            i.west_enable=False
            i.top_enable=False
            i.bottom_enable=False
    def update(self,app):
        if app.CanPlay:
            if Application.keyboard.is_pressed('z'):
                self.position[1]+=8*app.timeD
                if self.position[1]>=8:
                    self.position[1]=8
            elif Application.keyboard.is_pressed('s'):
                self.position[1]-=8*app.timeD
                if self.position[1]<=-8:
                    self.position[1]=-8

class Ball(Application.Model):
    def start(self,app):
        for i in self.model:
            i.north_enable=False
            i.east_enable=False
            i.west_enable=False
            i.top_enable=False
            i.bottom_enable=False
        self.nx=Application.choice([-1,1])
        self.ny=Application.choice([-1,1])
        self.speed = 1

    def update(self,app):
        try:
            '''if not app.CanPlay:
                del self'''
            if self.enable:
                if app.CanPlay:
                    if app.R==MAXSCORE or app.L==MAXSCORE:
                        self.enable=False
                    self.position[0]-=self.nx*app.timeD*self.speed
                    self.position[1]-=self.ny*app.timeD*self.speed
                    if self.position[1]<=-9:
                        self.ny=-1
                    if self.position[1]>=9:
                        self.ny=1

                    if self.position[0]<42:
                        app.L+=1
                        self.visible=False
                        self.enable = False
                    
                    if self.position[0]>=42 and self.position[0]<=44 and self.position[1]<=app.PPB.position[1]+1 and self.position[1]>=app.PPB.position[1]-1:
                        self.nx=-1
                        self.speed+=0.1
                    
                    if self.position[0]>78:
                        app.R+=1
                        self.visible=False
                        self.enable = False
                        
                    if self.position[0]>=76 and self.position[0]<=78 and self.position[1]<=app.PPA.position[1]+1 and self.position[1]>=app.PPA.position[1]-1:
                        self.nx=1
                        self.speed+=0.1
        except:
            for i in self.model:
                i.north_enable=False
                i.east_enable=False
                i.west_enable=False
                i.top_enable=False
                i.bottom_enable=False
            self.nx=1
            self.ny=Application.choice([-1,1])
            self.speed = 1

def MoveCameraTo(app,position):
    app.Time = Application.time.time()
    x = (position[0]-app.camera[0])*app.timeD
    app.camera[0]+=x
    y = (position[1]-app.camera[1])*app.timeD
    app.camera[1]+=y
    z = (position[2]-app.camera[2])*app.timeD
    app.camera[2]+=z
    app.timeD = (app.Time-app.lastTime)
    app.lastTime = app.Time
TitleScreen(x=10,y=100,size=[400,100],police_size=35,text_color="#ffdf00",text="title title title")
ButtonPlay(x=10,y=250,size=[300,100],police_size=30,text_color="#ffdf00",text="Play")

app.InGame = False

app.screen_distance = 160
model_paddle = [Application.Voxel(x=0,y=0,voxel_type = "model",color="#e9e9e9"),Application.Voxel(x=0,y=-1,voxel_type = "model",color="#e9e9e9"),
                Application.Voxel(x=0,y=1,color="#e9e9e9",voxel_type = "model")]
model_coupe = []

for x in range(-1,2):
    for z in range(-1,2):
        model_coupe.append(Application.Voxel(x=x,z=z,y=-3,voxel_type = "model",color="#e9e9e9"))

for y in range(-2,1):
    model_coupe.append(Application.Voxel(x=0,z=0,y=y,voxel_type = "model",color="#0075eb"))

for z in range(-1,2):
    for x in range(-1,2):
        model_coupe.append(Application.Voxel(x=x,z=z,y=1,voxel_type = "model",color="#e2e31e"))

for x in range(-1,2):
    for y in range(2,4):
        model_coupe.append(Application.Voxel(x=x,z=-2,y=y,voxel_type = "model",color="#e2e31e"))

for x in range(-1,2):
    for y in range(2,4):
        model_coupe.append(Application.Voxel(x=x,z=2,y=y,voxel_type = "model",color="#e2e31e"))

for z in range(-1,2):
    for y in range(2,4):
        model_coupe.append(Application.Voxel(x=2,z=z,y=y,voxel_type = "model",color="#e2e31e"))

for z in range(-1,2):
    for y in range(2,4):
        model_coupe.append(Application.Voxel(x=-2,z=z,y=y,voxel_type = "model",color="#e2e31e"))

model_terrain= []
for i in range(-17,17):
    model_terrain.append(Application.Voxel(x=i,y=10,voxel_type = "model"))

for i in range(-17,17):
    model_terrain.append(Application.Voxel(x=i,y=-10,voxel_type = "model"))

for i in range(-10,11):
    model_terrain.append(Application.Voxel(x=-18,y=i,voxel_type = "model"))

for i in range(-10,11):
    model_terrain.append(Application.Voxel(x=17,y=i,voxel_type = "model"))


#Terrain(model=model_terrain,x=60,z=15)
app.PPB=PaddlePA(model=model_paddle,x=43,y=0,z=15)
app.PPA=PaddlePB(model=model_paddle,x=77,y=0,z=15)
Application.Model(z=8,model=model_coupe)
app.CanPlay = False
Ball(model=[Application.Voxel(x=0,z=0,voxel_type = "model")],x=60,z=15)
LeftScore(background_enable = False,text_color="white",x=300,y=10,size=[300,100],police_size=30)
RightScore(background_enable = False,text_color="white",x=1200,y=10,size=[300,100],police_size=30)
app.L=0
app.R=0
app.BR = ButtonReturn(size=[440,100],police_size=30,x=640,y=540,text="Return to menu",text_color="black",visible=False)

app.run()
while True:
    app.canvas.delete("all")
    app.Time = Application.time.time()
    app.timeD = (app.Time-app.lastTime)
    if not app.InGame and app.distance([0,0,0])>0.4:
        app.PPB.NewGame()
        app.PPA.NewGame()
        MoveCameraTo(app,[0,0,0])
    if app.InGame and app.distance([60,0,10])>0.4:
        MoveCameraTo(app,[60,0,10])
    if app.InGame and app.distance([60,0,10])<=0.4:
        if app.L != MAXSCORE or app.R != MAXSCORE: 
            app.CanPlay = True
    if app.CanPlay:
        if app.L == MAXSCORE:
            app.BR.Show(app)
        if app.R == MAXSCORE:
            app.BR.Show(app)
        if Application.randint(0,1000)==233:
            Ball(model=[Application.Voxel(x=0,z=0,voxel_type = "model")],x=60,z=15)
    app.Update()
    app.drawn_element()
    app.screen.update()
    app.lastTime = app.Time
