import cv2
import numpy as np
import pygame
from pygame import mixer
from pygamevideo import Video
#from music import playsound, playmusic, stopmusic, getmixerargs, initMixer

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

scene_counter = 0

#Screen Size
size_width = 450
size_height = 800

size_width = 1080 /2
size_height = 1920 /2

win_wid_cen = size_width / 2 
win_hei_cen = size_height / 2 

#size   = [1280, 720]
size = [size_width, size_height]
screen = pygame.display.set_mode(size)

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

OLDTV = pygame.image.load("media/OLDTV.png")

video_demo = Video("media/VIDEO_DEMO.mp4")

bob_video_demo = Video("media/BOB_DEMO.mp4")

done = False

clock = pygame.time.Clock()

#버튼 클래스를 만들어서, 클래스에 마우스 입력이 들어올 때마다
#scene_counter += 1하면 되지 않을까... 싶긴 한데.

# myFont = pygame.font.SysFont( "arial", 30, True, False)        
# text_Title= myFont.render("Pygame Text Test", True, WHITE)

# def ct(font, size, text, color):
#     mf = pygame.font.Font(font, size)

#     t = mf.render(text, True, color)

#     return t 

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


mixer.init()
mixer.music.load('media/MUSIC_DEMO.mp3')
mixer.music.play()

while not done:

    clock.tick(30)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN:
            scene_counter += 1

    screen.fill(BLACK)

    if scene_counter == 0:
        draw_scene1()

    elif scene_counter == 1:
        success, frame = cap.read()

        #frame = np.fliplr(frame)
        frame = np.rot90(frame)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        surf = pygame.surfarray.make_surface(frame)

        screen.blit(surf, (0,0))

        txt2 = ct(30, "Capture your face", WHITE)
        screen.blit(txt2, (make_center(txt2)[0], size_height - 300))

        #draw_scene2()
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

    elif scene_counter == 2:
        draw_scene3()

    elif scene_counter == 3:
        txt = ct(20, "SCENE4_STARTOFPART1", RED)
        screen.blit(txt, (make_center(txt)[0], 100))

    elif scene_counter == 4:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))
        #현재는 내부 텍스트로 구현했지만, 실제로는 배경 이미지에 미리 텍스트 작성
        txt = ct(20, "SCENE5_PART1.1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 5:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))
        #현재는 내부 텍스트로 구현했지만, 실제로는 배경 이미지에 미리 텍스트 작성
        txt = ct(20, "SCENE6_PART1.2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 6:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))
        #현재는 내부 텍스트로 구현했지만, 실제로는 배경 이미지에 미리 텍스트 작성
        txt = ct(20, "SCENE7_PART1.3", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 7:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))
        #현재는 내부 텍스트로 구현했지만, 실제로는 배경 이미지에 미리 텍스트 작성
        txt = ct(20, "SCENE8_PART1.4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 8:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))
        #현재는 내부 텍스트로 구현했지만, 실제로는 배경 이미지에 미리 텍스트 작성
        txt = ct(20, "SCENE9_PART1.5", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 9:
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))
        
        screen.blit(OLDTV, (make_center(OLDTV)[0], 0))

        txt = ct(20, "SCENE10_STARTOFPART2", RED)
        screen.blit(txt, (make_center(txt)[0], 100))

    elif scene_counter == 10:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

        #OLDTV = pygame.transform.scale(OLDTV, (1000, 1000))
        
        #screen.blit(OLDTV, (make_center(OLDTV)[0], 100))

        #screen.fill(BLACK)

        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE11_ZOOMOUT", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 11:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

        video_demo.play(loop=True)
        video_demo.draw_to(screen, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE12_PART2.1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 12:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE13_PART2.2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 13:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE14_PART2.3", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 14:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE15_PART2.4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 15:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        
        bob_video_demo.play()
        bob_video_demo.draw_to(screen, (make_center(FRAME256)[0] - 10, 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE16_PART2.5", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 16:
        txt = ct(20, "SCENE17_ENDING", RED)
        screen.blit(txt, (make_center(txt)[0], 100))

    elif scene_counter > 16:
        #done=True #주석 처리 지울 시 프로그램 종료
        scene_counter = 0

    pygame.display.update()

pygame.QUIT