# <-- Flappy Bird Game using Pygame -->

# Importing Pygame and sys
import pygame as pg
import sys
import random


# Initializing Pygame
pg.init()
pg.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)

# Creating Screen
screen = pg.display.set_mode((288, 512))
clock = pg.time.Clock()
# Game Variables
gravity = 0.28
bird_movement = 0
game_active = True
score = 0
high_score = 0
score_sound_countdown = 100

# Game Title and Icon
pg.display.set_caption('Flappy Bird')
icon = pg.image.load('favicon.png')
pg.display.set_icon(icon)

# Importing Images
# For Background
background_surface = pg.image.load('images/background-day.png').convert()

# For Floor
floor_surface = pg.image.load('images/base.png')
floor_x = 0

# For Bird
bird_surface = pg.image.load('images/bluebird-midflap.png').convert_alpha()
bird_rect = bird_surface.get_rect(center=(50, 256))

# For Pipes
pipe_surface = pg.image.load('images/pipe-green.png')
pipe_list = []
SPAWNPIPE = pg.USEREVENT
pg.time.set_timer(SPAWNPIPE, 1000)
pipe_height = [250, 300, 350, 400]

# Game over surface+
game_over_surface = pg.image.load('images/message.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(144, 275))

# Adding Text (Score)
game_font = pg.font.Font('Font.TTF', 25)

# Importing Sounds
try:
    pg.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
    sound_enabled = True
except pg.error:
    print("Audio disabled: No sound device found.")
    sound_enabled = False

# Only load and play sounds if sound is enabled
if sound_enabled:
    flap_sound = pg.mixer.Sound('audio/wing.wav')
    death_sound = pg.mixer.Sound('audio/hit.wav')
    score_sound = pg.mixer.Sound('audio/point.wav')


def draw_floor():
    screen.blit(floor_surface, (floor_x, 450))
    screen.blit(floor_surface, (floor_x + 288, 450))


def create_pipe():
    random_pipe = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(288, random_pipe))
    top_pipe = pipe_surface.get_rect(midbottom=(288, random_pipe - 150))
    return bottom_pipe, top_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pg.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 450:
        death_sound.play()
        return False

    return True


def rotate_bird(bird):
    new_bird = pg.transform.rotozoom(bird, -bird_movement, 1)
    return new_bird


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render('Score : ' + str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(144, 50))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render('Score : ' + str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(144, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render('High Score : ' + str(int(high_score)), True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(144, 50))
        screen.blit(high_score_surface, high_score_rect)


def update_high_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# Selection Menu Variables
selected_background = 'day'
selected_bird = 'blue'
menu_stage = 'background'  # Stage to track which menu is active
option_index = 0  # Track current selected option

# Create text labels for options
menu_font = pg.font.Font('Font.TTF', 30)
# Load Game Over image or text surface
game_over_surface = pg.image.load('images/gameover.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(144, 256))

# Menu Loop for background selection
menu_active = True
while menu_active:
    screen.fill((0, 0, 0))  # Clear screen for menu display

    if menu_stage == 'background':
        menu_options = [
            {'text': 'Day Background', 'value': 'day'},
            {'text': 'Night Background', 'value': 'night'}
        ]
    elif menu_stage == 'bird':
        menu_options = [
            {'text': 'Blue Bird', 'value': 'blue'},
            {'text': 'Red Bird', 'value': 'red'},
            {'text': 'Yellow Bird', 'value': 'yellow'}
        ]

    # Render and highlight options
    for i, option in enumerate(menu_options):
        color = (255, 255, 0) if i == option_index else (255, 255, 255)  # Highlight current selection
        option_text = menu_font.render(option['text'], True, color)
        option_rect = option_text.get_rect(center=(144, 100 + i * 50))
        screen.blit(option_text, option_rect)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                option_index = (option_index + 1) % len(menu_options)  # Move down and wrap around
            if event.key == pg.K_UP:
                option_index = (option_index - 1) % len(menu_options)  # Move up and wrap around
            if event.key == pg.K_RETURN:  # Confirm selection with Enter
                if menu_stage == 'background':
                    selected_background = menu_options[option_index]['value']
                    menu_stage = 'bird'  # Move to the bird selection screen
                    option_index = 0  # Reset the index for the next menu
                elif menu_stage == 'bird':
                    selected_bird = menu_options[option_index]['value']
                    menu_active = False  # Exit the menu after selecting

# Load selected assets
if selected_background == 'night':
    background_surface = pg.image.load('images/background-night.png').convert()
else:
    background_surface = pg.image.load('images/background-day.png').convert()

if selected_bird == 'red':
    bird_surface = pg.image.load('images/redbird-midflap.png').convert_alpha()
elif selected_bird == 'yellow':
    bird_surface = pg.image.load('images/yellowbird-midflap.png').convert_alpha()
else:  # Defaults to blue
    bird_surface = pg.image.load('images/bluebird-midflap.png').convert_alpha()
# Starting Loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
                flap_sound.play()

            if event.key == pg.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50, 256)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # Background Surface and Floor
    screen.blit(background_surface, (0, 0))
    floor_x -= 1
    draw_floor()
    if floor_x <= -288:
        floor_x = 0

    if game_active:
        # Bird Movement
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Check Collision

        # Pipes
        pipe_list = move_pipe(pipe_list)
        draw_pipes(pipe_list)

        # Showing Score
        score += 0.01
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_high_score(score, high_score)
        score_display('game_over')

    pg.display.update()

    clock.tick(60)
