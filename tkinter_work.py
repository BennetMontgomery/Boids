from tkinter import *
import boids
import random

grid = []
grid_size = 100


def init_boids():
    boid_list = []
    for i in range(10):
        vals = []
        pos = []
        for j in range(2):
            pos.append(random.randrange(200, 300))
        for j in range(2):
            vals.append(random.randrange(-1, 1))
        boid_list.append(boids.Boid((pos[0], pos[1]), (vals[0], vals[1])))
    return boid_list


def main():
    boid_list = init_boids()

    root = Tk()
    title = Label(root, text='Boids Simulation')
    title.pack()
    img = PhotoImage(file='arrow.png')

    tweet_list = []
    c = Canvas(master=root, width=1000, height=800)
    for i in range(len(boid_list)):
        tweet_list.append(c.create_image(boid_list[i].getPosition()[0], boid_list[i].getPosition()[1], anchor=NW, image=img))

    def keypress(event):
        if event.char== 'a':
            print("h")
            print(boid_list[0].getPosition())
            boids.move_all_boids_to_new_positions(boid_list)
            print(boid_list[0].getPosition())
            for i in range(len(boid_list)):
                c.move(tweet_list[i], boid_list[i].getVelocity()[0], boid_list[i].getVelocity()[1])

    c.pack()

    # def move_tweets():
    #     boids.move_all_boids_to_new_positions(boid_list)
    #     for i in range(len(boid_list)):
    #         c.move(tweet_list[i], boid_list[i].getPosition()[0], boid_list[i].getPosition()[1])
    #     c.after(10, move_tweets())
    # move_tweets()
    # seems to have an issue?

    root.bind("<Key>", keypress)

    root.mainloop()


if __name__ == '__main__':
    main()
