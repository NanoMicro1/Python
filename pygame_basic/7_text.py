import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름!

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:/NC/Python_Self_study/pygame_basic/background.png")


# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/NC/Python_Self_study/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해온다
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_position = (screen_width / 2) - (character_width / 2) # 화면 가로 절반 위치
character_y_position = screen_height - character_height # 화면 세로 위치

# 이동할 좌표라는 변수
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# 적 캐릭터. enemy

enemy = pygame.image.load("D:/NC/Python_Self_study/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해온다
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_position = (screen_width / 2) - (enemy_width / 2) # 화면 가로 절반 위치
enemy_y_position = (screen_height / 2) - (enemy_height / 2) # 화면 세로 위치



# 폰트 정의 
game_font = pygame.font.Font(None, 40) 

# 총 시간
total_time = 1000

# 시작시간
start_ticks = pygame.time.get_ticks()



# 이벤트 루프
running = True # 게임이 진행중인가를 확인하는 코드줄
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정! 캐릭터의 스피드를 설정
    # print("fps : " + str(clock.get_fps())) fps 즉 프레임을 실시간으로 속도를 알수 있다. 재미용
    # FPS = Frame Per Second

# 캐릭터가 1초 동안에 100만큼 이동 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동한다는 뜻. 10 * 10 = 100
# 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동한다는 뜻. 5 * 20 = 100

    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?를 확인하는 코드
            running = False  # 게임이 진행중이 아님
    
        # 키보드를 눌렀을때 ↓
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로. Key_LEFT
                to_x -= character_speed # 5 위치만큼 왼쪽으로. to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 캐릭터 x좌표와 y좌표가 여기 있다 ↓
    character_x_position += to_x * dt
    character_y_position += to_y * dt

    # 가로 경계값 처리. 화면 밖으로 나가지 않도록 처리해주는 코드 ↓
    if character_x_position < 0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width
    # 세로 경계값 처리
    if character_y_position < 0:
        character_y_position = 0
    elif character_y_position > screen_height - character_height:
        character_y_position = screen_height - character_height

    # 충돌처리를 위한 rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_position
    character_rect.top = character_y_position

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position

    # 충돌체크
    if character_rect.colliderect(enemy_rect):
        print("## Impact ! ##\n## Game will be closed in 2 seconds ##")
        running = False

    screen.blit(background, (0, 0)) # background 이미지를 불러와서 배경으로 띄우기
    screen.blit(character, (character_x_position, character_y_position)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_position, enemy_y_position)) # enemy 그리기


    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # 지금까지 흐른 시간. ms밀리세컨드 이기때문에 1000으로 나눈다
    # 경과 시간을 나눠서 초단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
                    # render(            시간,                    True,     글자 색상 )
    screen.blit(timer, (10, 10)) # 출력할 글자, 글자 색상. 말 그대로 timer, 시계를 보여준다

    # 만약 시간이 0 이하이면 게임 종료!
    if total_time - elapsed_time <= 0:
        print("time out")
        running = False
    pygame.display.update() # 이 코드로 게임화면을 계속 그려준다. 말 그대로 display를 update를 계속하는것
    

    # 잠시대기 
pygame.time.delay(2000) # 2초 정도 대기!

# pygame 종료
pygame.quit()