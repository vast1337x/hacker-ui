import random
import time
import sys
import shutil
import colorama

colorama.init()

WIDTH, HEIGHT = shutil.get_terminal_size()

CHARACTERS = "!@#$%^&*()-+=<>?/.,;:"

MAX_FALLING_CHARACTERS = HEIGHT // 2

screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def generate_falling_character():
    return {
        'x': random.randint(0, WIDTH - 1),
        'y': random.randint(-HEIGHT, 0),
        'char': random.choice(CHARACTERS),
        'speed': random.randint(1, 3)
    }

def update_screen():
    print('\033c', end='')

    for row in screen:
        encoded_row = [colorama.Fore.GREEN + c + colorama.Style.RESET_ALL for c in row]
        print(''.join(encoded_row))

def animate_falling_characters():
    falling_characters = []

    while True:
        if len(falling_characters) < MAX_FALLING_CHARACTERS:
            falling_characters.append(generate_falling_character())

        for character in falling_characters:
            x, y = character['x'], character['y']
            screen[y][x] = ' '

            character['y'] += character['speed']

            if character['y'] >= HEIGHT:
                character['y'] = random.randint(-HEIGHT, 0)

            screen[character['y']][character['x']] = character['char']

        update_screen()

        time.sleep(0.01)

animate_falling_characters()
