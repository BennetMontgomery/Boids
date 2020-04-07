import math
import random
import time
from tkinter import *

'''
    Boids implementation for assignment 3

    Bennet Montgomery
    Daniel Oh
    Spencer Dallas
    Shreyansh Anand
    Evelyn Yach
'''


class Boid:
    def __init__(self, position, initv):
        """
        Constructor for Boid class

        :param position: tuple containing the initial x and y coordinate of the boid
        :param initv: tuple containing the initial x movement and y movement per tick of the boid
        """

        self.position = position
        self.vel = initv

    def setVelocity(self, newvel):
        self.vel = newvel

    def getVelocity(self):
        return self.vel

    def setPosition(self, newpos):
        self.position = newpos

    def getPosition(self):
        return self.position


def rule1(b, boids):
    """
    Rule 1 implementation of CR's rules

    :param b: boid to apply rule to
    :param boids: other boids in system
    :return: rule 1 vector as tuple of x and y movement
    """

    pcjx = 0
    pcjy = 0
    numboidsnearby = 1

    for boid in boids:
        xdiff = boid.getPosition()[0] - b.getPosition()[0]
        ydiff = boid.getPosition()[1] - b.getPosition()[1]

        if math.sqrt((xdiff ** 2) + (ydiff ** 2)) < 100:
            pcjx += boid.getPosition()[0]
            pcjy += boid.getPosition()[1]
            numboidsnearby += 1

    # pcjx = ((pcjx / (len(boids) - 1)) - b.getPosition()[0]) / 100
    # pcjy = ((pcjy / (len(boids) - 1)) - b.getPosition()[1]) / 100
    pcjx /= len(boids)-1
    pcjy /= len(boids)-1

    pcjx -= b.getPosition()[0]
    pcjy -= b.getPosition()[1]

    pcjx /= numboidsnearby
    pcjy /= numboidsnearby

    return pcjx, pcjy


def rule2(b, boids):
    """
    Rule 2 implementation of CR's rules

    :param b: boid to apply rule to
    :param boids: other boids in system
    :return: rule 2 vector as tuple of x and y movement
    """

    cx = 0
    cy = 0

    for boid in boids:
        if boid != b:
            xdiff = boid.getPosition()[0] - b.getPosition()[0]
            ydiff = boid.getPosition()[1] - b.getPosition()[1]

            if math.sqrt((xdiff ** 2) + (ydiff ** 2)) < 100:
                cx -= xdiff
                cy -= ydiff

    return cx, cy


def rule3(b, boids):
    """
    Rule 3 implementation of CR's rules

    :param b: boid to apply rule to
    :param boids: other boids in system
    :return: rule 3 vector as tuple of x and y movement
    """
    pvjx = 0
    pvjy = 0

    for boid in boids:
        if boid != b:
            pvjx += boid.getVelocity()[0]
            pvjy += boid.getVelocity()[1]

    pvjx /= (len(boids) - 1)
    pvjy /= (len(boids) - 1)

    pvjx = (pvjx - b.getVelocity()[0]) / 8
    pvjy = (pvjy - b.getVelocity()[1]) / 8

    return pvjx, pvjy


def move_all_boids_to_new_positions(boids):
    """
    Moves passed list of boids by applying all three of Craig Reynold's rules simultaneously

    :param boids: list of boids to move
    :return: void
    """
    for boid in boids:
        v1 = rule1(boid, boids)
        v2 = rule2(boid, boids)
        v3 = rule3(boid, boids)

        newvelx = (boid.getVelocity()[0] + v1[0] + v2[0] + v3[0]) / 10
        newvely = (boid.getVelocity()[1] + v1[1] + v2[1] + v3[1]) / 10

        boid.setVelocity((newvelx, newvely))

        newposx = boid.getPosition()[0] + boid.getVelocity()[0]
        newposy = boid.getPosition()[1] + boid.getVelocity()[1]

        boid.setPosition((newposx, newposy))

    return


def init_boids():
    """
    initializes the boids list
    :return: a list of boids
    """
    boid_list = []
    # the following for loop places all the boids initially on the grid
    # to change the number of boids, simply change the for loop condition
    for i in range(50):
        vals = []
        pos = []
        # the following two for loops were used to randomly create the necessary init vals for the boids
        for j in range(2):
            pos.append(random.randrange(305, 455))
        for j in range(2):
            vals.append(random.randrange(-100, 100))
        boid_list.append(Boid((pos[0], pos[1]), (vals[0], vals[1])))
    return boid_list


def main():
    """
    main function where all the simulation happens.
    """
    # inits the boids list
    boid_list = init_boids()

    # creating the tkinter window
    root = Tk()
    title = Label(root, text='Boids Simulation')
    title.pack()
    img = PhotoImage(file='arrow.png')
    board_height = 700
    board_width = 700
    tweet_list = []
    c = Canvas(master=root, width=board_width, height=board_height, bg="black")
    # initializing the tkinter window with the boids list
    for i in range(len(boid_list)):
        tweet_list.append(
            c.create_image(boid_list[i].getPosition()[0], boid_list[i].getPosition()[1], anchor=NW, image=img))
    c.pack()

    # the following loop is what displays how the boids move around the screen
    while True:
        move_all_boids_to_new_positions(boid_list)

        for i in range(len(boid_list)):
            pos = boid_list[i].getPosition()
            if pos[0] > board_height:
                boid_list[i].setPosition((0, pos[1]))
                c.coords(tweet_list[i], (0, pos[1]))
            if pos[1] > board_width:
                boid_list[i].setPosition((pos[0], 0))
                c.coords(tweet_list[i], (pos[0], 0))
            if pos[1] < 0:
                boid_list[i].setPosition((pos[0], board_width))
                c.coords(tweet_list[i], (pos[0], board_width))
            if pos[0] < 0:
                boid_list[i].setPosition((board_height, pos[1]))
                c.coords(tweet_list[i], (board_height, pos[1]))
            c.move(tweet_list[i], boid_list[i].getVelocity()[0], boid_list[i].getVelocity()[1])

        c.update()
        time.sleep(0.025)

    root.mainloop()


if __name__ == '__main__':
    main()
