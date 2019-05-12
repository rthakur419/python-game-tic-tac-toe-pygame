import pygame
from pygame.locals import *
pygame.init()
width=420
height=360
screen = pygame.display.set_mode((width,height))
title=pygame.display.set_caption("Tic Tac Toe")
player1= [False,False,False,False,False]
player2= [False,False,False,False,False]
start = False
p1=False
p2=False
time_since_enter=0
p1win=False
p1wincount=0
p2wincount=0
p2win=False
draw=False
start_time=False
start_time1=None
start_time2=0
startingscreen=False
endingscreen=False
time_since_enter=0
p=0
clicks =[]

rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
frameb=pygame.image.load("frame.png")
frameb=pygame.transform.scale(frameb,(201,10))
frameh=pygame.transform.scale(frameb,(10,200))
font = pygame.font.SysFont("comicsans", 80)
fontwin = pygame.font.SysFont("comicsans", 30)
p1w=fontwin.render("Player1", 1, (0,0,0))
p2w=fontwin.render("Player2", 1, (0,0,0))
restart=font.render("Restart", 1, (0,200,0))
title = font.render("Tic Tac Toe", 1, (0,200,0))
join = font.render("Press Enter!", 1, (0, 128, 0))
player1win=font.render("Player1 Wins", 1, (192,1,192))
player2win=font.render("Player2 Wins", 1, (192,1,192))
draww=font.render("Draw", 1, (192,1,192))
clock=pygame.time.Clock()
LEFT =1
end=False
class frame():
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self,screen):
        screen.blit(frameb,(self.x+10,self.y))
        screen.blit(frameb,(self.x+10,self.y-70))
        screen.blit(frameh,(self.x+70,self.y-130))
        screen.blit(frameh,(self.x+140,self.y-130))
class cross():
    cross=pygame.image.load("tick.png")
    cross=pygame.transform.scale(cross,(60,60))
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self,screen):
        self.rect=(self.x,self.y,60,60)
        screen.blit(self.cross,(self.x,self.y))
        pygame.draw.rect(screen,(0,0,0),(self.rect),2)
class circle(cross):
    circle=pygame.image.load("circle.png")
    circle=pygame.transform.scale(circle,(60,60))               
    def draw(self,screen):
        self.rect=(self.x,self.y,60,60)
        screen.blit(self.circle,(self.x,self.y))
        pygame.draw.rect(screen,(0,0,0),(self.rect),2)
def redraw():
    screen.fill((0,150,0))
    pt1=180
    pt2=180
    if start_time:
        time_since_enter1 = pygame.time.get_ticks() - start_time1
        time_since_enter2 = pygame.time.get_ticks() - start_time2
        if(p1):
            pt1-=time_since_enter1/1200
        timer1 = str(int(pt1//60)) + ":" + str(int(pt1%60))
        if int(pt1%60) < 10:
            timer1 = timer1[:-1] + "0" + timer1[-1]
        #screen.blit(fontwin.render(timer1, 1, (0,0,0)), (5, 27))
        if(p2):
             pt2-=time_since_enter1/1200
        timer2 = str(int(pt2//60)) + ":" + str(int(pt2%60))
        if int(pt2%60) < 10:
            timer2 = timer2[:-1] + "0" + timer2[-1]
        #screen.blit(fontwin.render(timer2, 1, (0,0,0)), (width-45,27))
    if (endingscreen):
        screen.blit(restart, (width/2 - restart.get_width()/2, 100))
        screen.blit(join, (width/2 - join.get_width() / 2, 200))
    if not(startingscreen):
        screen.blit(title, (width/2 - title.get_width()/2, 100))
        screen.blit(join, (width/2 - join.get_width() / 2, 200))
    if(start):
        fr.draw(screen)
        screen.blit(p1w,(5,5))
        if(p1):
            pygame.draw.rect(screen,(150,0,0),(3,3,p1w.get_width()+3,p1w.get_height()+3),2)
        #screen.blit(fontwin.render(str(p1wincount), 1, (255,0,0)),(5,44))
        screen.blit(p2w,((width-p2w.get_width())-5,5))
        if(p2):
            pygame.draw.rect(screen,(0,150,150),((width-p2w.get_width())-8,3,p1w.get_width()+7,p1w.get_height()+3),2)
        #screen.blit(fontwin.render(str(p2wincount), 1, (0,180,180)),(width-45,44))
    if (player1[0]):
        if(rect[0])and not(rect[9]):
            cro1.draw(screen)
        if(rect[1])and not(rect[10]):
            cro2.draw(screen)
        if(rect[2])and not(rect[11]):
            cro3.draw(screen)
        if(rect[3])and not(rect[12]):
            cro4.draw(screen)
        if(rect[4])and not(rect[13]):
            cro5.draw(screen)
        if(rect[5])and not(rect[14]):
            cro6.draw(screen)
        if(rect[6])and not(rect[15]):
            cro7.draw(screen)
        if(rect[7])and not(rect[16]):
            cro8.draw(screen)
        if(rect[8])and not(rect[17]):
            cro9.draw(screen)
    if(player2[0]):
        if(rect[9])and not(rect[0]):
            cir1.draw(screen)
        if(rect[10])and not(rect[1]):
            cir2.draw(screen)
        if(rect[11])and not(rect[2]):
            cir3.draw(screen)
        if(rect[12])and not(rect[3]):
            cir4.draw(screen)
        if(rect[13])and not(rect[4]):
            cir5.draw(screen)
        if(rect[14])and not(rect[5]):
            cir6.draw(screen)
        if(rect[15])and not(rect[6]):
            cir7.draw(screen)
        if(rect[16])and not(rect[7]):
            cir8.draw(screen)
        if(rect[17])and not(rect[8]):
            cir9.draw(screen)
    if(player1[1]):
        if(rect[0])and not(rect[9]):
            cro1.draw(screen)
        if(rect[1])and not(rect[10]):
            cro2.draw(screen)
        if(rect[2])and not(rect[11]):
            cro3.draw(screen)
        if(rect[3])and not(rect[12]):
            cro4.draw(screen)
        if(rect[4])and not(rect[13]):
            cro5.draw(screen)
        if(rect[5])and not(rect[14]):
            cro6.draw(screen)
        if(rect[6])and not(rect[15]):
            cro7.draw(screen)
        if(rect[7])and not(rect[16]):
            cro8.draw(screen)
        if(rect[8])and not(rect[17]):
            cro9.draw(screen)
    if(player2[1]):
        if(rect[9])and not(rect[0]):
            cir1.draw(screen)
        if(rect[10])and not(rect[1]):
            cir2.draw(screen)
        if(rect[11])and not(rect[2]):
            cir3.draw(screen)
        if(rect[12])and not(rect[3]):
            cir4.draw(screen)
        if(rect[13])and not(rect[4]):
            cir5.draw(screen)
        if(rect[14])and not(rect[5]):
            cir6.draw(screen)
        if(rect[15])and not(rect[6]):
            cir7.draw(screen)
        if(rect[16])and not(rect[7]):
            cir8.draw(screen)
        if(rect[17])and not(rect[8]):
            cir9.draw(screen)
    if(player1[2]):
        if(rect[0])and not(rect[9]):
            cro1.draw(screen)
        if(rect[1])and not(rect[10]):
            cro2.draw(screen)
        if(rect[2])and not(rect[11]):
            cro3.draw(screen)
        if(rect[3])and not(rect[12]):
            cro4.draw(screen)
        if(rect[4])and not(rect[13]):
            cro5.draw(screen)
        if(rect[5])and not(rect[14]):
            cro6.draw(screen)
        if(rect[6])and not(rect[15]):
            cro7.draw(screen)
        if(rect[7])and not(rect[16]):
            cro8.draw(screen)
        if(rect[8])and not(rect[17]):
            cro9.draw(screen)
    if(player2[2]):
        if(rect[9])and not(rect[0]):
            cir1.draw(screen)
        if(rect[10])and not(rect[1]):
            cir2.draw(screen)
        if(rect[11])and not(rect[2]):
            cir3.draw(screen)
        if(rect[12])and not(rect[3]):
            cir4.draw(screen)
        if(rect[13])and not(rect[4]):
            cir5.draw(screen)
        if(rect[14])and not(rect[5]):
            cir6.draw(screen)
        if(rect[15])and not(rect[6]):
            cir7.draw(screen)
        if(rect[16])and not(rect[7]):
            cir8.draw(screen)
        if(rect[17])and not(rect[8]):
            cir9.draw(screen)
    if(player1[3]):
        if(rect[0])and not(rect[9]):
            cro1.draw(screen)
        if(rect[1])and not(rect[10]):
            cro2.draw(screen)
        if(rect[2])and not(rect[11]):
            cro3.draw(screen)
        if(rect[3])and not(rect[12]):
            cro4.draw(screen)
        if(rect[4])and not(rect[13]):
            cro5.draw(screen)
        if(rect[5])and not(rect[14]):
            cro6.draw(screen)
        if(rect[6])and not(rect[15]):
            cro7.draw(screen)
        if(rect[7])and not(rect[16]):
            cro8.draw(screen)
        if(rect[8])and not(rect[17]):
            cro9.draw(screen)
    if(player2[3]):
        if(rect[9])and not(rect[0]):
            cir1.draw(screen)
        if(rect[10])and not(rect[1]):
            cir2.draw(screen)
        if(rect[11])and not(rect[2]):
            cir3.draw(screen)
        if(rect[12])and not(rect[3]):
            cir4.draw(screen)
        if(rect[13])and not(rect[4]):
            cir5.draw(screen)
        if(rect[14])and not(rect[5]):
            cir6.draw(screen)
        if(rect[15])and not(rect[6]):
            cir7.draw(screen)
        if(rect[16])and not(rect[7]):
            cir8.draw(screen)
        if(rect[17])and not(rect[8]):
            cir9.draw(screen)
    if(player1[4]):
        if(rect[0])and not(rect[9]):
            cro1.draw(screen)
        if(rect[1])and not(rect[10]):
            cro2.draw(screen)
        if(rect[2])and not(rect[11]):
            cro3.draw(screen)
        if(rect[3])and not(rect[12]):
            cro4.draw(screen)
        if(rect[4])and not(rect[13]):
            cro5.draw(screen)
        if(rect[5])and not(rect[14]):
            cro6.draw(screen)
        if(rect[6])and not(rect[15]):
            cro7.draw(screen)
        if(rect[7])and not(rect[16]):
            cro8.draw(screen)
        if(rect[8])and not(rect[17]):
            cro9.draw(screen)
    if(p1win):
        screen.blit(player1win, (width/2 -player1win.get_width()/2, 100))
    if(p2win):
        screen.blit(player2win, (width/2 - player2win.get_width()/2, 100))
    if(draw):
        screen.blit(draww, (width/2 - draww.get_width()/2, 100))
    pygame.display.update()
fr=frame(110,215)
cro1=cross(120,85)
cro2=cross(190,85)
cro3=cross(260,85)
cro4=cross(120,155)
cro5=cross(190,155)
cro6=cross(260,155)
cro7=cross(120,225)
cro8=cross(190,225)
cro9=cross(260,225)
cir1=circle(120,85)
cir2=circle(190,85)
cir3=circle(260,85)
cir4=circle(120,155)
cir5=circle(190,155)
cir6=circle(260,155)
cir7=circle(120,225)
cir8=circle(190,225)
cir9=circle(260,225)
run=1
while run:
    if (rect[0]) and(rect[1])and(rect[2]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p1win=False
                    start_time=False
                    start=False
                    pt1=180
                    pt2=180
                    clicks=[]
    elif (rect[3]) and(rect[4])and(rect[5]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    endingscreen=True
                    p1win=False
                    pt1=180
                    pt2=180
                    start_time=False
                    start=False
                    clicks=[]
    elif (rect[6]) and(rect[7])and(rect[8]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p1win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[0]) and(rect[3])and(rect[6]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p1win=False
                    pt1=180
                    pt2=180
                    start=False
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[1]) and(rect[4])and(rect[7]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p1win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[2]) and(rect[5])and(rect[8]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p1win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[0]) and(rect[4])and(rect[8]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p1win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[2]) and(rect[4])and(rect[6]):
        p1win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p1win=False
                    start=False
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[9]) and(rect[10])and(rect[11]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[12]) and(rect[13])and(rect[14]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    start=False
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[15]) and(rect[16])and(rect[17]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[9]) and(rect[12])and(rect[15]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[10]) and(rect[13])and(rect[16]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[11]) and(rect[14])and(rect[17]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    pt1=180
                    pt2=180
                    start=False
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[9]) and(rect[13])and(rect[17]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    elif (rect[11]) and(rect[13])and(rect[15]):
        p2win=True
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    p2win=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    else:
        if(player2[4]):
            draw=True
            clicks=[]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    rect=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
                    player1= [False,False,False,False,False]
                    player2= [False,False,False,False,False]
                    draw=False
                    start=False
                    pt1=180
                    pt2=180
                    start_time=False
                    endingscreen=True
                    clicks=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if (start):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                mx,my=pygame.mouse.get_pos()
                for i in range(0, 1):
                    x, y = event.pos
                    if (mx>110 and mx < 180) or (mx>190 and mx < 250) or (mx>260 and mx < 320):
                        if (my>75 and my<145) or (my>155 and my<215) or (my>225 and my<285):
                            pass
                if mx>110 and mx < 180:
                    if my>75 and my<145:
                        if(p1 and rect[0]==False and rect[9]==False ):
                            rect[0]=True
                            clicks.append([x, y])
                        elif(p2 and rect[9]==False and rect[0]==False):
                            rect[9]=True
                            clicks.append([x, y])
                if mx>190 and mx < 250:
                    if my>75 and my<145:
                        if(p1 and rect[1]==False and rect[10]==False):
                            rect[1]=True
                            clicks.append([x, y])
                        elif(p2 and rect[1]==False and rect[10]==False):
                            rect[10]=True
                            clicks.append([x, y])
                if mx>260 and mx < 320:
                    if my>75 and my<145:
                        if(p1 and rect[11]==False and rect[2]==False):
                            rect[2]=True
                            clicks.append([x, y])
                        elif(p2 and rect[11]==False and rect[2]==False):
                            rect[11]=True
                            clicks.append([x, y])
                if mx>110 and mx < 180:
                    if my>155 and my<215:
                        if(p1 and rect[3]==False and rect[12]==False):
                            rect[3]=True
                            clicks.append([x, y])
                        elif(p2):
                            rect[12]=True
                            clicks.append([x, y])
                if mx>190 and mx < 250:
                    if my>155 and my<215:
                        if(p1 and rect[4]==False and rect[13]==False):
                            rect[4]=True
                            clicks.append([x, y])
                        elif(p2 and rect[4]==False and rect[13]==False):
                            rect[13]=True
                            clicks.append([x, y])
                if mx>260 and mx < 320:
                    if my>155 and my<215:
                        if(p1 and rect[5]==False and rect[14]==False):
                            rect[5]=True
                            clicks.append([x, y])
                        elif(p2 and rect[5]==False and rect[14]==False):
                            rect[14]=True
                            clicks.append([x, y])
                if mx>110 and mx < 180:
                    if my>225 and my<285:
                        if(p1 and rect[6]==False and rect[15]==False):
                            rect[6]=True
                            clicks.append([x, y])
                        elif(p2 and rect[6]==False and rect[15]==False):
                            rect[15]=True
                            clicks.append([x, y])
                if mx>190 and mx < 250:
                    if my>225 and my<285:
                        if(p1 and rect[7]==False and rect[16]==False):
                            rect[7]=True
                            clicks.append([x, y])
                        elif(p2 and rect[7]==False and rect[16]==False):
                            rect[16]=True
                            clicks.append([x, y])
                if mx>260 and mx < 320:
                    if my>225 and my<285:
                        if(p1 and rect[8]==False and rect[17]==False):
                            rect[8]=True
                            clicks.append([x, y])
                        elif(p2 and rect[8]==False and rect[17]==False):
                            rect[17]=True
                            clicks.append([x, y])
        if len(clicks) == 1:
            player2[0]=True
            p2=True
            p1=False
            start_time2=pygame.time.get_ticks()
        if len(clicks) == 2:
            player1[1]=True
            p1=True
            p2=False
        if len(clicks) == 3:
            player2[1]=True
            p2=True
            p1=False
        if len(clicks) == 4:
            player1[2]=True
            p1=True
            p2=False
        if len(clicks) == 5:
            player2[2]=True
            p2=True
            p1=False
        if len(clicks) == 6:
            player1[3]=True
            p1=True
            p2=False
        if len(clicks) == 7:
            player2[3]=True
            p2=True
            p1=False
        if len(clicks) == 8:
            player1[4]=True
            p1=True
            p2=False
        if len(clicks) ==9:
            player2[4]=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start= True 
                endingscreen=False
                start_time = True
                start_time1=pygame.time.get_ticks()
                startingscreen=True
                player1[0]=True
                p1=True        
    redraw()  
pygame.quit()
