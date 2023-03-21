from models import*

GREEN = (0, 255, 0)

background = transform.scale(image.load("Blue.jpg"), WINDOW_SIZE)

font.init()
font_label = font.SysFont('Comic Sans Ms', 32)

player1_win_label = font_label.render('Player1 WIN!!!', True, GREEN)
player2_win_label = font_label.render('Player2 WIN!!!', True, GREEN)


player1 = Player('PingPongGame-exam-600x453.jpg', PLAYER_SIZE[0], WINDOW_SIZE[1] - PLAYER_SIZE[1], 5, "left")
player2 = Player('PingPongGame-exam-600x453.jpg', WINDOW_SIZE[0] - 2 * PLAYER_SIZE[0], 0, 5, "right")
ball = Ball()

game = True
finish = False

clock = time.Clock()

while game:
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        ball.draw()
        ball.move(player1, player2)
        player1.update_position()
        player2.update_position()

        if ball.rect.x + ball.rect.width >= WINDOW_SIZE[0]:
            window.blit(player1_win_label, 
                    (WINDOW_SIZE[0] / 2 - player1_win_label.get_width() / 2, WINDOW_SIZE[1] / 2 - player1_win_label.get_height() / 2))
            finish = True
        
        if ball.rect.x <= 0:
            window.blit(player2_win_label, 
                    (WINDOW_SIZE[0] / 2 - player1_win_label.get_width() / 2, WINDOW_SIZE[1] / 2 - player1_win_label.get_height() / 2))
            finish = True
        clock.tick(FPS)
        display.update()