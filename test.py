import RPi.GPIO as GPIO
import time

# 定义步进电机控制引脚
PINS = [31, 29, 21, 19, 13, 37, 35, 33, 18, 16, 12, 10, 15, 26, 24, 22, 11, 7, 5, 3, 40, 38, 36, 32]

# 初始化GPIO引脚
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PINS, GPIO.OUT)

# 清理GPIO引脚
def destroy():
    GPIO.cleanup()

# 设置步进电机状态
def set_step(pin1, pin2, pin3, pin4):
    GPIO.output(PINS, GPIO.LOW)
    GPIO.output([pin1, pin2, pin3, pin4], GPIO.HIGH)

# 顺时针旋转步进电机
def rotate_clockwise(delay, steps, pin1, pin2, pin3, pin4):
    for _ in range(steps):
        set_step(pin1, pin2, pin3, pin4)
        time.sleep(delay)
        pin1, pin2, pin3, pin4 = pin4, pin1, pin2, pin3

# 逆时针旋转步进电机
def rotate_counterclockwise(delay, steps, pin1, pin2, pin3, pin4):
    for _ in range(steps):
        set_step(pin1, pin2, pin3, pin4)
        time.sleep(delay)
        pin1, pin2, pin3, pin4 = pin2, pin3, pin4, pin1

# 定义旋转函数
def move(direction, clockwise=True):
    print(f"{direction}: {'' if clockwise else '逆'}时针旋转90度")
    pins = {
        'U': (31, 29, 21, 19),
        'R': (13, 37, 35, 33),
        'F': (18, 16, 12, 10),
        'D': (15, 26, 24, 22),
        'L': (11, 7, 5, 3),
        'B': (40, 38, 36, 32)
    }
    delay = 0.005
    steps = 14 if clockwise else -14
    rotate_clockwise(delay, steps, *pins[direction])

# 定义各个方向的旋转函数
def move_U():
    move('U')

def move_U_prime():
    move('U', clockwise=False)

def move_R():
    move('R')

def move_R_prime():
    move('R', clockwise=False)
    
def move_F():
    move('F')

def move_F_prime():
    move('F', clockwise=False)
    
def move_D():
    move('D')

def move_D_prime():
    move('D', clockwise=False)
    
def move_L():
    move('L')

def move_L_prime():
    move('L', clockwise=False)
    
def move_B():
    move('B')

def move_B_prime():
    move('B', clockwise=False)