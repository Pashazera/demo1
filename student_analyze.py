import pandas as pd

data = pd.read_table('student.txt', encoding='utf-8', sep='[ \\t]+', engine='python')

print(len('13210949957032019'))


import pygame, math, time, random, os
from pygame.locals import *
from sys import exit

WINDOW_W = 1000
WINDOW_H = 600
one_time = 1    # 时间流速（默认1）
scale = 120       # 缩放（默认120）
FPS = 60        # 帧率
point_size = 2  # 点的大小
start_xy = (300, WINDOW_H // 2)  # 圆的位置

# 波形图参数
b_xy = (600, start_xy[1])  # 波形图原点坐标
b_scale = 0.8              # 波形图缩放
b_color = (200, 200, 0)    # 波形图颜色
b_length = 500             # 波形图显示的长度

#================================#
# 在此处设置函数
# 此处设置的是：f(x) = 1*sin(x) + (1/3)*sin(3x) + (1/5)*sin(5x) + ...
# 这里是一个方形波
# Set the function here
# The settings here are: f(x) = 1*sin(x) + (1/3)*sin(3x) + (1/5)*sin(5x) + ...
# Here's a square wave.
#
# A * sin(v*(θ+ω))
# A->r    v->angle_v    ω->angle
# [r, angle_v, angle]
# fourier_list = [
#     [1    ,  1, 0],
#     [1 / 3,  3, 0],
#     [1 / 5,  5, 0],
#     [1 / 7,  7, 0],
#     [1 / 9,  9, 0],
#     [1 /11, 11, 0],
#     [1 /13, 13, 0],
#     [1 /15, 15, 0],
#     [1 /17, 17, 0],
#     [1 /19, 19, 0]
# ]
fourier_list = []
for i in range(1, 1000):
    fourier_list.append([1 / i, i, 0])
#================================#

# 圆圈的颜色来自于这里，你可以随意添加、删除
color_list = [
    (255, 50, 50),
    (50, 255, 50),
    (50, 50, 255),
    (255, 255, 50),
    (255, 50, 255),
    (50, 255, 255),
    (255, 255, 255)
]

# 初始化pygame
pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 40)
# 创建一个窗口
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("傅里叶变换可视化")
font = pygame.font.SysFont('Arial', 20)
# for i in pygame.font.get_fonts():
#     print(i)

class Circle():
    x, y = 0, 0
    r = 0
    angle = 0
    angle_v = 0
    color = (0, 0, 0)
    father = None

    def __init__(self, r, angle_v, angle, color=None, father=None):
        self.r = r
        self.angle_v = angle_v
        self.angle = angle
        self.father = father
        if color is None:
            self.color = random.choice(color_list)
        else:
            self.color = color

    def set_xy(self, xy):
        self.x, self.y = xy

    def get_xy(self):
        return (self.x, self.y)

    def set_xy_by_angle(self):
        self.x = self.father.x + self.r * math.cos(self.angle) * scale
        self.y = self.father.y + self.r * math.sin(self.angle) * scale

    def run(self, step_time):
        if self.father is not None:
            self.angle += self.angle_v * step_time
            self.set_xy_by_angle()

    def draw(self, screen):
        color_an = tuple(map(lambda x: x // 3, self.color))
        # 画圆
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), point_size)
        # 画轨道
        if self.father is not None:
            pygame.draw.circle(screen, color_an, (int(self.father.x), int(self.father.y)), max(int(self.r * scale), 1),
                               1)
            pygame.draw.line(screen, self.color, (int(self.father.x), int(self.father.y)), (int(self.x), int(self.y)),
                             1)


class Boxin():
    ys = []
    def add_point(self, y):
        self.ys.append(y)
        if len(self.ys) > b_length:
            self.ys.pop(0)

    def draw(self, screen):
        # 画一个圆
        pygame.draw.circle(screen, b_color, (b_xy[0], int(b_xy[1]+self.ys[-1] * scale)), point_size)
        bl = len(self.ys)
        for i in range(bl - 1):
            pygame.draw.line(screen, b_color,
                             (b_xy[0] + int((bl - i) * b_scale), int(b_xy[1]+self.ys[i] * scale)),
                             (b_xy[0] + int((bl - i - 1) * b_scale), int(b_xy[1]+self.ys[i + 1] * scale)),
                             1)


fourier_list = sorted(fourier_list, key=lambda x: x[0], reverse=True)
super_circle = Circle(0, 0, 0)
super_circle.set_xy(start_xy)
circle_list = [super_circle]
for i in range(len(fourier_list)):
    p = fourier_list[i]
    circle_list.append(Circle(p[0], p[1], p[2], father=circle_list[i]))

bx = Boxin()
clock = pygame.time.Clock()
nnn = 0
# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key == K_LEFT and one_time>0.1:
                one_time *= 0.9
                one_time = max(one_time,0.1)
            elif event.key == K_RIGHT and one_time<10:
                one_time *= 1.1
            elif (event.key == K_EQUALS or event.key == K_PLUS) and scale<800:
                scale *= 1.1
            elif event.key == K_MINUS and scale>2:
                scale *= 0.9
                scale = max(scale,2)
            elif event.key == K_l and b_scale<10:
                b_scale *= 1.1
            elif event.key == K_k and b_scale>0.1:
                b_scale *= 0.9
                b_scale = max(b_scale,0.1)
            else:
                print(type(event.key),event.key)

    # 将背景图画上去
    screen.fill((0, 0, 0))
    # 运行
    for i, circle in enumerate(circle_list):
        circle.run(one_time / FPS)
        circle.draw(screen)

    last_circle = circle_list[-1]
    pygame.draw.line(screen, last_circle.color,
                     (int(last_circle.x), int(last_circle.y)),
                     (int(b_xy[0]), int(last_circle.y)),
                     1)
    # 画波形
    bx.add_point((last_circle.y - b_xy[1]) / scale)
    bx.draw(screen)

    # 画文字

    text_obj = font.render(r'傅里叶变换可视化', 1, (255,255,255))
    screen.blit(text_obj, (10,10))
    text_obj = font.render('左右键：加速/减速', 1, (255,255,255))
    screen.blit(text_obj, (10,35))
    text_obj = font.render('+/-键：放大/缩小', 1, (255,255,255))
    screen.blit(text_obj, (10,55))
    text_obj = font.render('L/K键：波形图放大/缩小', 1, (255,255,255))
    screen.blit(text_obj, (10,75))
    text_obj = font.render('时间速率：{:.3f},放大比例：{:.3f}'.format(one_time,scale), 1, (255,255,255))
    screen.blit(text_obj, (10,100))
    text_obj = font.render('波形图放大比例：{:.3f}'.format(b_scale), 1, (255,255,255))
    screen.blit(text_obj, (10,120))
    text_obj = font.render('FPS：{}'.format(clock.get_fps()), 1, (255,255,255))
    screen.blit(text_obj, (10,140))


    pygame.display.update()
    # pygame.image.save(screen, "./catch/catch-{:04d}.png".format(nnn))
    nnn += 1
    time_passed = clock.tick(FPS)


