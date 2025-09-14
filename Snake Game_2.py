import pygame
import random

pygame.init()
tile_sizee = 32
width = 640
height = 610
Score = 0
Lives = 5
tile_number_x = width // tile_sizee
tile_number_y = height //  tile_sizee

Font = pygame.font.SysFont("Papyrus",35)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")

Apple = pygame.image.load("SnakeGame_Assets/apple.png")
# Apple = pygame.transform.scale(Apple,(100,10))

Path = pygame.image.load("SnakeGame_Assets/Path, The REAL ONEEE.jpg")
Path = pygame.transform.scale(Path,(width,height))

Head_imgs = {
    "UP": pygame.image.load("SnakeGame_Assets/head_up.png"),
    "DOWN":pygame.image.load("SnakeGame_Assets/head_down.png"),
    "LEFT":pygame.image.load("SnakeGame_Assets/head_left.png"),
    "RIGHT":pygame.image.load("SnakeGame_Assets/head_right.png")
}

Tail_imgs = {
    "UP": pygame.image.load("SnakeGame_Assets/tail_up.png"),
    "DOWN":pygame.image.load("SnakeGame_Assets/tail_down.png"),
    "LEFT":pygame.image.load("SnakeGame_Assets/tail_left.png"),
    "RIGHT":pygame.image.load("SnakeGame_Assets/tail_right.png")
}

body_horiz = pygame.image.load("SnakeGame_Assets/body_horizontal.png")
body_verti = pygame.image.load("SnakeGame_Assets/body_vertical.png")

    # index = 0  = head
    # index  = 1 = body
    # index = 2 = tail

#           0      1      2
snake = [(5,10),(4,10),(3,10)]

new_block = False

direction =(1,0)

# directions                                         #head is at column 5 and row 10
                                                        #body is at column 4 and row 10
                                                        # tail is at col 3 and row 10
# (1,0) ---> right
# (-1,0) ---> left
# (0,1) ---> down
# (0,-1) ----> up
def random_fruit():
    global snake
    x = random.randint(2,tile_number_x -3)
    y = random.randint(2,tile_number_y -3)
    pos = (x,y)

    if pos not in snake:
        return pos
    else:
        return random_fruit()
# fruit = random_fruit()





def move_Snake():
    global snake, new_block
    headx,heady = snake[0]
    dx,dy = direction

    new_head = (headx+ dx, heady + dy) # gives new head positon

    if new_block == True:
        snake = [new_head] + snake
        new_block = False
    else:
        snake = [new_head] + snake[:-1]



# fruit = random_fruit()

def draw_fruit():
    global fruits,x,y
    # x,y = fruit
    # screen.blit(Apple,(x*tile_sizee,  y * tile_sizee))
    # draw the fruit at random spots
    
    for x,y in fruits:
        screen.blit(Apple, (x * tile_sizee, y * tile_sizee))


def draw_snalke():
    for index,block in enumerate(snake):
        x,y = block
        rect  = pygame.Rect(x*tile_sizee, y *tile_sizee, tile_sizee, tile_sizee)

        if index ==0:
            if direction ==(1,0):
                screen.blit(Head_imgs["RIGHT"],rect)
            if direction ==(-1,0):
                screen.blit(Head_imgs["LEFT"],rect)
            if direction ==(0,1):
                screen.blit(Head_imgs["DOWN"],rect)
            if direction ==(0,-1):
                screen.blit(Head_imgs["UP"],rect)

        elif index == len(snake) -1:
            prev_X,prev_Y = snake[-2]
            dx,dy = prev_X-x, prev_Y - y

            if dx == 1:
                 screen.blit(Tail_imgs["LEFT"],rect)
            if dx == -1:
                screen.blit(Tail_imgs["RIGHT"],rect)
            if dy == 1:
                screen.blit(Tail_imgs["UP"],rect)
            if dy == -1:
                screen.blit(Tail_imgs["DOWN"],rect)


        else:
            prev_X,prev_Y = snake [index-1]
            next_X,next_Y = snake[index + 1]

            if prev_X == next_X:
                screen.blit(body_verti,rect)
            elif prev_Y == next_Y:
                screen.blit(body_horiz,rect)
            else:
                screen.blit(body_horiz,rect)



running = True
tile_number_x = width // tile_sizee
tile_number_y = width // tile_sizee

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

def reset_game():
    global snake,direction,fruit,new_block, Score, Lives
    snake = [(5,10), (4,10), (3,10)]
    direction = (1,0) # right
    Score = 0
    Lives = Lives - 1
    fruit = random_fruit()

fruits = []

for i in range(5):
    fruits.append(random_fruit())


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == screen_update:
            move_Snake()

        for f in fruits:
            if snake[0] == f:
                fruits.remove(f)
                fruits.append(random_fruit())
                new_block = True
                Score += 1
                break
            # if snake[0] == fruit:
            #     fruit = random_fruit()
            #     new_block = True
            #     Score = Score + 1

            head_x, head_y = snake[0]

            if head_x <= 0 or head_x >= tile_number_x or head_y < 0 or head_y >= tile_number_y:
                reset_game()

            if snake[0] in snake[1:]:
                reset_game()

            headx,heady = snake[0]
            if Lives == 0:
                running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w and direction != (0,1):
                direction = (0,-1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s and direction != (0,-1):
                direction = (0,1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d and direction != (-1,0):
                direction = (1,0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a and direction != (1,0):
                direction = (-1,0)

    text = Font.render(f"Score : {Score}" , True,"white")
    Text = Font.render(f"Lives : {Lives}", True,'White')

    # screen.blit(Apple,(100,100))
    screen.blit(Path,(0,0))
    draw_snalke()
    draw_fruit()
    # fruit = random_fruit()
    draw_fruit()
    # fruit = random_fruit()
    draw_fruit()
    # fruit = random_fruit()
    screen.blit(text,(25,25))
    screen.blit(Text,(500,25))
    pygame.display.flip()

#hw : increase the score and display itd
