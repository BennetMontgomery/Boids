import math

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
        '''
        Constructor for Boid class

        :param position: tuple containing the initial x and y coordinate of the boid
        :param initv: tuple containing the initial x movement and y movement per tick of the boid
        '''

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
    '''
    Rule 1 implementation of CR's rules

    :param b: boid to apply rule to
    :param boids: other boids in system
    :return: rule 1 vector as tuple of x and y movement
    '''

    pcjx = 0
    pcjy = 0

    for boid in boids:
        if b != boid:
            pcjx += boid.getPosition()[0]
            pcjy += boid.getPosition()[1]

    pcjx = ((pcjx/(len(boids) - 1)) - b.getPosition()[0])/100
    pcjy = ((pcjy/(len(boids) - 1)) - b.getPosition()[1])/100

    return pcjx, pcjy


def rule2(b, boids):
    '''
    Rule 2 implementation of CR's rules

    :param b: boid to apply rule to
    :param boids: other boids in system
    :return: rule 2 vector as tuple of x and y movement
    '''

    cx = 0
    cy = 0

    for boid in boids:
        if boid != b:
            xdiff = boid.getPosition()[0] - b.getPosition()[0]
            ydiff = boid.getPosition()[1] - b.getPosition()[1]

            if math.sqrt((xdiff**2) + (ydiff**2)) < 100:
                cx -= xdiff
                cy -= ydiff

    return cx, cy


def rule3(b, boids):
    '''
    Rule 3 implementation of CR's rules

    :param b: boid to apply rule to
    :param boids: other boids in system
    :return: rule 3 vector as tuple of x and y movement
    '''
    pvjx = 0
    pvjy = 0

    for boid in boids:
        if boid != b:
            pvjx += boid.getVelocity()[0]
            pvjy += boid.getVelocity()[1]

    pvjx /= len(boids) - 1
    pvjy /= len(boids) - 1

    pvjx = (pvjx - b.getVelocity()[0])/8
    pvjy = (pvjy - b.getVelocity()[1])/8

    return pvjx, pvjy


def move_all_boids_to_new_positions(boids):
    '''
    Moves passed list of boids by applying all three of Craig Reynold's rules simultaneously

    :param boids: list of boids to move
    :return: void
    '''
    for boid in boids:
        v1 = rule1(boid, boids)
        v2 = rule2(boid, boids)
        v3 = rule3(boid, boids)

        newvelx = boid.getVelocity()[0] + v1[0] + v2[0] + v3[0]
        newvely = boid.getVelocity()[1] + v1[1] + v2[1] + v3[1]

        boid.setVelocity((newvelx, newvely))

        newposx = boid.getPosition()[0] + boid.getVelocity()[0]
        newposy = boid.getPosition()[1] + boid.getVelocity()[1]

        boid.setPosition((newposx, newposy))

    return

# def main():
#     boid1 = Boid((0, 0), (4, 3))
#     boid2 = Boid((3, 5), (-1, -2))
#     boid3 = Boid((-1, 4), (1, -1))
#
#     boidlist = [boid1, boid2, boid3]
#
#     for i in range(0, 10):
#         move_all_boids_to_new_positions(boidlist)
#         print("boid1")
#         print(boid1.getPosition())
#         print(boid1.getVelocity())
#         print("boid2")
#         print(boid2.getPosition())
#         print(boid2.getVelocity())
#         print("boid3")
#         print(boid3.getPosition())
#         print(boid3.getVelocity())
#
#
# if __name__ == '__main__':
#     main()
