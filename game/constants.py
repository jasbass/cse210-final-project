import os

MAX_X = 800
MAX_Y = 608
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_HERO = os.path.join(os.getcwd(), "./graphics/single.png")

IMAGES_HERO = {
    'down_animations': [os.path.join(os.getcwd(), "./graphics/character_down_one.png"),
    os.path.join(os.getcwd(), "./graphics/character_down_two.png"),
    os.path.join(os.getcwd(), "./graphics/character_down_three.png")],

    'left_animations': [os.path.join(os.getcwd(), "./graphics/character_left_one.png"),
    os.path.join(os.getcwd(), "./graphics/character_left_two.png"),
    os.path.join(os.getcwd(), "./graphics/character_left_three.png")],

    'right_animations': [os.path.join(os.getcwd(), "./graphics/character_right_one.png"),
    os.path.join(os.getcwd(), "./graphics/character_right_two.png"),
    os.path.join(os.getcwd(), "./graphics/character_right_three.png")],

    'up_animations': [os.path.join(os.getcwd(), "./graphics/character_up_one.png"),
    os.path.join(os.getcwd(), "./graphics/character_up_two.png"),
    os.path.join(os.getcwd(), "./graphics/character_up_three.png")]
     }

IMAGES_ENEMY = {
    'down_animations': [os.path.join(os.getcwd(), "./graphics/enemy_down_one.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_down_two.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_down_three.png")],

    'left_animations': [os.path.join(os.getcwd(), "./graphics/enemy_left_one.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_left_two.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_left_three.png")],

    'right_animations': [os.path.join(os.getcwd(), "./graphics/enemy_right_one.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_right_two.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_right_three.png")],

    'up_animations': [os.path.join(os.getcwd(), "./graphics/enemy_up_one.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_up_two.png"),
    os.path.join(os.getcwd(), "./graphics/enemy_up_three.png")]
     }

IMAGES_GROUND = [os.path.join(os.getcwd(), "./graphics/grass_one.png"), os.path.join(os.getcwd(), "./graphics/grass_two.png"), os.path.join(os.getcwd(), "./graphics/grass_three.png"),
    os.path.join(os.getcwd(), "./graphics/grass_four.png"), os.path.join(os.getcwd(), "./graphics/grass_five.png"), os.path.join(os.getcwd(), "./graphics/grass_six.png")]

IMAGE_BUSH = os.path.join(os.getcwd(), "./graphics/bush.png")

IMAGE_INTRO_BACKROUND = os.path.join(os.getcwd(), "./graphics/introbackground.png")

IMAGE_GAME_OVER = os.path.join(os.getcwd(), "./graphics/gameover.png")

IMAGE_BUTTON = os.path.join(os.getcwd(), "./graphics/button.png")


BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

PLAYER_SPEED = 5
ENEMY_SPEED = 2

TILESIZE = 32

# IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")

# SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
# SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
# SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

# BALL_WIDTH = 24
# BALL_HEIGHT = 24

# BALL_X = (MAX_X / 2) - (BALL_WIDTH / 2)
# BALL_Y = MAX_Y - 125

# BALL_DX = 8
# BALL_DY = BALL_DX * -1

# PADDLE_WIDTH = 96
# PADDLE_HEIGHT = 24

# PADDLE_X = (MAX_X / 2) - (PADDLE_WIDTH / 2)
# PADDLE_Y = MAX_Y - 25

# BRICK_WIDTH = 48
# BRICK_HEIGHT = 24

# BRICK_SPACE = 5

# PADDLE_SPEED = 15