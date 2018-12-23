import pygame

pygame.init()

BLACK = [0, 0, 0]
RED = [255, 0, 0]
clock = pygame.time.Clock()

# screen (could change to grid matching the pixels to make it easier if we wanted)
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill(BLACK)
pygame.display.set_caption("TRON")
pygame.display.flip()


class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([30, 30])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()


test = Player(RED)

print("hi")
# TODO: make player pixel(s)

# TODO: make function to move player pixel and leave trail

# TODO: make function to boost player pixel

# TODO: function for starting a new game

# TODO: function for detecting collisions with wall or other players path
