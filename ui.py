import pygame
import board
from pygame.locals import *

pygame.init()
WIDTH = 700
HEIGHT = 600


def start():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_loop(screen)


def game_loop(screen):
    game_board = board.Board()
    colors = {0: (255, 255, 204), 1: (0, 0, 255), 2: (255, 0, 0)}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if game_board.winner is not None:
                    game_board.reset_board()
                position = pygame.mouse.get_pos()
                col = position[0] // 100
                game_board.next_move(col)
            if event.type == pygame.QUIT:
                running = False
        screen.fill((153, 76, 0))

        for i in range(board.board_size[0]):
            for j in range(board.board_size[1]):
                pygame.draw.circle(screen, (0, 0, 0), (50 + j * 100, 550 - i * 100), 48)
                pygame.draw.circle(screen, colors[game_board.board[i][j]], (50 + j * 100, 550 - i * 100), 45)

        if game_board.winner is not None:
            pygame.display.set_caption('Show Text')
            font = pygame.font.Font('freesansbold.ttf', 72)
            text = font.render(f"Player {game_board.winner} win!!!", True, colors[game_board.winner], (125, 125, 125))
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(text, textRect)
        pygame.display.update()
