import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름!

# 배경 이미지 불러오기
background = pygame.image.load("D:/NC/Python_Self_study/pygame_basic/background.png");

# 이벤트 루프
running = True # 게임이 진행중인가를 확인하는 코드줄
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?를 확인하는 코드
            running = False  # 게임이 진행중이 아님
    
    # screen.fill((0,0,255)) RGB값을 받아서 배경을 그려준다
    screen.blit(background, (0, 0)) # background 이미지를 불러와서 배경으로 띄우기

    pygame.display.update() # 이 코드로 게임화면을 계속 그려준다. 말 그대로 display를 update를 계속하는것

# pygame 종료
pygame.quit()