from pygame import *
from pygame import movie

width, height = 800, 600
screen = display.set_mode((width, height))
red = (255, 0, 0)
gray = (127, 127, 127)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
bg = (50, 62, 79)

#open stats---------------------------------------------------------------------
open("stats.txt", "r")

##RECTANGLES--------------------------------------------------------------------
LeBron_JamesPick = Rect(50, 125, 175, 140)
Kawhi_LeonardPick = Rect(50, 350, 175, 140)
Stephen_CurryPick = Rect(300, 125, 175, 140)
Nikola_JokicPick = Rect(300, 350, 175, 140)
GiannisPick = Rect(550, 125, 175, 140)
Kevin_DurantPick = Rect(550, 350, 175, 140)

Luka_DoncicPick = Rect(50, 125, 175, 140)
Russell_WestbrookPick = Rect(50, 350, 175, 140)
Jayson_TatumPick = Rect(300, 125, 175, 140)
Zach_LavinePick = Rect(300, 350, 175, 140)
James_HardenPick = Rect(550, 125, 175, 140)
Zion_WilliamsonPick = Rect(550, 350, 175, 140)

Bradley_BealPick = Rect(50, 125, 175, 140)
Trae_YoungPick = Rect(50, 350, 175, 140)
Joel_EmbiidPick = Rect(300, 125, 175, 140)
Ben_SimmonsPick = Rect(300, 350, 175, 140)
Julius_RandlePick = Rect(550, 125, 175, 140)
Kyle_LowryPick = Rect(550, 350, 175, 140)

Devin_BookerPick = Rect(50, 125, 175, 140)
Kristaps_PorzingisPick = Rect(50, 350, 175, 140)
Myles_TurnerPick = Rect(300, 125, 175, 140)
CJ_McCollumPick = Rect(300, 350, 175, 140)
Jaylen_BrownPick = Rect(550, 125, 175, 140)
Kyrie_IrvingPick = Rect(550, 350, 175, 140)

Donovan_MitchellPick = Rect(50, 125, 175, 140)
Anthony_DavisPick = Rect(50, 350, 175, 140)
Kemba_WalkerPick = Rect(300, 125, 175, 140)
Jerami_GrantPick = Rect(300, 350, 175, 140)
Pascal_SiakamPick = Rect(550, 125, 175, 140)
Paul_GeorgePick = Rect(550, 350, 175, 140)


## loading pics for picks
# picNames=["WinHacks.py/Pics/lebron.png", "WinHacks.py/Pics/kawhi.png",
#           "WinHacks.py/Pics/curry.png", "WinHacks.py/Pics/jokic.png",
#           "WinHacks.py/Pics/giannis.png", "WinHacks.py/Pics/durant.png",
#
#           "WinHacks.py/Pics/luka.png", "WinHacks.py/Pics/westbrook.png",
#           "WinHacks.py/Pics/tatum.png", "WinHacks.py/Pics/zach.png",
#           "WinHacks.py/Pics/harden.png", "WinHacks.py/Pics/zion.png",
#
#           "WinHacks.py/Pics/beal.png", "WinHacks.py/Pics/trae.png",
#           "WinHacks.py/Pics/embiid.png", "WinHacks.py/Pics/ben.png",
#           "WinHacks.py/Pics/randle.png", "WinHacks.py/Pics/lowry.png",
#
#           "WinHacks.py/Pics/booker.png", "WinHacks.py/Pics/porzingis.png",
#           "WinHacks.py/Pics/turner.png", "WinHacks.py/Pics/CJ.png",
#           "WinHacks.py/Pics/brown.png", "WinHacks.py/Pics/kyrie.png",
#
#           "WinHacks.py/Pics/donovan.png", "WinHacks.py/Pics/davis.png",
#           "WinHacks.py/Pics/kemba.png", "WinHacks.py/Pics/grant.png",
#           "WinHacks.py/Pics/siakam.png", "WinHacks.py/Pics/pg.png"]

picNames = ["Pics/lebron.png", "Pics/kawhi.png",
          "Pics/curry.png", "Pics/jokic.png",
          "Pics/giannis.png", "Pics/durant.png",

          "Pics/luka.png", "Pics/westbrook.png",
          "Pics/tatum.png", "Pics/zach.png",
          "Pics/harden.png", "Pics/zion.png",

          "Pics/beal.png", "Pics/trae.png",
          "Pics/embiid.png", "Pics/ben.png",
          "Pics/randle.png", "Pics/lowry.png",

          "Pics/booker.png", "Pics/porzingis.png",
          "Pics/turner.png", "Pics/CJ.png",
          "Pics/brown.png", "Pics/kyrie.png",

          "Pics/donovan.png", "Pics/davis.png",
          "Pics/kemba.png", "Pics/grant.png",
          "Pics/siakam.png", "Pics/pg.png"]

myPicList = []
for name in picNames:
    pic = image.load(name)    #loading only one picture
    picc = transform.smoothscale(pic, (175, 140))
    myPicList.append(picc)

rectList1 = [LeBron_JamesPick, Kawhi_LeonardPick, Stephen_CurryPick,
            Nikola_JokicPick, GiannisPick, Kevin_DurantPick]

rectList2 = [Luka_DoncicPick, Russell_WestbrookPick, Jayson_TatumPick,
            Zach_LavinePick, James_HardenPick, Zion_WilliamsonPick]

rectList3 = [Bradley_BealPick, Trae_YoungPick, Joel_EmbiidPick,
            Ben_SimmonsPick, Julius_RandlePick, Kyle_LowryPick]

rectList4 = [Devin_BookerPick, Kristaps_PorzingisPick, Myles_TurnerPick,
            CJ_McCollumPick, Jaylen_BrownPick, Kyrie_IrvingPick]

rectList5 = [Donovan_MitchellPick, Anthony_DavisPick, Kemba_WalkerPick,
            Jerami_GrantPick, Pascal_SiakamPick, Paul_GeorgePick]

screen.fill(bg)
P1Team = []
P2Team = []
count = 0
menu = 'p1pick1'

def p1pick1():
    for rect in rectList1:
        draw.rect(screen, white, rect, 1)
        #draw.rect(screen,black,rect,1)
        if rect.collidepoint(mx,my):
            draw.rect(screen, gray, rect, 3)         #highlights the tool rects if the mouse hovers over
        #blitting the text box in accordance with the tool
            # if mb[0] == 1:
            #     return p1pick2()
        else:
            draw.rect(screen, white, rect, 3)

    screen.blit(myPicList[0], LeBron_JamesPick)
    screen.blit(myPicList[1], Kawhi_LeonardPick)
    screen.blit(myPicList[2], Stephen_CurryPick)
    screen.blit(myPicList[3], Nikola_JokicPick)
    screen.blit(myPicList[4], GiannisPick)
    screen.blit(myPicList[5], Kevin_DurantPick)

def p1pick2():
    for rect in rectList2:
        draw.rect(screen, white, rect, 1)
        #draw.rect(screen,black,rect,1)
        if rect.collidepoint(mx,my):
            draw.rect(screen, gray, rect, 3)         #highlights the tool rects if the mouse hovers over
        #blitting the text box in accordance with the tool
        else:
            draw.rect(screen, white, rect, 3)

    screen.blit(myPicList[6], Luka_DoncicPick)
    screen.blit(myPicList[7], Russell_WestbrookPick)
    screen.blit(myPicList[8], Jayson_TatumPick)
    screen.blit(myPicList[9], Zach_LavinePick)
    screen.blit(myPicList[10], James_HardenPick)
    screen.blit(myPicList[11], Zion_WilliamsonPick)

def p1pick3():
    for rect in rectList1:
        draw.rect(screen, white, rect, 1)
        # draw.rect(screen,black,rect,1)
        if rect.collidepoint(mx, my):
            draw.rect(screen, gray, rect, 3)  # highlights the tool rects if the mouse hovers over
        # blitting the text box in accordance with the tool
        # if mb[0] == 1:
        #     return p1pick2()
        else:
            draw.rect(screen, white, rect, 3)

    screen.blit(myPicList[12], Bradley_BealPick)
    screen.blit(myPicList[13], Trae_YoungPick)
    screen.blit(myPicList[14], Joel_EmbiidPick)
    screen.blit(myPicList[15], Ben_SimmonsPick)
    screen.blit(myPicList[16], Julius_RandlePick)
    screen.blit(myPicList[17], Kyle_LowryPick)

def p1pick4():
    for rect in rectList1:
        draw.rect(screen, white, rect, 1)
        # draw.rect(screen,black,rect,1)
        if rect.collidepoint(mx, my):
            draw.rect(screen, gray, rect, 3)  # highlights the tool rects if the mouse hovers over
        # blitting the text box in accordance with the tool
        # if mb[0] == 1:
        #     return p1pick2()
        else:
            draw.rect(screen, white, rect, 3)

    screen.blit(myPicList[18], Devin_BookerPick)
    screen.blit(myPicList[19], Kristaps_PorzingisPick)
    screen.blit(myPicList[20], Myles_TurnerPick)
    screen.blit(myPicList[21], CJ_McCollumPick)
    screen.blit(myPicList[22], Jaylen_BrownPick)
    screen.blit(myPicList[23], Kyrie_IrvingPick)

def p1pick5():
    for rect in rectList1:
        draw.rect(screen, white, rect, 1)
        # draw.rect(screen,black,rect,1)
        if rect.collidepoint(mx, my):
            draw.rect(screen, gray, rect, 3)  # highlights the tool rects if the mouse hovers over
        # blitting the text box in accordance with the tool
        # if mb[0] == 1:
        #     return p1pick2()
        else:
            draw.rect(screen, white, rect, 3)

    screen.blit(myPicList[24], Donovan_MitchellPick)
    screen.blit(myPicList[25], Anthony_DavisPick)
    screen.blit(myPicList[26], Kemba_WalkerPick)
    screen.blit(myPicList[27], Jerami_GrantPick)
    screen.blit(myPicList[28], Pascal_SiakamPick)
    screen.blit(myPicList[29], Paul_GeorgePick)

    # for rect in rectList1:
    #     if rect.collidepoint(mx, my):
    #         screen.fill(bg)
    #         screen.blit(myPicList[6], p2Select1)
    #         screen.blit(myPicList[7], p2Select2)
    #         screen.blit(myPicList[8], p2Select3)
    #         screen.blit(myPicList[9], p2Select4)
    #         screen.blit(myPicList[10], p2Select5)
    #         screen.blit(myPicList[11], p2Select6)


running = True

while running:
    print(menu)
    screen.fill(bg)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    for evt in event.get():
        for rect in rectList1:
            if rect.collidepoint(mx, my) and evt.type == MOUSEBUTTONUP:
                if menu == 'p1pick1':
                    menu = 'p1pick2'

                if menu == 'p1pick2':
                    menu = 'p1pick3'

                if menu == 'p1pick3':
                    menu = 'p1pick4'

                if menu == 'p1pick4':
                    menu = 'p1pick5'

                # if menu == 'p1pick5':
                #     menu = 'p1team review'

        if evt.type == QUIT:
            running = False
    if menu == 'intro':
        intro()
    if menu == 'instructions':
        instructions()
    if menu == 'p1pick1':
        p1pick1()
    if menu == 'p1pick2':
        p1pick2()
    if menu == 'p1pick3':
        p1pick3()
    if menu == 'p1pick4':
        p1pick4()
    if menu == 'p1pick5':
        p1pick5()
    if menu == 'p1team review':
        p1teamreview()

    if menu == 'p2pick1':
        p2pick1()
    if menu == 'p2pick2':
        p2pick2()
    if menu == 'p2pick3':
        p2pick3()
    if menu == 'p2pick4':
        p2pick4()
    if menu == 'p2pick5':
        p2pick5()
    if menu == 'team review':
        teamReview()
    if menu == 'Results':
        results()
    # for rect in rectList2:
    #     if rect.collidepoint(mx, my) and mb[0] == 1:
    #         screen.fill(bg)
    #         screen.blit(myPicList[12], p3Select1)
    #         screen.blit(myPicList[13], p3Select2)
    #         screen.blit(myPicList[14], p3Select3)
    #         screen.blit(myPicList[15], p3Select4)
    #         screen.blit(myPicList[16], p3Select5)
    #         screen.blit(myPicList[17], p3Select6)

    display.flip()

quit()
