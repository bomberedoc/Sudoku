import pygame
from pygame.locals import *
from sudok import Sudoku

def draw_board(board):
    screen.fill((255,255,255))
    for i in range(9):
        for j in range(9):
            if boards[i*9+j][2]:
                pygame.draw.rect(screen, (255,127,80), boards[i*9+j][0])
                pygame.draw.rect(screen, BLACK, boards[i*9+j][0],1)
            else:
                pygame.draw.rect(screen, BLACK, boards[i*9+j][0],1)
    for i in range(3):
        pygame.draw.rect(screen,BLACK,(50+150*i,50+0,150,450), 2)
        pygame.draw.rect(screen,BLACK,(50+0,50+150*i,450,150), 2)
    for i in range(9):
        for j in range(9):
            if boards[i*9+j][1]!=0:
                font = pygame.font.SysFont(None, 40)
                img = font.render(str(boards[i*9+j][1]), True, (69,69,69))
                screen.blit(img, (boards[i*9+j][0].centerx-5,boards[i*9+j][0].centery-10))
    pygame.draw.rect(screen,(200,200,200),button[0])
    pygame.draw.rect(screen,(0,0,0),button[0],1)
    font = pygame.font.SysFont(None, 40)
    img = font.render('Solve', True, BLACK)
    screen.blit(img, (width/2-35, 525+12))
    pygame.display.update()

def solve_it(boards,running,l,m,sudoku):
    while running:
        col=BLACK
        change = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                x1,y1 = button[0].topleft
                x2,_ = button[0].topright
                _,y3 = button[0].bottomleft
                if x>=x1 and x<=x2 and y>=y1 and y<=y3:
                    sudoku = sudoku.sudoku_solver()
                    for i in range(9):
                        for j in range(9):
                            boards[i*9+j][1]=sudoku[j][i]
                    change = True
                for i in range(9):
                    for j in range(9): 
                        x1,y1 = boards[i*9+j][0].topleft
                        x2,_ = boards[i*9+j][0].topright
                        _,y3 = boards[i*9+j][0].bottomleft
                        if x>=x1 and x<=x2 and y>=y1 and y<=y3:
                            if col != (255,127,80):
                                col = (255,127,80)
                                pygame.draw.rect(screen, col, boards[i*9+j][0])
                                pygame.draw.rect(screen, BLACK, boards[i*9+j][0],1)
                            l,m = i,j
                            change = True
                            boards[i*9+j][2] = True
            if event.type == KEYDOWN:
                sudoku.grid[m][l]=int(pygame.key.name(event.key))
                boards[l*9+m][1]=pygame.key.name(event.key)
                change = True
        if change:
            draw_board(boards)
    pygame.quit()

if __name__=="__main__":
    BLACK = (0, 0, 0)
    GRAY = (127, 127, 127)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}
    
    width,height=(550,600)
    sudoku=Sudoku([[0]*9 for i in range(0,9)])
    boards=[]
    
    for i in range(9):
        for j in range(9):
            boards.append([Rect(50+50*i,50+50*j,50,50),sudoku.grid[i][j],False])
    button=[Rect(width/2 - 50,525,100,50),True]

    pygame.init()
    screen = pygame.display.set_mode((width,height))
    screen.fill((255,255,255))
    pygame.display.set_caption("Sudoku Maybe!")

    draw_board(boards)

    l,m=0,0
    running = True

    solve_it(boards, True, l, m, sudoku)