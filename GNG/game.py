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
import sys
from .gamerobot import gamerobot


class Game:
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
        start_ck2.fill((0,0,0))
        # 加载各个素材图片 并且赋予变量名
        pygame.mixer.init()
        self.click = "assets/click.ogg"
        self.click = pygame.mixer.music.load(self.click)
        
        self.rule = image.load("./assets/rule.png")
        self.rule1 = image.load("./assets/rule1.png")
        self.rule = transform.scale(self.rule, (400, 250))
        self.rule.convert()
        self.rule_show = False
        self.init_background = image.load("./assets/init.png")
        
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
        
        self.i6 = pygame.image.load("./assets/b61.png")
        self.i6 = transform.scale(self.i6, (300, 41))
        self.i6.convert()
        self.i61 = pygame.image.load("./assets/b62.png")
        self.i61 = transform.scale(self.i61, (300, 41))
        self.i61.convert()
#        
        start_ck.blit(self.init_background, (0, 0))
        n1 = True
        while n1:
            start_ck.blit(self.i1, (100, 300))
            start_ck.blit(self.i2, (100, 360))
            start_ck.blit(self.i3, (100, 420))
            start_ck.blit(self.i4, (100, 480))
            start_ck.blit(self.i6, (100, 540))
            start_ck.blit(self.rule1, (50, 30))
            
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if x1 >= 187 and x1 <= 555 and y1 >= 289 and y1 <=340:
                start_ck.blit(self.i11, (100, 300))
                start_ck.blit(self.rule, (50, 30))
                
        
            elif x1 >= 187 and x1 <= 555 and y1 >= 351 and y1 <=417:
                start_ck.blit(self.i21, (100, 360))
                if buttons[0]:
                    n1 = False
                    pygame.mixer.music.play()
                    
            elif x1 >= 187 and x1 <= 555 and y1 >= 424 and y1 <477:
                start_ck.blit(self.i31, (100, 420))
                if buttons[0]:
                    pygame.mixer.music.play()
                    gamerobot(timer = timer)
                    n1 = True
            elif x1 >= 187 and x1 <= 555 and y1 >= 490 and y1 <=537:
                start_ck.blit(self.i41, (100, 480))
                if buttons[0]:
                    n1 = False
                    pygame.mixer.music.play()
                    
            elif x1 >= 187 and x1 <= 555 and y1 >= 550 and y1 <=600:
                start_ck.blit(self.i61, (100, 540))
                if buttons[0]:
                    pygame.mixer.music.play()
                    pygame.quit()
                    sys.exit()
                    
            else:
                start_ck.blit(self.i1, (100, 300))
                start_ck.blit(self.i2, (100, 360))
                start_ck.blit(self.i3, (100, 420))
                start_ck.blit(self.i4, (100, 480))
                start_ck.blit(self.i6, (100, 540))
            
            self.screen.blit(start_ck,(0,0))
            pygame.display.update()
            # 下面是监听退出动作
        
            # 监听事件
            for event in pygame.event.get():
                # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    print("游戏退出...")
        
                    # quit 卸载所有的模块
                    pygame.quit()
        
                    # exit() 直接终止当前正在执行的程序
                    sys.exit()
        
        
        self.screen.blit(start_ck2,(0,0))
        pygame.display.update()


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
        
        self.imageb = image.load(Constants.IMAGEPLAYERB)
        self.imageb = transform.scale(self.imageb, (250, 293))
        self.moveset = 0;
        self.turn = 0
        self.time_out = False
        
        #空出来单独的一行，因为初始化的时候压入了多余的元素
        self.vis = [[ False for i in range (Constants.HOLECOLUMNS)]for j in range(Constants.HOLEROWS+1)]
        self.get = "assets/get.ogg"
        self.get = mixer.Sound(self.get)
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
        self.win_show = False
        self.holes = [[]for i in range(Constants.HOLECOLUMNS+1)]
        #保存了洞的一些坐标元组
        self.victory_play = False
        for column in range(Constants.HOLECOLUMNS):
            thisX = base_column * column
            thisX += (base_column - Constants.HOLEWIDTH) / 2
            for row in range(Constants.HOLEROWS):
                rowY = base_row * row
                rowY += (base_row - Constants.HOLEHEIGHT) / 2    
                self.holes[column].append((int(thisX), int(rowY)))
#                print(row, " ", column, " ", thisX, " ", rowY)
                
        
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
        for i in range(row, 0, -1):
            if(self.vis[i][col] == False):
                self.change[i][col] = 30;
                self.tot_stone -= 1
            self.vis[i][col] = True
    def loop_events(self):

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
                                if(self.judge(pos, thisX, rowY) and self.vis[row][column] == False):
                                    self.process(row, column)
#                                    print(row, column)
                                    pygame.mixer.music.load("assets/get.ogg")
                                    pygame.mixer.music.play()
                                    self.timer_start = time.get_ticks()
                                    flag = True
                                    self.turn += 1
                                    if(self.turn%2):
                                        self.a = True
                                        self.b = False
                                    else:
                                        self.a = False
                                        self.b = True
                                    self.moveset = 0
                                    break
                            if(flag):
                                break;

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
                        Game(timer=20)
                
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
            self.moveset += 0.2
        
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
                winner = "PLAYER1 WIN"
            elif(self.time_out and self.turn%2==0):
                winner = "PLAYER2 WIN"
            elif(self.tot_stone == 0):
                if(self.turn%2):
                    winner = "PLAYER1 WIN"
                else:
                    winner = "PLAYER2 WIN"
            timer_label_1 = self.text.get_label(winner, scale=3, color=(0, 150, 255))
            timer_label_2 = self.text.get_label("Press space to restart...", scale=2, color=(0, 150, 255))
            if(self.win_show == False):
                self.win_show = True
                
            else:
                if(winner == "PLAYER1 WIN"):
                    self.screen.blit(self.imagea, (150, 70))
                else:
                     self.screen.blit(self.imageb, (150, 70))
            if(self.victory_play == False):
                self.victory_play = True
                pygame.mixer.music.load("assets/victory.ogg")
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

    def run(self):
        self.start()
        quit()
