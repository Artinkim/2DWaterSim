import time
grid = []
size = 20,20
for i in range (size[0]):
    new = []
    for j in range (size[1]):
        new.append(0)
    grid.append(new)

def clearGrid():
    for i in range (size[0]):
        for j in range (size[1]):
            grid[i][j] = 0



def displayGrid():
    print()
    print()
    for i in range (size[0]-1,-1,-1):
        s = ""
        for j in range (size[1]):
            s+=str(grid[j][i])+""
        print(s)


def render(angle):
    #print(angle)
    water = 1
    height = 20
    width = 20
    angle%=360
    an = angle
    if (angle <90 and angle>=0) or (angle <270 and angle>=180):
        angle%=90
        p1 = 0,int(height*(angle/90))
        p2 = width-1,int(height-height*(angle/90))
        if p2[1]==p1[1]:
            slope = 0
        else:
            slope =(p2[1]-p1[1])/(p2[0]-p1[0])
        #print(slope)
        for i in range(0,width):
            #print(p1[1]+int(i*slope))
            for j in range(0,p1[1]+int(i*slope)):
                if(an <90 and an>=0):
                    grid[i][j] = water
                else:
                    grid[height-i-1][height-j-1] = water
    else:
        angle%=90
        angle = 90-angle
        p1 = int(width*(angle/90)),0
        p2 = int(width-width*(angle/90)),height-1
        #print(p1,p2)
        if p2[0]==p1[0]:
            slope = 0
        else:
            slope =(p2[0]-p1[0])/(p2[1]-p1[1])
        #print(slope)
        for i in range(0,height):
            #print(p1[1]+int(i*slope))
            for j in range(0,p1[0]+int(i*slope)):
                if(an <180 and an>=90):
                    grid[j][i] = water
                else:
                    grid[height-j-1][height-i-1] = water
    # p1 = 0,5
    # p2 = 19,10
    #print(p1,p2)

    # grid[p1[0]][p1[1]] = 3
    # grid[p2[0]][p2[1]] = 4


    # for j in range(p1[1]):
    #     print(int(p1[0]+slope*j))
    #     for i in range(p1[0]+int(slope*j)):
    #

acceleration = 0.4
velocity = 0
angle = 0
friction = .02
import keyboard  # using module keyboard
while True:  # making a loop
    time.sleep(0.005)
    render(angle)
    angle +=velocity
    velocity-=velocity*friction
    displayGrid()
    clearGrid()
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            velocity+=acceleration
              # finishing the loop
        if keyboard.is_pressed('e'):
            velocity-=acceleration
    except:
         pass # if user pressed a key other than the given key the loop will break




# def display(angle,width,height):
#     angle = angle%360
#     if angle <=45:
#         p1 = 0,(height/2)+(height/2)*(angle/45)
#         p2 = width-1,(height/2)-(height/2)*(angle/45)
#         if p2[1]==int(p1[1]):
#             slope = -999999
#         else:
#             slope =(p2[0]-p1[0])/(p2[1]-p1[1])
#         for j in range(p1[1]):
#             for i in range(p1[1]+slope*j):
#                 grid[j][i] = 1
#     else if angle <=180:
#
#     else if angle <=270:
#
#     else:










# # count = 0
# # dx = [1,-1,0,0]
# # dy = [0,0,-1,1]
# #
# # def bfs(x,y):
# #     queue = []
# #     queue.append((x,y))
# #     while len(queue) >0:
# #         x,y = queue.pop(0)
# #         print(x,y)
# #         grid[x][y] = 1
# #         # if x<0 or y<0 or x>len(grid) or x>len(grid[0]):
# #         #     return
# #         for i in range(4):
# #             tx = x+dx[i]
# #             ty = y+dy[i]
# #             displayGrid()
# #             if tx<0 or ty<0 or tx>len(grid) or tx>len(grid[0]):
# #                 continue
# #             if grid[tx][ty] or count>50:
# #                 continue
# #             queue.append((tx,ty))
#
# def render():
#     point1 = 4,10
#     point2 = 19,15
#     if point1[1]<point2[1]:
#         tmp = point1[0],point1[1]
#         point1 = point2[0],point2[1]
#         point2 = tmp
#
#
#
#
#
#     b = len(grid)//2
#
#     #print(point2[1],point1[1])
#     if point2[1]==int(point1[1]):
#         slope = -999999
#     else:
#         slope =(point2[0]-point1[0])/(point2[1]-point1[1])
#
#     print(slope)
#     for i in range(max(point1[1]+1,point2[1]+1)):
#         #print(min(20,int(point1[0]-(slope*(point1[1]-i)))))
#         for j in range(point1[0],min(20,int(point1[0]-(slope*(point1[1]-i))))):
#             grid[j][i] = 1
#     grid[point1[0]][point1[1]] =3
#     grid[point2[0]][point2[1]] =4
#     # grid[0][19] = 6
#     grid[0][0] = 7
#
# #def render():
#     #for i in range():
#
#
#
#
# #def calculateStart(angle):
#
#
