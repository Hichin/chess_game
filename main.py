import pygame
from data.classes.Board import Board
pygame.init()
MENU = "menu"
GAME = "game"
EXIT = "exit"
window_size = (800, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Шахматы")
board = Board(window_size[0], window_size[1])
state = MENU
def game_loop(screen, board):
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXIT
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.handle_click(mx, my)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return MENU

        winner = None
        if board.check_checkmate('black'):
            winner = 'Белые победили!'
        elif board.check_checkmate('white'):
            winner = 'Черные победили!'
        draw(screen)
        if winner:
            draw_popup(screen, winner)
            pygame.time.wait(3000)
            return MENU
    return GAME
def settings_menu(screen, board):
    settings_running = True
    while settings_running:
        screen.fill((0, 0, 0))  # Задний фон

        font = pygame.font.Font(None, 36)
        light_color_text = font.render('Светлая доска', True, (255, 255, 255))
        dark_color_text = font.render('Темная доска', True, (255, 255, 255))
        return_text = font.render('Вернуться в меню', True, (255, 255, 255))

        screen.blit(light_color_text, (100, 100))
        screen.blit(dark_color_text, (100, 150))
        screen.blit(return_text, (100, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_running = False
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 100 <= mx <= 300 and 100 <= my <= 130:
                    board.change_board_color('light')  # Изменение на светлую тему
                elif 100 <= mx <= 300 and 150 <= my <= 180:
                    board.change_board_color('dark')  # Изменение на темную тему
                elif 100 <= mx <= 300 and 200 <= my <= 230:
                    settings_running = False

        pygame.display.flip()

def main_menu(screen, board):
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))  # Задний фон

        font = pygame.font.Font(None, 36)


        if board.game_started:
            start_game_text = font.render('Продолжить', True, (255, 255, 255))
            screen.blit(start_game_text, (100, 100))
            restart_game_text = font.render('Рестарт игры', True, (255, 255, 255))
            screen.blit(restart_game_text, (100, 150))
            settings_text = font.render('Настройки', True, (255, 255, 255))
            screen.blit(settings_text, (100, 200))
            exit_text = font.render('Выход', True, (255, 255, 255))
            screen.blit(exit_text, (100, 250))
        else:
            start_game_text = font.render('Начать игру', True, (255, 255, 255))
            screen.blit(start_game_text, (100, 100))
            settings_text = font.render('Цвет доски', True, (255, 255, 255))
            screen.blit(settings_text, (100, 150))
            exit_text = font.render('Выход', True, (255, 255, 255))
            screen.blit(exit_text, (100, 200))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 100 <= mx <= 300 and 100 <= my <= 130:
                    board.start_game()  # Устанавливаем флаг начала игры
                    return 'game'  # Начать игру
                elif board.game_started and 100 <= mx <= 300 and 150 <= my <= 180:
                    board.reset_board()  # Рестарт игры
                    return 'game'
                elif (board.game_started and 100 <= mx <= 300 and 200 <= my <= 230) or (not board.game_started and 100 <= mx <= 300 and 150 <= my <= 180):
                    settings_menu(screen, board)  # Переход в настройки
                elif (board.game_started and 100 <= mx <= 300 and 250 <= my <= 280) or (not board.game_started and 100 <= mx <= 300 and 200 <= my <= 230):
                    return 'exit'  # Выход из игры

        pygame.display.flip()
    return 'menu'


def draw(display):
	display.fill('black')
	board.draw(display)
	pygame.display.update()
def draw_popup(window, message):
	popup_width, popup_height = 300, 150
	popup_x, popup_y = (window.get_width() - popup_width) // 2, (window.get_height() - popup_height) // 2
	popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
	background_color = (255, 255, 255)
	text_color = (0, 0, 0)
	pygame.draw.rect(window, background_color, popup_rect)
	font = pygame.font.Font(None, 36)
	text_surface = font.render(message, True, text_color)
	text_rect = text_surface.get_rect(center=popup_rect.center)
	window.blit(text_surface, text_rect)
	pygame.display.update()

main_menu(screen, board)
while True:
    if state == MENU:
        state = main_menu(screen, board)
    elif state == GAME:
        state = game_loop(screen, board)
    elif state == EXIT:
        break
pygame.quit()

if __name__ == '__main__':
    pygame.init()
    window_size = (800, 800)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Шахматы")
    board = Board(window_size[0], window_size[1])
    state = MENU

    while True:
        if state == MENU:
            state = main_menu(screen, board)
        elif state == GAME:
            state = game_loop(screen, board)
        elif state == EXIT:
            break

    pygame.quit()





