from tkinter import *
import boids
import random
import time


def init_boids():
    """
    initializes the boids list
    :return: a list of boids
    """
    boid_list = []
    # the following for loop places all the boids initially on the grid
    # to change the number of boids, simply change the for loop condition
    for i in range(150):
        vals = []
        pos = []
        # the following two for loops were used to randomly create the necessary init vals for the boids
        for j in range(2):
            pos.append(random.randrange(305, 455))
        for j in range(2):
            vals.append(random.randrange(-1, 1))
        boid_list.append(boids.Boid((pos[0], pos[1]), (vals[0], vals[1])))
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
    img = PhotoImage(file='tweet.png')

    tweet_list = []
    c = Canvas(master=root, width=1000, height=800)
    # initializing the tkinter window with the boids list
    for i in range(len(boid_list)):
        tweet_list.append(c.create_image(boid_list[i].getPosition()[0], boid_list[i].getPosition()[1], anchor=NW, image=img))
    c.pack()

    # the following loop is what displays how the boids move around the screen
    while True:
        boids.move_all_boids_to_new_positions(boid_list)
        time.sleep(0.025)
        for i in range(len(boid_list)):
            c.move(tweet_list[i], boid_list[i].getVelocity()[0], boid_list[i].getVelocity()[1])

        c.update()

    root.mainloop()


if __name__ == '__main__':
    main()
