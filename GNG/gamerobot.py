# -*- coding: utf-8 -*-

"""
Whack a Mole
~~~~~~~~~~~~~~~~~~~
A simple Whack a Mole game written with PyGame
:copyright: (c) 2018 Matt Cowley (IPv4)
"""

from pygame import init, quit, mixer, display, image, transform, time, mouse, event, Surface, \
    SRCALPHA, QUIT, MOUSEBUTTONDOWN, KEYDOWN, \
    K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p, K_SPACE, K_ESCAPE

from .constants import Constants
from .score import Score
from .text import Text
import pygame


class gamerobot:
    """
    Handles the main game
    Takes :time: in seconds for game timer
    """

    def __init__(self, *, timer: int = None, autostart: bool = True):
        # Init pygame
        init()
        self.screen = display.set_mode((Constants.GAMEWIDTH, Constants.GAMEHEIGHT))
        display.set_caption(Constants.TEXTTITLE)
        start_ck = pygame.Surface(self.screen.get_size())    #   充当开始界面的画布
        start_ck2 = pygame.Surface(self.screen.get_size())  #  充当第一关的画布界面暂时占位（可以理解为游戏开始了）
        start_ck = start_ck.convert()
        start_ck2 = start_ck2.convert()
        start_ck.fill((255,255,255))  # 白色画布1（开始界面用的）
        start_ck2.fill((0,255,0))
        # 加载各个素材图片 并且赋予变量名
        pygame.mixer.init()
        self.click = "assets/click.ogg"
        self.click = pygame.mixer.music.load(self.click)
        
        
        
        self.i1 = pygame.image.load("./assets/b11.png")
        self.i1 = transform.scale(self.i1, (300, 41))
        self.i1.convert()
        self.i11 = pygame.image.load("./assets/b12.png")
        self.i11 = transform.scale(self.i11, (300, 41))
        self.i11.convert()
        
        self.i2 = pygame.image.load("./assets/b21.png")
        self.i2 = transform.scale(self.i2, (300, 41))
        self.i2.convert()
        self.i21 = pygame.image.load("./assets/b22.png")
        self.i21 = transform.scale(self.i21, (300, 41))
        self.i21.convert()
        
        self.i3 = pygame.image.load("./assets/b31.png")
        self.i3 = transform.scale(self.i3, (300, 41))
        self.i3.convert()
        self.i31 = pygame.image.load("./assets/b32.png")
        self.i31 = transform.scale(self.i31, (300, 41))
        self.i31.convert()
        
        self.i4 = pygame.image.load("./assets/b41.png")
        self.i4 = transform.scale(self.i4, (300, 41))
        self.i4.convert()
        self.i41 = pygame.image.load("./assets/b42.png")
        self.i41 = transform.scale(self.i41,(300, 41))
        self.i41.convert()
        
        self.i5 = pygame.image.load("./assets/b51.png")
        self.i5 = transform.scale(self.i5, (300, 41))
        self.i5.convert()
        self.i51 = pygame.image.load("./assets/b52.png")
        self.i51 = transform.scale(self.i51, (300, 41))
        self.i51.convert()
        
        self.i6 = pygame.image.load("./assets/n1.png")
        self.i6 = transform.scale(self.i6, (300, 41))
        self.i6.convert()
        self.i61 = pygame.image.load("./assets/n2.png")
        self.i61 = transform.scale(self.i61, (300, 41))
        self.i61.convert()
#        
        
        
        # Create pygame screen
       

        # Load background
        self.img_background = image.load(Constants.IMAGEBACKGROUND)
        #背景图适应设置的大小
        self.img_background = transform.scale(self.img_background, (Constants.GAMEWIDTH, Constants.GAMEHEIGHT))

        # Load hole
        self.img_hole = image.load(Constants.IMAGEHOLE)
        self.img_hole = transform.scale(self.img_hole, (Constants.HOLEWIDTH, Constants.HOLEHEIGHT))
        self.img_hole_change = image.load(Constants.IMAGEHOLE_CHANGE)
        self.img_hole_change = transform.scale(self.img_hole_change, (Constants.HOLEWIDTH, Constants.HOLEHEIGHT))

        # Load mallet
        self.img_mallet = image.load(Constants.IMAGEMALLET)
        self.img_mallet = transform.scale(self.img_mallet, (Constants.MALLETWIDTH, Constants.MALLETHEIGHT))

        # Set timer
        self.timer = timer
        # set figure
        self.imagea = image.load(Constants.IMAGEPLAYERA)
        self.imagea = transform.scale(self.imagea, (250, 293))
        
        self.imageb = image.load("assets/cxk.png")
        self.imageb = transform.scale(self.imageb, (250, 293))
        self.imageb2 = image.load("assets/cxk1.png")
        self.imageb2 = transform.scale(self.imageb2, (250, 293))
        self.moveset = 0;
        self.turn = 0
        self.time_out = False
        
        #空出来单独的一行，因为初始化的时候压入了多余的元素
        self.vis = [[ False for i in range (Constants.HOLECOLUMNS)]for j in range(Constants.HOLEROWS+1)]
        pygame.mixer.music.load("assets/get.ogg")
        
        temp = "assets/"
        self.diamond = [image.load(Constants.IMAGEPLAYERB) for i in range(Constants.HOLECOLUMNS)]
        for i in range(Constants.HOLECOLUMNS):
            aid = temp+"dia"+repr(i+1)+".png"
            self.diamond[i] = image.load(aid)
            self.diamond[i] = transform.scale(self.diamond[i], (Constants.HOLEWIDTH, Constants.HOLEHEIGHT))
            
        self.diamond_remove = [image.load(Constants.IMAGEPLAYERB) for i in range(Constants.HOLECOLUMNS)]
        for i in range(Constants.HOLECOLUMNS):
            aid = temp+"dia"+repr(i+1)+"2.png"
            self.diamond_remove[i] = image.load(aid)
            self.diamond_remove[i] = transform.scale(self.diamond_remove[i], (Constants.HOLEWIDTH, Constants.HOLEHEIGHT))
        
        
        
        # Reset/initialise data
        self.reset()

        # Run
        if autostart:
            self.run()

    def reset(self):
        
        # Generate hole positions
        for i in range(Constants.HOLEROWS+1):
            for j in range(Constants.HOLECOLUMNS):
                self.vis[i][j] = False;
        
        base_row = Constants.GAMEHEIGHT // Constants.HOLEROWS
        base_column = Constants.GAMEWIDTH // Constants.HOLECOLUMNS
        self.holes = [[(0, 0)]for i in range(base_column)]
        #print(Constants.HOLEROWS, Constants.HOLECOLUMNS)
        self.tot_stone =  (Constants.HOLEROWS-1)*Constants.HOLECOLUMNS
        self.moveset = 0;
        self.turn = 0
        self.time_out = False
        self.a = False
        self.b = False
        self.back_on = False
        self.out = False
        self.victory_play = False
        self.holes = [[]for i in range(Constants.HOLECOLUMNS+1)]
        self.num = [Constants.HOLEROWS-1 for i in range(Constants.HOLECOLUMNS+1)]
        
        self.move = False
        self.pause = 50
        self.win_show = False
        #保存了洞的一些坐标元组
        for column in range(Constants.HOLECOLUMNS):
            thisX = base_column * column
            thisX += (base_column - Constants.HOLEWIDTH) / 2
            for row in range(Constants.HOLEROWS):
                rowY = base_row * row
                rowY += (base_row - Constants.HOLEHEIGHT) / 2    
                self.holes[column].append((int(thisX), int(rowY)))
                print(row, " ", column, " ", thisX, " ", rowY)
                
        
        # Get the text object
        self.text = Text()

        # Get the score object
        self.score = Score(self.text)

        # Indicates whether the HUD indicators should be displayed
        self.show_hit = 0
        self.show_miss = 0
        self.change = [[0 for i in range(Constants.HOLECOLUMNS+1)] for j in range(Constants.HOLEROWS+1)]

        # Allow for game timer
        #记录此刻的系统的时间
        self.timer_start = 0

    @property
    def timerData(self):
        if self.timer is not None and self.timer_start != 0:
            remain = (time.get_ticks() - self.timer_start) / 1000
            remain = self.timer - remain
            self.time_out = True if remain <= 0 else False
            endGame = True if remain <= 0 else False
            if(self.tot_stone == 0):
                endGame = True
                remain = 0.1
            return (remain, endGame)
        return (None, False)
    
    def judge(self, pos, x, y):
        
        mousex, mousey = pos
        mousex -= Constants.HOLEHEIGHT/2
        mousey -= Constants.HOLEWIDTH/2
        #偏移的范围
        pian_yi = 15
        if(x-pian_yi<=mousex and x+pian_yi>=mousex and 
           y-pian_yi<=mousey and y+pian_yi>=mousey):
            return True
        return False
    
    def process(self, row, col):
        tot = 0
        for i in range(row, 0, -1):
            if(self.vis[i][col] == False):
                self.change[i][col] = 30;
                tot += 1
                self.tot_stone -= 1
            self.vis[i][col] = True
        self.num[col] -= tot
                
    def robot(self):
        ans = 0
        red = 0#要减少的个数
        idx = -1
        for i in range(0, Constants.HOLECOLUMNS):
            ans ^= self.num[i]
        for i in range(0, Constants.HOLECOLUMNS):
            for j in range(1, self.num[i]+1):
                if((ans ^ self.num[i] ^ (self.num[i]-j)) == 0):
                    idx = i
                    red = j
                    break
            if(idx!=-1):
                break
        if(idx == -1):
            for i in range(0, Constants.HOLECOLUMNS):
                if(self.num[i]>0):
                    idx = i
                    red =1
        tot = 1
        self.num[idx] -= red
        print("hahaha   ", idx, red)
        while(red>0 and tot<Constants.HOLEROWS):
            while(self.vis[tot][idx] == True):
                tot+=1
            self.vis[tot][idx] = True
            self.tot_stone -= 1
            self.change[tot][idx] = 30
            red -= 1
    def loop_events(self):
        if(self.turn%2==1 and self.move and self.pause>0):
            self.pause -= 1
        elif(self.turn%2==1 and self.move):
            self.move = False
            self.turn += 1
            self.robot()
            pygame.mixer.music.play()
            self.timer_start = time.get_ticks()
            self.a = False
            self.b = True
            self.moveset = 0
            
        hit = False
        miss = False
        clicked = False#表示是否有按键的动作
        #system function
        pos = mouse.get_pos()

        # Handle PyGame events
        for e in event.get():

            # Handle quit
            if e.type == QUIT:
                self.loop = False
                break

            gameTime, endGame = self.timerData
            
            
            if not endGame:

                # Handle click
                if e.type == MOUSEBUTTONDOWN and e.button == Constants.LEFTMOUSEBUTTON:

                    # Start timer if not started
                    if self.timer is not None and self.timer_start == 0:
                        self.timer_start = time.get_ticks()

                    else:
                        # Handle hit/miss
                        clicked = True
                        miss = True
                        
                        flag = False;
                        print(pos[0], pos[1])
                        base_row = Constants.GAMEHEIGHT // Constants.HOLEROWS
                        base_column = Constants.GAMEWIDTH // Constants.HOLECOLUMNS
                        for column in range(Constants.HOLECOLUMNS):
                            thisX = base_column * column
                            thisX += (base_column - Constants.HOLEWIDTH) / 2
                            for row in range(Constants.HOLEROWS):
                                rowY = base_row * row
                                rowY += (base_row - Constants.HOLEHEIGHT) / 2    
                                if(self.judge(pos, thisX, rowY) and self.vis[row][column] == False and self.turn%2==0):
                                    self.process(row, column)
                                    print(row, column)
                                    #self.get.play(1)
                                    pygame.mixer.music.load("assets/get.ogg")
                                    pygame.mixer.music.play()
                                    self.timer_start = time.get_ticks()
                                    flag = True
                                    self.turn += 1
                                    if(self.turn%2):
                                        self.a = True
                                        self.b = False
                                        if(self.tot_stone>0):
                                            self.move = True
                                        self.pause = 100
                                    else:
                                        self.a = False
                                        self.b = True
                                    self.moveset = 0
                                    break
                            if(flag):
                                break

                        if hit:
                            self.score.hit()
                        if miss:
                            self.score.miss()

                if e.type == KEYDOWN:

                    # Allow escape to abort attempt
                    if e.key == K_ESCAPE:
                        self.reset()
                        break

                    # Handle cheats (for dev work)
                    if Constants.DEBUGMODE:
                        if e.key == K_e:
                            hit = True
                            miss = False
                            self.score.hit()
                        if e.key == K_r:
                            hit = False
                            miss = True
                            self.score.miss()

                        if e.key == K_t:
                            self.score.misses = 0
                        if e.key == K_y:
                            self.score.misses += 5
                        if e.key == K_u:
                            self.score.misses -= 5

                        if e.key == K_i:
                            self.score.hits = 0
                        if e.key == K_o:
                            self.score.hits += 5
                        if e.key == K_p:
                            self.score.hits -= 5

            # End game screen
            else:
                if(pos[0]>120 and pos[0]<320 and pos[1]>600 and pos[1]<660):
                    self.back_on = True
                else :
                    self.back_on = False
                if e.type == MOUSEBUTTONDOWN:
                    
                    if(pos[0]>120 and pos[0]<300 and pos[1]>600 and pos[1]<660):
                        self.out = True
                
                if e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        # Restart
                        self.reset()
                        break
                   
                

        return (clicked, hit, miss)

    def loop_display(self, clicked, hit, miss):
        gameTime, endGame = self.timerData
        if not gameTime and self.timer:
            gameTime = -1

        # Display bg
        self.screen.blit(self.img_background, (0, 0))

        # Display holes
        #有一个防止栈空
        for i in range(1, Constants.HOLEROWS):
            for j in range(Constants.HOLECOLUMNS):
                if(self.vis[i][j] == False):
                    self.screen.blit(self.diamond[j%Constants.HOLECOLUMNS], self.holes[j][i])
        flag = False
        for i in range(1, Constants.HOLEROWS):
            for j in range(Constants.HOLECOLUMNS):
                if(self.change[i][j] > 0):
                    flag = True
                    self.screen.blit(self.diamond_remove[j%Constants.HOLECOLUMNS], self.holes[j][i])
                    self.change[i][j] -= 1
                    
        if(flag):
            if(self.turn%2):
                self.screen.blit(self.imagea, (0+self.moveset, 200+self.moveset))
            else:
                self.screen.blit(self.imageb, (250-self.moveset, 200-self.moveset))
            self.moveset += 0.3
        
        thisHammer = transform.rotate(self.img_mallet.copy(),
                                      (Constants.MALLETROTHIT if clicked else Constants.MALLETROTNORM))
        hammer_x, hammer_y = mouse.get_pos()
        hammer_x -= thisHammer.get_width() / 5
        hammer_y -= thisHammer.get_height() / 4
        self.screen.blit(thisHammer, (hammer_x, hammer_y))

        # Fade screen if not started or has ended
        if self.timer and (endGame or gameTime == -1):
            overlay = Surface((Constants.GAMEWIDTH, Constants.GAMEHEIGHT), SRCALPHA, 32)
            overlay = overlay.convert_alpha()
            #rgb, opacity
            overlay.fill((100, 100, 100, 0.8 * 255))
            self.screen.blit(overlay, (0, 0))

        # Debug data for readout
        debug_data = {}
        if Constants.DEBUGMODE:
            debug_data = {
                "DEBUG": True,
                "FPS": int(self.clock.get_fps()),
                "MOLES": "{}/{}".format(Constants.MOLECOUNT, Constants.HOLEROWS * Constants.HOLECOLUMNS),
                "KEYS": "E[H]R[M]T[M0]Y[M+5]U[M-5]I[H0]O[H+5]P[H-5]"
            }

        # Display data readout
        data = self.score.label(timer=gameTime, turn=self.turn, debug=debug_data, size=(1.5 if endGame else 1.5))
        self.screen.blit(data, (5, 5))
        
        # Display hit/miss indicators
        if not endGame:
            
            # Hit indicator
            if self.a:
                self.show_hit = time.get_ticks()
                self.a = False
            if self.show_hit > 0 and time.get_ticks() - self.show_hit <= Constants.MOLEHITHUD:
                hit_label = self.text.get_label("PLAYER 1 DONE", scale=3, color=(255, 50, 0))
                hit_x = (Constants.GAMEWIDTH - hit_label.get_width()) / 2
                hit_y = (Constants.GAMEHEIGHT - hit_label.get_height()) / 2
                self.screen.blit(hit_label, (hit_x, hit_y))
            else:
                self.show_hit = 0

            # Miss indicator
            if self.b:
                self.show_miss = time.get_ticks()
                self.b = False
            if self.show_miss > 0 and time.get_ticks() - self.show_miss <= Constants.MOLEMISSHUD:
                miss_label = self.text.get_label("PLAYER 2 DONE", scale=2, color=(0, 150, 255))
                miss_x = (Constants.GAMEWIDTH - miss_label.get_width()) / 2
                miss_y = (Constants.GAMEHEIGHT + miss_label.get_height()) / 2
                self.screen.blit(miss_label, (miss_x, miss_y))
            else:
                self.show_miss = 0

        # Click to start indicator
        if self.timer and gameTime == -1:
            timer_label = self.text.get_label("Click to begin...", scale=2, color=(0, 255, 255))
            timer_x = (Constants.GAMEWIDTH - timer_label.get_width()) / 2
            timer_y = (Constants.GAMEHEIGHT - timer_label.get_height()) / 2
            self.screen.blit(timer_label, (timer_x, timer_y))
            

        # Time's up indicator
        if endGame:
            winner = ""
            if(self.time_out and self.turn%2):
                winner = "YOU PLAY BETTER THAN CXK"
            elif(self.time_out and self.turn%2==0):
                winner = "YOU PALY AS GOOD AS CXK"
            elif(self.tot_stone == 0):
                if(self.turn%2):
                    winner = "YOU PLAY BETTER THAN CXK"
                else:
                    winner = "YOU PALY AS GOOD AS CXK"
            timer_label_1 = self.text.get_label(winner, scale=2, color=(0, 150, 255))
            timer_label_2 = self.text.get_label("Press space to restart...", scale=2, color=(0, 150, 255))
            
            if(self.win_show == False):
                self.win_show = True
                
            else:
                if(winner == "YOU PLAY BETTER THAN CXK"):
                    self.screen.blit(self.imagea, (150, 70))
                else:
                     self.screen.blit(self.imageb2, (150, 70))
            
            if(self.victory_play == False):
                self.victory_play = True
                pygame.mixer.music.load("assets/cxkwin.wav")
                pygame.mixer.music.play()
            
            timer_x_1 = (Constants.GAMEWIDTH - timer_label_1.get_width()) / 2
            timer_x_2 = (Constants.GAMEWIDTH - timer_label_2.get_width()) / 2

            timer_y_1 = (Constants.GAMEHEIGHT / 2) - timer_label_1.get_height()
            timer_y_2 = (Constants.GAMEHEIGHT / 2)

            self.screen.blit(timer_label_1, (timer_x_1, timer_y_1+70))
            self.screen.blit(timer_label_2, (timer_x_2, timer_y_2+70))
            if(self.back_on == False):
                self.screen.blit(self.i5, (120, 600))
            else :
                self.screen.blit(self.i51, (120, 600))

    def start(self):
        self.clock = time.Clock()
        self.loop = True

        while self.loop:
            # Do all events
            clicked, hit, miss = self.loop_events()

            # Do all render
            self.loop_display(clicked, hit, miss)
                

            # Update display
            self.clock.tick(Constants.GAMEMAXFPS)
            display.flip()
            if(self.out):
                break

    def run(self):
        self.start()
        print("you are here")
