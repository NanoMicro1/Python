import pygame

## 게임의 skeleton, scatch
###################################################################################################
# 기본초기화 (반드시 해야하는것들)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름!

# FPS
clock = pygame.time.Clock()
###################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등등 세부사항)

running = True # 게임이 진행중인가를 확인하는 코드줄
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정! 캐릭터의 스피드를 설정
    # print("fps : " + str(clock.get_fps())) fps 즉 프레임을 실시간으로 속도를 알수 있다. 재미용
    # FPS = Frame Per Second


# 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False  

# 3. 게임 캐릭터 위치 정의
# 4. 충돌 처리

    
# 5. 화면에 그리기 

    pygame.display.update() # 이 코드로 게임화면을 계속 그려준다. 말 그대로 display를 update를 계속하는것

# pygame 종료
pygame.quit()