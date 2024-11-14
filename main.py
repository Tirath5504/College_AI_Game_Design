import pygame
import networkx as nx
import random
import math

GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 5
PREDATOR_SPEED_DELAY = 3
SURVIVAL_TIME_LIMIT = 30
TEXT_SIZE = 24

BACKGROUND_COLOR = (200, 200, 200)
OBSTACLE_COLOR = (0, 0, 255)

directions = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}

prey_image = pygame.image.load('assets/jerry.png')
prey_image = pygame.transform.scale(prey_image, (CELL_SIZE, CELL_SIZE))

predator_image = pygame.image.load('assets/tom.png')
predator_image = pygame.transform.scale(predator_image, (CELL_SIZE, CELL_SIZE))

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("AI Predator and Prey")
clock = pygame.time.Clock()

grid = nx.grid_2d_graph(GRID_SIZE, GRID_SIZE)
obstacles = random.sample(list(grid.nodes()), GRID_SIZE)
for obstacle in obstacles:
    grid.remove_node(obstacle)

start_ticks = pygame.time.get_ticks()
game_over = False
win = False
frame_counter = 0

def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    for obstacle in obstacles:
        x, y = obstacle
        pygame.draw.rect(screen, OBSTACLE_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    x, y = prey_position
    screen.blit(prey_image, (x * CELL_SIZE, y * CELL_SIZE))

    x, y = predator_position
    screen.blit(predator_image, (x * CELL_SIZE, y * CELL_SIZE))

def display_text(text, position, color=(0, 0, 0), size=TEXT_SIZE):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def move_prey(key):
    global prey_position
    if key in directions:
        dx, dy = directions[key]
        new_position = (prey_position[0] + dx, prey_position[1] + dy)
        if new_position in grid.nodes:
            prey_position = new_position

def move_predator():
    global predator_position
    if prey_position != predator_position:
        try:
            path = nx.astar_path(grid, predator_position, prey_position)
            if len(path) > 1:
                predator_position = path[1]
        except nx.NetworkXNoPath:
            pass

def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def random_position_away_from_predator(predator_position, min_distance):
    valid_positions = [node for node in grid.nodes if euclidean_distance(node, predator_position) > min_distance]
    return random.choice(valid_positions) if valid_positions else predator_position

predator_position = random.choice(list(grid.nodes()))
prey_position = random_position_away_from_predator(predator_position, 5)

def show_start_screen():
    screen.fill(BACKGROUND_COLOR)
    display_text("AI Predator and Prey", (WINDOW_SIZE // 2 - 130, WINDOW_SIZE // 2 - 100), (0, 0, 0), 36)
    display_text("Survive for 30 seconds to win", (WINDOW_SIZE // 2 - 150, WINDOW_SIZE // 2 - 50), (0, 0, 0), 28)
    display_text("Use arrow keys to move", (WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2), (0, 0, 0), 24)
    display_text("The predator will chase you if you are in its vision", (WINDOW_SIZE // 2 - 180, WINDOW_SIZE // 2 + 50), (0, 0, 0), 24)
    display_text("Starting in 10 seconds...", (WINDOW_SIZE // 2 - 100, WINDOW_SIZE // 2 + 100), (150, 0, 0), 24)
    pygame.display.flip()
    pygame.time.delay(10000)
    return True

def show_end_screen(result_text, color):
    screen.fill(BACKGROUND_COLOR)
    display_text(result_text, (WINDOW_SIZE // 2 - 150, WINDOW_SIZE // 2 - 50), color, 36)
    pygame.display.flip()
    pygame.time.delay(5000)

def check_survival_time():
    survival_time = (pygame.time.get_ticks() - start_ticks) / 1000
    return survival_time >= SURVIVAL_TIME_LIMIT

def game_loop():
    global predator_position, prey_position, game_over, win, frame_counter, start_ticks
    running = show_start_screen()
    while running:
        if game_over:
            if win:
                show_end_screen("Congratulations! You Win!", (0, 0, 255))
            else:
                show_end_screen("Game Over! You Lose!", (255, 0, 0))
            running = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                move_prey(event.key)

        if not game_over:
            if frame_counter % PREDATOR_SPEED_DELAY == 0:
                move_predator()

            if euclidean_distance(predator_position, prey_position) <= 1:
                game_over = True
                win = False

            if check_survival_time():
                game_over = True
                win = True

            draw_grid()
            display_text(f"Survival Time: {int((pygame.time.get_ticks() - start_ticks) / 1000)}s", (10, 10))
            display_text("Reach 30s to Win!", (10, 40))

        pygame.display.flip()
        clock.tick(FPS)
        frame_counter += 1

    pygame.quit()

game_loop()
