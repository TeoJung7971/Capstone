import cv2
import numpy as np
from time import *
import pygame
from pygame.locals import *
from pygame import mixer
from pygamevideo import Video
import RPGtext
#import pygame_widgets
#from pygame_widgets.button import Button
#from music import playsound, playmusic, stopmusic, getmixerargs, initMixer

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

global scene_counter; scene_counter = -1

#Screen Size
# size_width = 450
# size_height = 800

size_width = 1080
size_height = 1920

win_wid_cen = size_width / 2 
win_hei_cen = size_height / 2 

#size   = [1280, 720]
size = [size_width, size_height]
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode(size, pygame.NOFRAME)

#Builtin Camera using Opencv
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
cap.set(cv2.CAP_PROP_FPS, 30)

pygame.display.set_caption("media/Capstone Project")

background = pygame.image.load("media/BLACK_BACKGROUND.png")

FRAME256 =  pygame.image.load("media/256FRAME.png")

SCENE1 = pygame.image.load("media/SCENE1.png")

SCENE2 = pygame.image.load("media/SCENE2.png")

FACE1 = pygame.image.load("media/FACE1.jpeg")

FACE2 = pygame.image.load("media/FACE2.png")

OLDTV = pygame.image.load("media/tv.png")

PORTRAIT_DEMO = pygame.image.load("media/OIG.jpg")

glitch = Video("media/glitch.mp4")

glitch.mute()

part2_mario = Video("media/Mario_Kart_Rekt.mp4")

#비디오 크기 조정이 아직 되지 않았습니다.
#Adobe 비디오 크기 조정 사이트에서 크기 조정 가능합니다
#기존에 사용된 영상 크기 속성 참고하여 조정하면 될 듯 합니다
#기존 영상: tetris.mp4, chess.mp4, mine3.mp4

part2_tetris_1 = Video("media/Tetris1.mp4")

part2_tetris_2 = Video("media/Tetris2.mp4")

#part2_tetris.mute()

part2_chess_1 = Video("media/Chess1.mp4")

part2_chess_2 = Video("media/Chess2.mp4")

part2_chess_3 = Video("media/Chess3.mp4")

#part2_chess.mute()

part2_bomb1 = Video("media/bomb1.mp4")

part2_bomb2 = Video("media/bomb2.mp4")

part2_bomb3 = Video("media/bomb3.mp4")

part2_bomb4 = Video("media/bomb4.mp4")

part2_bomb5 = Video("media/bomb5.mp4")

#part2_mine3.mute()

part2_bob = Video("media/Bob.mp4")

part2_bob.mute()

video_demo = Video("media/VIDEO_DEMO.mp4")

bob_video_demo = Video("media/BOB_DEMO.mp4")

face_aging_demo = Video("media/DEMO_FACE_AGING.mp4")

loading = Video("media/Loading.mp4")

loading_long = Video("media/loading_long.mp4")

script = [0]*42


for i in range (0, 42):
    script[i] = pygame.image.load("script/script ({}).PNG".format(i+1))

done = False

clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

global action
action = 0

def button(msg, x, y, w, h, ic, ac, act = 0):
    global scene_counter
    global action

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #pygame.draw.rect(screen, ic,(x,y,w,h))

    #print(click)
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action == 0:

            sleep(0.3)
            action += 1

            if action ==1 and act == 1:
                print("Female")
            
            elif action ==1 and act == 2:
                print("Male")

            elif action == 1 and act == 0:
                scene_counter += 1
                print(action)
                return 0
     
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("cambria",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def ct(size, text, color):
    mf = pygame.font.SysFont("cambria", size, True, False)

    t = mf.render(text, True, color)

    return t 

def text_size(txt):
    t_width = txt.get_width()
    t_height = txt.get_height()
    return (t_width, t_height)

def make_center(txt):
    t_width = txt.get_width()
    t_height = txt.get_height()
    return ((size_width -  t_width)/1.9, (win_hei_cen - t_height))

def video_player_loading(video, duration, cordw = make_center(FRAME256)[0], cordh = 600):
    video.play(False)

    #duration을 ==으로 넣게 되면 제대로 작동하지 않음을 주의!
    if video.current_time >= duration:
        video.draw_to(screen, (cordw+350, cordh+830))
        video.pause()
        #박스 크기 조정하여 loading 영상 가릴 수 있도록 조정만 하면 될듯!
        pygame.draw.rect(screen, BLACK, [cordw+350, cordh+830, 80, 80])
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        
    else:
        video.draw_to(screen, (cordw+350, cordh+830))

video1  = Video("media\DEMO_FACE_AGING.mp4")

def video_player_dur_quar(video, duration, cordw = make_center(FRAME256)[0], cordh = 600):
    #video1 = video; 
    
    video2 = video1; video3 = video

    #face_aging_demo.resume()

    t = 20

    video.play(False)
    video1.play(False)
    video2.play(False)
    video3.play(False)
        
    if video.current_time >= duration :
        video.draw_to(screen, (cordw-128 - t, cordh-128 -t))
        video.pause()
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
    else:
        video.draw_to(screen, (cordw-128 - t, cordh-128 - t))

    if video1.current_time >= duration - 200 :
        video1.draw_to(screen, (cordw+128 + t, cordh-128 -t))
        video1.pause()
    else:
        video1.draw_to(screen, (cordw+128 + t, cordh-128 - t))
        #print(video1.current_time)

    if video2.current_time >= duration - 300:
        video2.draw_to(screen, (cordw-128 -t, cordh+128 + t))
        video2.pause()
    else:
        video2.draw_to(screen, (cordw-128 - t, cordh+128 + t))

    if video3.current_time >= duration :
        video3.draw_to(screen, (cordw+128 + t, cordh+128 + t))
        video3.pause()
    else:
        video3.draw_to(screen, (cordw+128 + t, cordh+128 + t))

def draw_scene1():
    #print("This is Scene 1")
    txt = ct(30, "<Convolution>", WHITE)
    screen.blit(txt, make_center(txt))


#def draw_scene2():
    #print("This is scene 2")

def draw_scene3():
    #print("This is Scene 1")
    txt3 = ct(30, "Did you know?", WHITE)
    screen.blit(txt3, (make_center(txt3)[0], 50))

def display_text_animation(string):
    text = ''
    for i in range(len(string)):
        screen.fill(BLACK)
        text += string[i]
        text_surface = ct(30, text, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (1080/2, 1100)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(120)

def slow(text): #function which displays characters one at a time
    for letters in text: #the variable goes through each character at a time
        print(letters, end = "") #current character is printed
        sleep(0.02) #insert the time between each character shown
#the for loop will move onto the next character

line_space = 16
basicfont = pygame.font.SysFont('cambria', 16)

def text_ani(str, tuple):
    x, y = tuple
    y = y*line_space ##shift text down by one line
    char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(str)):
        #pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        sleep(0.07) ##change this for faster or slower text animation
        char = char + str[letter]
        text = basicfont.render(char, False, WHITE, (0, 0, 0)) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(1080/2, 1400)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect) ## update only the text just added without removing previous lines.
        count += 1
        letter += 1

#음악 재생 시 에러 발생 추후 수정 예정
mixer.init()
mixer.music.load('media/MUSIC_CHILL.mp3')
mixer.music.set_volume = 0.5
mixer.music.play()
#=========================================

img_counter = 0

pause_cnt = 0

while not done:

    clock.tick(30)

    screen.fill(BLACK)

    # BUTTON_img = Buttonify('media\BUTTON_DEMO.png', (500, 900), screen)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     pass
            #scene_counter += 1

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_0:

                img_name = "outputimg/opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, cv2.cvtColor(np.rot90(frame, k = 3), cv2.COLOR_RGB2BGR))
                print("{} written!".format(img_name))
                img_counter += 1


    if scene_counter == -1:
        print(loading.duration)
        draw_scene1()
        button("START", 1080/2, 1000, 80,40, WHITE, BLACK)      

    elif scene_counter == 0:
        screen.blit(BLACK, (0, 0))
        button("Female", 300, 1080-300, 80,40, WHITE, BLACK, act = 1)
        button("Male", 780, 1500, 80,40, WHITE, BLACK, act = 2)

        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 1:
        screen.blit(script[0], (0, 0))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 2:
        screen.blit(script[1], (0,0))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 3:
        screen.blit(script[2], (0, 0))
        #장비에 카메라가 존재하지 않는 경우 본 캡쳐 부분은 주석 처리 후 실행
        success, frame = cap.read()

        frame = np.fliplr(frame)
        frame = np.rot90(frame)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        surf = pygame.surfarray.make_surface(frame)

        screen.blit(surf, (230,500))
        #===============================================================

        txt2 = ct(30, "Capture your face", WHITE)
        screen.blit(txt2, (make_center(txt2)[0], size_height - 300))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0
        #draw_scene2()
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

    elif scene_counter == 4:
        screen.blit(script[3], (0,0))
        video_player_loading(loading_long, 3000.0, make_center(FRAME256)[0], 600)
        #draw_scene3()
        action = 0

    elif scene_counter == 5:
        screen.blit(script[4], (0,0))
        txt = ct(20, "SCENE4_STARTOFPART1", RED)
        screen.blit(txt, (make_center(txt)[0], 100))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 6:
        screen.blit(script[5], (0,0))

        video_player_dur_quar(face_aging_demo, 1000.0)

        txt = ct(20, "SCENE5_PART1.1_1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        action = 0

    elif scene_counter == 7:
        screen.blit(script[6], (0,0))

        video_player_dur_quar(face_aging_demo, 1000.0)

        txt = ct(20, "SCENE5_PART1.1_2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 8:
        screen.blit(script[7], (0,0))

        video_player_dur_quar(face_aging_demo, 1000.0)

        txt = ct(20, "SCENE5_PART1.1_2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 9:
        screen.blit(script[8], (0,0))

        if  pause_cnt == 0:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
            video1.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 2000.0)

        txt = ct(20, "SCENE6_PART1.2_1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 10:
        screen.blit(script[9], (0,0))

        video_player_dur_quar(face_aging_demo, 2000.0)

        txt = ct(20, "SCENE6_PART1.2_2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 11:
        screen.blit(script[10], (0,0))

        video_player_dur_quar(face_aging_demo, 2000.0)

        txt = ct(20, "SCENE6_PART1.2_3", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 12:
        screen.blit(script[11], (0,0))

        video_player_dur_quar(face_aging_demo, 2000.0)

        txt = ct(20, "SCENE6_PART1.2_4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 13:
        screen.blit(script[12], (0,0))

        if  pause_cnt == 1:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
            video1.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 3000.0)
        
        txt = ct(20, "SCENE7_PART1.3_1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 14:
        screen.blit(script[13], (0,0))

        video_player_dur_quar(face_aging_demo, 3000.0)
        
        txt = ct(20, "SCENE7_PART1.3_2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 15:
        screen.blit(script[14], (0,0))

        video_player_dur_quar(face_aging_demo, 3000.0)
        
        txt = ct(20, "SCENE7_PART1.3_3", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 16:
        screen.blit(script[15], (0,0))

        video_player_dur_quar(face_aging_demo, 3000.0)
        
        txt = ct(20, "SCENE7_PART1.3_4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 17:
        screen.blit(script[16], (0,0))

        if  pause_cnt == 2:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
            video1.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 4000.0)

        txt = ct(20, "SCENE8_PART1.4_1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 18:
        screen.blit(script[17], (0,0))

        video_player_dur_quar(face_aging_demo, 4000.0)

        txt = ct(20, "SCENE8_PART1.4_2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 19:
        screen.blit(script[18], (0,0))

        video_player_dur_quar(face_aging_demo, 4000.0)

        txt = ct(20, "SCENE8_PART1.4_3", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 20:
        screen.blit(script[19], (0,0))

        video_player_dur_quar(face_aging_demo, 4000.0)

        txt = ct(20, "SCENE8_PART1.4_4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 21:
        screen.blit(script[20], (0,0))

        video_player_dur_quar(face_aging_demo, 4000.0)

        txt = ct(20, "SCENE8_PART1.4_5", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 22:
        screen.blit(script[21], (0,0))

        if  pause_cnt == 3:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
            video1.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 4500.0)

        txt = ct(20, "SCENE9_PART1.5_1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 23:
        screen.blit(script[22], (0,0))

        video_player_dur_quar(face_aging_demo, 4500.0)

        txt = ct(20, "SCENE9_PART1.5_2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 24:
        screen.blit(script[23], (0,0))

        video_player_dur_quar(face_aging_demo, 4500.0)

        txt = ct(20, "SCENE9_PART1.5_3", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 25:
        screen.blit(script[24], (0,0))

        video_player_dur_quar(face_aging_demo, 4500.0)

        txt = ct(20, "SCENE9_PART1.5_4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 26:
        screen.blit(script[25], (0,0))

        video_player_dur_quar(face_aging_demo, 4500.0)

        txt = ct(20, "SCENE9_PART1.5_4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 27:
        screen.blit(script[26], (0,0))

        video_player_dur_quar(face_aging_demo, 4500.0)

        txt = ct(20, "SCENE9_PART1.5_4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 28:
        screen.blit(script[27], (0,0))

        txt = ct(20, "SCENE9_PART1_Ending", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 29:
        screen.blit(script[28], (0,0))

        txt = ct(20, "SCENE9_PART1_Ending", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 30:
        screen.blit(script[29], (0,0))

        txt = ct(20, "SCENE9_PART1_Ending", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 31:
        screen.fill('BLACK')

        txt = ct(20, "SCENE9_PART1_Ending", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 32:
        #zoomout 처리의 어색함.. 그냥 암전으로 갈까?

        OLDTV.set_alpha(70) 
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))
        
        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))

        txt = ct(20, "SCENE10_STARTOFPART2", RED)
        screen.blit(txt, (make_center(txt)[0], 100))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 33:

        OLDTV.set_alpha(100) 
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE11_ZOOMOUT", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 34:

        OLDTV.set_alpha(1000) 
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE11_ZOOMOUT", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 35:
        screen.blit(script[30], (0,0))

        part2_mario.play(loop=False)
        part2_mario.draw_to(screen, (320, 530))

        #glitch.draw_to(screen, (make_center(FRAME256)[0] - 127, 180))

        if part2_mario.current_time >= 12000.0:
            part2_mario.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE12_PART2.1_mario", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 36:
        screen.blit(script[31], (0,0))

        part2_tetris_1.play(loop=False)
        part2_tetris_1.draw_to(screen, (320, 530))

        #glitch.draw_to(screen, (make_center(FRAME256)[0] - 127, 180))

        if part2_tetris_1.current_time >= 5000.0:
            part2_tetris_1.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 37:
        screen.blit(script[32], (0,0))

        part2_tetris_2.play(loop=False)

        part2_tetris_2.mute()
        part2_tetris_2.draw_to(screen, (320, 530))

        #glitch.draw_to(screen, (make_center(FRAME256)[0] - 127, 180))

        if part2_tetris_2.current_time >= 9000.0:
            part2_tetris_2.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 38:
        screen.blit(script[33], (0,0))

        part2_chess_1.play(loop=False)

        part2_chess_1.mute()
        part2_chess_1.draw_to(screen, (200, 460))

        if part2_chess_1.current_time >= 8000.0:
            part2_chess_1.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 39:
        screen.blit(script[34], (0,0))

        part2_chess_2.play(loop=False)

        part2_chess_2.mute()
        part2_chess_2.draw_to(screen, (200, 460))

        if part2_chess_2.current_time >= 25000.0:
            part2_chess_2.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 40:
        screen.blit(script[35], (0,0))

        part2_chess_3.play(loop=False)

        part2_chess_3.mute()
        part2_chess_3.draw_to(screen, (200, 460))

        if part2_chess_3.current_time >= 3000.0:
            part2_chess_3.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 41:
        screen.blit(script[36], (0,0))

        part2_bomb1.play(loop=False)

        part2_bomb1.mute()
        part2_bomb1.draw_to(screen, (270, 390))

        if part2_bomb1.current_time >= 3000.0:
            part2_bomb1.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 42:
        screen.blit(script[37], (0,0))

        part2_bomb2.play(loop=False)

        part2_bomb2.mute()
        part2_bomb2.draw_to(screen, (270, 390))

        if part2_bomb2.current_time >= 5000.0:
            part2_bomb2.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 43:
        screen.blit(script[38], (0,0))

        part2_bomb3.play(loop=False)

        part2_bomb3.mute()
        part2_bomb3.draw_to(screen, (270, 390))


        if part2_bomb3.current_time >= 9000.0:
            part2_bomb3.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
    
    elif scene_counter == 44:
        screen.blit(script[39], (0,0))

        part2_bomb4.play(loop=False)

        part2_bomb4.mute()
        part2_bomb4.draw_to(screen, (270, 390))


        if part2_bomb4.current_time >= 5000.0:
            part2_bomb4.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 45:
        screen.blit(script[40], (0,0))

        part2_bomb5.play(loop=False)

        part2_bomb5.mute()
        part2_bomb5.draw_to(screen, (270, 390))


        if part2_bomb5.current_time >= 2000.0:
            part2_bomb5.pause()
            glitch.play(loop=False)
            glitch.mute()
            glitch.draw_to(screen, (250, 430))
            button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
            action = 0
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 46:
        screen.blit(script[41], (0,0))

        glitch.pause()

        part2_bob.play(loop=False)
        part2_bob.mute()
        part2_bob.draw_to(screen, (260, 500))

        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 47:
        screen.blit(script[42], (0,0))

        #part2_bob.play(loop=False)
        part2_bob.mute()
        part2_bob.draw_to(screen, (260, 500))

        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 48:
        screen.blit(script[43], (0,0))

        #part2_bob.play(loop=False)
        part2_bob.mute()
        part2_bob.draw_to(screen, (260, 500))

        if part2_bob.current_time == 9000.0:
            part2_bob.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 49:
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 300))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter == 50:
        PORTRAIT_DEMO = pygame.transform.scale(PORTRAIT_DEMO, (600, 600))
        screen.blit(PORTRAIT_DEMO, (make_center(PORTRAIT_DEMO)[0], 300))

        txt = ct(20, "SCENE17_ENDING", RED)
        screen.blit(txt, (make_center(txt)[0], 100))
        button("NEXT", 780, 1500, 80,40, WHITE, BLACK)
        action = 0

    elif scene_counter > 51:
        done=True #주석 처리 지울 시 프로그램 종료
        scene_counter = 0

    pygame.display.update()

pygame.QUIT