import pygame
import os

pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First game!")
# how fast the game runs is largely dependant on your computer, on how fast it will complete the while loop. if you have a good pc it could be thousands of times a second
# compared to a subpar machine it could be a few hundred. To control this you implement FPS, or how fast the screen will draw itself
FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
WHITE = (255, 255, 255)
# rect = X and Y, Width and Height
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
# basis of pygame is creating a for loop that sits and checks for everything thats going on , drawing the screen, keeping
# the game running
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.mp3"))
BULLET_VEL = 7
MAX_BULLETS = 3


HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)
# this is how you would import images
SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT)
)
# the directory seperator might be different depending on machine, ie not \ so you use os.path.join to make os do it for you
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png")
)
# transform takes the image you want to resize, then the dimensions you want to resize it to
# while rotate takes the thing you want to rotate, and then as a second arguement takes how much you want to rotate it
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90,
)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))

RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    270,
)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    # what surface you want to draw on , what color, what rectangle do you want to draw
    pygame.draw.rect(WIN, "BLACK", BORDER)

    red_health_text = HEALTH_FONT.render("health : " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("health : " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    # we are allowed to use .x and .y because yellow and red are pygame rectangles
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    # you use blit() when you want to draw a surface onto the screen
    # drawing the bullets which are rectangles created in main, which are then passed to the handle bullets fnc which then adds or subtracts to the x at which the bullet was created
    # to then move it across the screen every single frame, which we are doing with the code below
    for bullet in red_bullets:
        pygame.draw.rect(WIN, "RED", bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, "YELLOW", bullet)
    # when you fill the window in python, you can draw as many things as youd like but nothing will change until you update the display
    pygame.display.update()


# functions take in keys_pressed, and the rect they are controlling
# width is a property of rect, what we are using it for is because the everything is drawn from the top left, you need to account for the size of the image as well otherwise it
# will overlap the border without technically going over because its 0,0 is still on the correct side
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # right
        yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER.x + BORDER.width:  # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # right
        red.x += VEL

    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:  # down
        red.y += VEL


# here we take all created bullets, and add on the bullet velocity to move it across the screen . If it hits the red or yellow rect rep. the spaceships, issue an pygame event we
# can then get at back in the for loop in the main
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(
        draw_text,
        (
            WIDTH // 2 - draw_text.get_width() / 2,
            HEIGHT // 2 - draw_text.get_height() / 2,
        ),
    )
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    # This is what you were doing this all for, you end up just making a rectangle the same size as the image, it takes an x and a y, then the widght and height of the rectangle
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_health = 10
    yellow_health = 10
    red_bullets = []
    yellow_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        # the code below MAKES SURE the program is going to refresh at 60 frames per second unless the computer cannot keep up with that speed. This keeps it controlled
        # instead of running/refreshing 100000 times a second
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width,
                        yellow.y + yellow.height // 2 - 2,
                        10,
                        5,
                    )

                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)

                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins!"
        if yellow_health <= 0:
            winner_text = "Red wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        # everytime the while loop runs, this tell us what keys are currently pressed down AS A LIST
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    main()


# pygame event get returns a list and then we can go through each event and check what they were. currently checks if we click on red x, then run = false, breakings while loop and
# quits the game

if __name__ == "__main__":
    main()
