# -*- coding: utf-8 -*-
"""003_static_blit_pretty_template.py"""
import pygame 
import random
import math
def radians_to_degrees(radians):
    return (radians /math.pi)*180.0
    
def degrees_to_radians(degrees):
    return degrees * (math.pi/180.0)


class PygView(object):
    width = 0
    height = 0
    def __init__(self, width=640, height=400, fps=100):
        """Initialize pygame, window, background, font,...
           default arguments """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        PygView.width = width
        PygView.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((255,255,255)) # fill background white
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)

    def paint(self):
        """painting on the surface"""
        #pygame.draw.line(Surface, color, start, end, width=1)
        #pygame.draw.rect(self.background, (0,0,255), (0,0,725,420)) # rect: (x1, y1, width, height)
        #pygame.draw.rect(self.background, (0,0,0), (725,0,725,420))
        #pygame.draw.rect(self.background, (0,0,0), (0,420,725,420))
        #pygame.draw.rect(self.background, (0,0,255), (720,420,725,420))
        #pygame.draw.line(self.background, (1,0,128), (0,0), (1450,840),(20))
        #pygame.draw.line(self.background, (1,0,128), (1450,0), (0,840),(20))
        #pygame.draw.line(self.background, (128,0,1), (0,10), (1450,10),(10))
        #pygame.draw.line(self.background, (128,0,1), (1450/2,0), (1450/2,840),(10))
        #pygame.draw.rect(Surface, color, Rect, width=0): return Rect
        #pygame.draw.rect(self.background, (0,0,255), (0,0,725,420)) # rect: (x1, y1, width, height)
        #pygame.draw.rect(self.background, (0,0,0), (725,0,725,420))
        #pygame.draw.rect(self.background, (0,0,0), (0,420,725,420))
        #pygame.draw.rect(self.background, (0,0,255), (720,420,725,420))
        #pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
        #pygame.draw.circle(self.background, (0,200,0), (0,0), 300)
        #pygame.draw.circle(self.background, (0,200,0), (1450,0), 300)
        #pygame.draw.circle(self.background, (0,200,0), (1450,840), 300)
        #pygame.draw.circle(self.background, (0,200,0), (0,840), 300)
        #pygame.draw.circle(self.background, (0,200,0), (725,420), 200)
        #pygame.draw.lines(self.background, (64,64,64), False,
        #[(0,350), (15,300),(30,400), (45,250),(70,250),(90,300),(100,500),(150,700)])
        #pygame.draw.ellipse(self.background, (255,0,0), (0,0,1450,815))
        #pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
        #pygame.draw.polygon(self.background, (0,180,0), ((250,100),(300,0),(350,50)))
        #pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
        #pygame.draw.arc(self.background, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad
        #pygame.draw.rect(self.background, (0,0,255), (0,0,725,420),1)
        #pygame.draw.ellipse(self.background, (255,0,0), (0,0,725,420))
        #pygame.draw.circle(self.background, (0,200,0), (365,210), 200)
        #pygame.draw.ellipse(self.background, (255,0,0), (365,0,50,400))
        #start = degrees_to_radians(90)
        #end = degrees_to_radians(5)
        #for x in range(0,1450,100):
            #for y in range(0,840,50):
                #pygame.draw.line(self.background, (0,0,255),(x,0),(0,y))
                 #pygame.draw.arc(self.background, (0,150,0),(725,10,725,420),start,end,1)
        xpoints=[]
        ypoints=[]
        xdist=PygView.width//100
        ydist=PygView.height//100
        for a in range(100):
            xpoints.append(xdist*a)
        for a in range(100):
            ypoints.append(ydist*a)
        for a in range(100):
            pygame.draw.line(self.background, (0,255-int(a*2.55),int(a*2.55)), (0,ypoints[a]),(xpoints[a],PygView.height))
            pygame.draw.line(self.background, (0+int(a*2.55),255-int(a*2.55),int(a*2.55)), (PygView.width,ypoints[a]),(xpoints[a],0))
            pygame.draw.line(self.background, (0+int(a*2.55),255-int(a*2.55),int(a*2.55)), (xpoints[-a],0),(0,ypoints[a]))
        for a in range(1, 100):
            pygame.draw.line(self.background, (0+int(a*2.55),255-int(a*2.55),int(a*2.55)), (xpoints[a],PygView.height),(PygView.width,ypoints[-a]))
        
        
        
        
        
        
            
    def run(self):
        self.paint() 
        myball = Ball() # creating the Ball object
        running = True
        while running:
            milliseconds = self.clock.tick(self.fps)
            seconds = milliseconds / 1000.0
            self.playtime += seconds
            #self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                           #self.clock.get_fps(), " "*5, self.playtime))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    # keys that you press once and release
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_q: # stopper 
                        myball.dx = 0
                        myball.dy = 0
                        myball.x = PygView.width //3 # one third without remainder
                        myball.y = PygView.height // 2 # one half without remainder
            pressedkeys = pygame.key.get_pressed() # keys that you can press all the time
            if pressedkeys[pygame.K_a]:
                myball.dx -=100
            if pressedkeys[pygame.K_d]:
                myball.dx +=100
            if pressedkeys[pygame.K_w]:
                myball.dy -= 100
            if pressedkeys[pygame.K_s]:
                myball.dy += 100
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))
            myball.update(seconds)
            myball.blit(self.screen) # blitting it
            #tail
            if len(myball.tail)>2:
                for a in range(1,len(myball.tail)):
                    pygame.draw.line(self.screen,(0,0,150),
                                     myball.tail[a-1],
                                     myball.tail[a],10-a//10)
        pygame.quit()

    def draw_text(self, text):
        """Center text in window"""
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (50,150))

class Ball(object):
    """this is not a native pygame sprite but instead a pygame surface"""
    def __init__(self, radius = 20, color=(0,0,255), x=320, y=240):
        """create a (black) surface and paint a blue ball on it"""
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        # create a rectangular surface for the ball 50x50
        self.surface = pygame.Surface((2*self.radius,2*self.radius))    
        pygame.draw.circle(self.surface, color, (radius, radius), radius) # draw blue filled circle on ball surface
        self.surface = self.surface.convert() # for faster blitting. 
        # to avoid the black background, make black the transparent color:
        # self.surface.set_colorkey((0,0,0))
        # self.surface = self.surface.convert_alpha() # faster blitting with transparent color
        self.tail=[]
        
    def update(self, seconds):
        self.x += self.dx * seconds
        self.y += self.dy * seconds
        # wrap around screen
        if self.x < 0:
            #self.x = PygView.width
            self.x=0
            self.dx*=-1
        if self.x > PygView.width:
            #self.x = 0
            self.x=PygView.width
            self.dx*=-1
        if self.y < 0:
            #self.y = PygView.height
            self.y=0
            self.dy*=-1
        if self.y > PygView.height:
            #self.y = 0
            self.y=PygView.height
            self.dy*=-1
        self.tail.insert(0,(self.x,self.y))
        self.tail=self.tail[:128]
        
            
        
    def blit(self, ground):
        """blit the Ball on the background"""
        ground.blit(self.surface, ( self.x, self.y))
        
if __name__ == '__main__':
    PygView(1450,815).run() # call with width of window and fps

