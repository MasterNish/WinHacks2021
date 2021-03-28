from pygame import *

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

##RECTANGLES--------------------------------------------------------------------
p1Select1 = Rect(50, 125, 175, 140)
p1Select2 = Rect(50, 350, 175, 140)
p1Select3 = Rect(300, 125, 175, 140)
p1Select4 = Rect(300, 350, 175, 140)
p1Select5 = Rect(550, 125, 175, 140)
p1Select6 = Rect(550, 350, 175, 140)

p2Select1 = Rect(50, 125, 175, 140)
p2Select2 = Rect(50, 350, 175, 140)
p2Select3 = Rect(300, 125, 175, 140)
p2Select4 = Rect(300, 350, 175, 140)
p2Select5 = Rect(550, 125, 175, 140)
p2Select6 = Rect(550, 350, 175, 140)

p3Select1 = Rect(50, 125, 175, 140)
p3Select2 = Rect(50, 350, 175, 140)
p3Select3 = Rect(300, 125, 175, 140)
p3Select4 = Rect(300, 350, 175, 140)
p3Select5 = Rect(550, 125, 175, 140)
p3Select6 = Rect(550, 350, 175, 140)

p4Select1 = Rect(50, 125, 175, 140)
p4Select2 = Rect(50, 350, 175, 140)
p4Select3 = Rect(300, 125, 175, 140)
p4Select4 = Rect(300, 350, 175, 140)
p4Select5 = Rect(550, 125, 175, 140)
p4Select6 = Rect(550, 350, 175, 140)

p5Select1 = Rect(50, 125, 175, 140)
p5Select2 = Rect(50, 350, 175, 140)
p5Select3 = Rect(300, 125, 175, 140)
p5Select4 = Rect(300, 350, 175, 140)
p5Select5 = Rect(550, 125, 175, 140)
p5Select6 = Rect(550, 350, 175, 140)


## loading pics for pick 1
picNames=["Pics/lebron.png", "Pics/kawhi.png",
          "Pics/curry.png", "Pics/jokic.png",
          "Pics/giannis.png", "Pics/durant.png",
          "Pics/luka.png", "Pics/westbrook.png",
          "Pics/tatum.png", "Pics/zach.png",
          "Pics/harden.png", "Pics/zion.png",
          "Pics/beal.png", "Pics/trae.png",
          "Pics/embiid.png", "Pics/ben.png",
          "Pics/randle.png", "Pics/lowry.png",]

myPicList = []
for name in picNames:
    pic = image.load(name)    #loading only one picture
    picc = transform.smoothscale(pic, (175, 140))
    myPicList.append(picc)

rectList1 = [p1Select1, p1Select2, p1Select3,
            p1Select4, p1Select5, p1Select6]

rectList2 = [p2Select1, p2Select2, p2Select3,
            p2Select4, p2Select5, p2Select6]

rectList3 = [p3Select1, p3Select2, p3Select3,
            p3Select4, p3Select5, p3Select6]

rectList4 = [p4Select1, p4Select2, p4Select3,
            p4Select4, p4Select5, p4Select6]

rectList5 = [p5Select1, p5Select2, p5Select3,
            p5Select4, p5Select5, p5Select6]

screen.fill(bg)
screen.blit(myPicList[0], p1Select1)
screen.blit(myPicList[1], p1Select2)
screen.blit(myPicList[2], p1Select3)
screen.blit(myPicList[3], p1Select4)
screen.blit(myPicList[4], p1Select5)
screen.blit(myPicList[5], p1Select6)

count = 0

running = True

while running:

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    for evt in event.get():
        if evt.type == QUIT:
            running = False

    for rect in rectList1:
        draw.rect(screen, white, rect, 1)
        #draw.rect(screen,black,rect,1)
        if rect.collidepoint(mx,my):
            draw.rect(screen, gray, rect, 3)         #highlights the tool rects if the mouse hovers over
        #blitting the text box in accordance with the tool
        else:
            draw.rect(screen, white, rect, 3)

    for rect in rectList1:
        if rect.collidepoint(mx, my):
            screen.fill(bg)
            screen.blit(myPicList[6], p2Select1)
            screen.blit(myPicList[7], p2Select2)
            screen.blit(myPicList[8], p2Select3)
            screen.blit(myPicList[9], p2Select4)
            screen.blit(myPicList[10], p2Select5)
            screen.blit(myPicList[11], p2Select6)

    for rect in rectList2:
        if rect.collidepoint(mx, my) and mb[0] == 1:
            screen.fill(bg)
            screen.blit(myPicList[12], p3Select1)
            screen.blit(myPicList[13], p3Select2)
            screen.blit(myPicList[14], p3Select3)
            screen.blit(myPicList[15], p3Select4)
            screen.blit(myPicList[16], p3Select5)
            screen.blit(myPicList[17], p3Select6)
    print(count)

    display.flip()

quit()
