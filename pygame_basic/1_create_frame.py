import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_height, screen_width))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름!

# 이벤트 루프
running = True # 게임이 진행중인가를 확인하는 코드줄
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?를 확인하는 코드
            running = False  # 게임이 진행중이 아님

# pygame 종료
pygame.quit()