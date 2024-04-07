import turtle as tl
from turtle import Screen

tl.colormode(255)
screen = Screen()
screen.setup(1000, 1000)
canvas = screen.getcanvas()
cnt = 0
running = True
xlist = [[]]
ylist = [[]]
dlist = [[]]
tl.home()
tl.speed("fastest")
tl.color("black")
tl.width(1)

def grid():
    for a in range(20):
        tl.up()
        tl.goto(-500, 500-a*50)
        tl.down()
        tl.forward(1000)

    tl.right(90)

    for b in range(20):
        tl.up()
        tl.goto(-500+b*50, 500)
        tl.down()
        tl.forward(1000)

    tl.up()
    tl.left(90)
    tl.goto(-500, 90)
    tl.width(10)
    tl.color("red")
    tl.down()
    tl.forward(700)
    tl.right(30)
    tl.forward(300)
    tl.left(30)
    tl.forward(275)
    tl.up()
    tl.goto(-500, -40)
    tl.down()
    tl.forward(700)
    tl.right(30)
    tl.forward(300)
    tl.left(30)
    tl.forward(275)
    tl.up()
    tl.width(2)

def point(x, y):
    global cnt
    x_local = []
    y_local = []
    for a in range(3):
        tl.goto(x, y)
        tl.down()
        while True:
            overlapping = canvas.find_overlapping(tl.xcor(), -tl.ycor(), tl.xcor(), -tl.ycor())
            color = canvas.itemcget(overlapping[0], "fill")
            if abs(tl.xcor()) >= 500 or abs(tl.ycor()) >= 500:
                break
            if color != "red":
                tl.forward(1)
            if overlapping:
                if color == "red":
                    break
                if tl.distance(x, y) > 20:
                    if color == "black" and color != "red" and color != "orange":
                        if color == "red":
                            break
                        dist = ((tl.xcor() - x)**2 + (tl.ycor() - y)**2) ** (1 / 2)
                        sum_dist = dist
                        if len(dlist) > 1:
                            if len(dlist[cnt-1]) < a + 1:
                                dlist[cnt-1].append(dlist[cnt-1][0])
                            if dlist[cnt-1][a] < dlist[cnt-1][0]:
                                dlist[cnt-1][a] = dlist[cnt-1][0]
                            sum_dist = sum_dist + dlist[cnt-1][a]
                        dlist[cnt].append(round(sum_dist))
                        x_local.append(tl.xcor())
                        y_local.append(tl.ycor())
                        break
                elif tl.distance(x, y) <= 20:
                        if color == "black":
                            dlist[cnt-1].append(dlist[cnt-1][0])
                if color == "black":
                    if len(dlist[cnt-1]) < a + 1:
                        dlist[cnt-1].append(dlist[cnt-1][0])
        tl.up()
        tl.right(120)
        if round(tl.xcor()) / 350 > 1:
            print("\nLocated. Distance:", dlist[cnt-1][a] + ((tl.xcor() - x)**2 + (tl.ycor() - y)**2) ** (1 / 2))
            running = False
            break
    if x_local != [] and y_local != 0:
        xlist[cnt].append(x_local)
        ylist[cnt].append(y_local)

#main
if __name__ == "__main__":
    grid()
    tl.color("orange")
    point(-375, 25)
    cnt = cnt + 1
    while running == True:
        if len(xlist) < cnt+1:
            xlist.append([])
            ylist.append([])
            dlist.append([])
        for x in range(len(xlist[cnt-1])):
            for a in range(len(xlist[cnt-1][x])):
                if a > 0:
                    if xlist[cnt-1][x][a-1] - xlist[cnt-1][x][a] > 40 and ylist[cnt-1][x][a-1] - ylist[cnt-1][x][a] > 40:
                        point(xlist[cnt-1][x][a], ylist[cnt-1][x][a])
                elif a == 0:
                    point(xlist[cnt - 1][x][a], ylist[cnt - 1][x][a])
            if running == False:
                break
        cnt = cnt + 1