import cv2
import numpy as np
import pygame
from pygame import mixer
from pygamevideo import Video
import pygame_widgets
from pygame_widgets.button import Button
#from music import playsound, playmusic, stopmusic, getmixerargs, initMixer

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

scene_counter = 0

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

glitch = Video("media/glitch.mp4")

part2_tetris = Video("media/Tetris.mp4")

video_demo = Video("media/VIDEO_DEMO.mp4")

bob_video_demo = Video("media/BOB_DEMO.mp4")

face_aging_demo = Video("media\DEMO_FACE_AGING.mp4")

#face_aging_demo1 = cv2.imread("media\DEMO_FACE_AGING.mp4")

#face_aging_demo1 = cv2.cvtColor(face_aging_demo1, cv2.COLOR_RGB2GRAY)

#face_aging_demo1 = Video(face_aging_demo1)

script = [0]*41


for i in range (0, 41):
    script[i] = pygame.image.load("script/script ({}).PNG".format(i+1))

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

def Buttonify(Picture, coords, surface):
    image = pygame.image.load(Picture)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image,imagerect)
    return (image,imagerect)

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

def video_player_dur(video, duration, cord = (make_center(FRAME256)[0], 200)):
    video.play(False)
        
    if video.current_time == duration:
        video.draw_to(screen, cord)
        video.pause()
    else:
        video.draw_to(screen, cord)

def video_player_dur_quar(video, duration, cordw = make_center(FRAME256)[0], cordh = 200):
    video1 = video; video2 = video; video3 = video

    #face_aging_demo.resume()

    video.play(False)
    video1.play(False)
    video2.play(False)
    video3.play(False)
        
    if video.current_time == duration:
        video.draw_to(screen, (cordw-128, cordh-128))
        video.pause()
    else:
        video.draw_to(screen, (cordw-128, cordh-128))

    if video1.current_time == duration:
        video1.draw_to(screen, (cordw+128, cordh-128))
        video1.pause()
    else:
        video1.draw_to(screen, (cordw+128, cordh-128))

    if video2.current_time == duration:
        video2.draw_to(screen, (cordw-128, cordh+128))
        video2.pause()
    else:
        video.draw_to(screen, (cordw-128, cordh+128))

    if video3.current_time == duration:
        video3.draw_to(screen, (cordw+128, cordh+128))
        video3.pause()
    else:
        video3.draw_to(screen, (cordw+128, cordh+128))

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

img_counter = 0

pause_cnt = 0

while not done:

    clock.tick(30)

    screen.fill(BLACK)

    # BUTTON_img = Buttonify('media\BUTTON_DEMO.png', (500, 900), screen)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     mouse = pygame.mouse.get_pos

        #     if BUTTON_img[1].collidepoint(mouse):
        #         img_name = "outputimg/opencv_frame_{}.png".format(img_counter)
        #         cv2.imwrite(img_name, cv2.cvtColor(np.rot90(frame, k = 3), cv2.COLOR_RGB2BGR))
        #         print("{} written!".format(img_name))
        #         img_counter += 1
            
        #     else: 
        #         pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            scene_counter += 1

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_0:
                # SPACE pressed
                img_name = "outputimg/opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, cv2.cvtColor(np.rot90(frame, k = 3), cv2.COLOR_RGB2BGR))
                print("{} written!".format(img_name))
                img_counter += 1


    if scene_counter == 0:
        draw_scene1()

    elif scene_counter == 1:
        screen.blit(script[0], (0, 0))

    elif scene_counter == 2:
        screen.blit(script[1], (0,0))

    elif scene_counter == 3:
        screen.blit(script[2], (0, 0))
        success, frame = cap.read()

        #frame = np.fliplr(frame)
        frame = np.rot90(frame)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        surf = pygame.surfarray.make_surface(frame)

        screen.blit(surf, (230,500))

        txt2 = ct(30, "Capture your face", WHITE)
        screen.blit(txt2, (make_center(txt2)[0], size_height - 300))

        #draw_scene2()
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

    elif scene_counter == 4:
        screen.blit(script[3], (0,0))
        draw_scene3()

    elif scene_counter == 5:
        screen.blit(script[4], (0,0))
        txt = ct(20, "SCENE4_STARTOFPART1", RED)
        screen.blit(txt, (make_center(txt)[0], 100))

    elif scene_counter == 6:
        screen.blit(script[5], (0,0))

        video_player_dur_quar(face_aging_demo, 1000.0)

        txt = ct(20, "SCENE5_PART1.1_1", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 7:
        screen.blit(script[6], (0,0))

        video_player_dur_quar(face_aging_demo, 1000.0)

        txt = ct(20, "SCENE5_PART1.1_2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))


    elif scene_counter == 8:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))

        if  pause_cnt == 0:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 2000.0)

        #pygame.draw.line(screen, BLACK, [make_center(FRAME256)[0]+128, 0], [make_center(FRAME256)[0]+128, 1080], 5)
        #pygame.draw.line(screen, BLACK, [0, make_center(FRAME256)[0]-100], [1080, make_center(FRAME256)[0]-100], 5)

        txt = ct(20, "SCENE6_PART1.2", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 8:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))

        if  pause_cnt == 1:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 3000.0)
        
        txt = ct(20, "SCENE7_PART1.3", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 9:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))

        if  pause_cnt == 2:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 4000.0)

        txt = ct(20, "SCENE8_PART1.4", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 10:
        screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        screen.blit(FACE2, (make_center(FACE2)[0], 200))

        if  pause_cnt == 3:
            print("resres")
            pause_cnt += 1
            face_aging_demo.resume()
        else:
            pass

        video_player_dur_quar(face_aging_demo, 5000.0)

        txt = ct(20, "SCENE9_PART1.5", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 11:
        OLDTV = pygame.transform.scale(OLDTV, (800, 800))
        
        screen.blit(OLDTV, (make_center(OLDTV)[0], 0))

        txt = ct(20, "SCENE10_STARTOFPART2", RED)
        screen.blit(txt, (make_center(txt)[0], 100))

    elif scene_counter == 12:
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

        #OLDTV = pygame.transform.scale(OLDTV, (1000, 1000))
        
        #screen.blit(OLDTV, (make_center(OLDTV)[0], 100))

        #screen.fill(BLACK)

        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE11_ZOOMOUT", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 13:
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

        video_demo.play(loop=False)
        video_demo.draw_to(screen, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE12_PART2.1_mario", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 14:
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))

        part2_tetris.play(loop=False)
        part2_tetris.draw_to(screen, (make_center(FRAME256)[0] - 110, 200))

        glitch.play(True)
        #glitch.draw_to(screen, (make_center(FRAME256)[0] - 127, 180))

        if part2_tetris.current_time == 11000.0:
            part2_tetris.pause()
            glitch.play(True)
            glitch.draw_to(screen, (make_center(FRAME256)[0] - 127, 180))
            #glitch.pause()
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE13_PART2.2_tetris", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 15:
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE14_PART2.3_chess", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 16:
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE15_PART2.4_bomber", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 17:
        #screen.blit(FRAME256, (make_center(FRAME256)[0], 200))
        
        bob_video_demo.play()
        bob_video_demo.draw_to(screen, (make_center(FRAME256)[0], 200))
        
        OLDTV = pygame.transform.scale(OLDTV, (500, 500))

        screen.blit(OLDTV, (make_center(OLDTV)[0], 100))
        txt = ct(20, "SCENE16_PART2.5", RED)
        screen.blit(txt, (make_center(txt)[0], 500))

    elif scene_counter == 18:
        txt = ct(20, "SCENE17_ENDING", RED)
        screen.blit(txt, (make_center(txt)[0], 100))

    elif scene_counter > 19:
        #done=True #주석 처리 지울 시 프로그램 종료
        scene_counter = 0

    pygame.display.update()

pygame.QUIT