import kociemba
import RPi.GPIO as GPIO
import time

IN_u1 = 31
IN_u2 = 29
IN_u3 = 21
IN_u4 = 19

IN_r1 = 13
IN_r2 = 37
IN_r3 = 35
IN_r4 = 33

IN_f1 = 18
IN_f2 = 16
IN_f3 = 12
IN_f4 = 10

IN_d1 = 15
IN_d2 = 26
IN_d3 = 24
IN_d4 = 22

IN_l1 = 11
IN_l2 = 7
IN_l3 = 5
IN_l4 = 3

IN_b1 = 40
IN_b2 = 38
IN_b3 = 36
IN_b4 = 32

# u--------------------------------------------

def u_setStep(w1, w2, w3, w4):
    GPIO.output(IN_u1, w1)
    GPIO.output(IN_u2, w2)
    GPIO.output(IN_u3, w3)
    GPIO.output(IN_u4, w4)
 
def u_stop():
    u_setStep(0, 0, 0, 0)
 
def u_clockwise(delay, steps):  
    for i in range(0, steps):
        u_setStep(1, 0, 0, 0)
        time.sleep(delay)
        u_setStep(0, 1, 0, 0)
        time.sleep(delay)
        u_setStep(0, 0, 1, 0)
        time.sleep(delay)
        u_setStep(0, 0, 0, 1)
        time.sleep(delay)
 
def u_anticlockwise(delay, steps):  
    for i in range(0, steps):
        u_setStep(0, 0, 0, 1)
        time.sleep(delay)
        u_setStep(0, 0, 1, 0)
        time.sleep(delay)
        u_setStep(0, 1, 0, 0)
        time.sleep(delay)
        u_setStep(1, 0, 0, 0)
        time.sleep(delay)
        
# r--------------------------------------------

def r_setStep(w1, w2, w3, w4):
    GPIO.output(IN_r1, w1)
    GPIO.output(IN_r2, w2)
    GPIO.output(IN_r3, w3)
    GPIO.output(IN_r4, w4)
     
def r_stop():
    r_setStep(0, 0, 0, 0)
 
def r_clockwise(delay, steps):  
    for i in range(0, steps):
        r_setStep(1, 0, 0, 0)
        time.sleep(delay)
        r_setStep(0, 1, 0, 0)
        time.sleep(delay)
        r_setStep(0, 0, 1, 0)
        time.sleep(delay)
        r_setStep(0, 0, 0, 1)
        time.sleep(delay)
 
def r_anticlockwise(delay, steps):  
    for i in range(0, steps):
        r_setStep(0, 0, 0, 1)
        time.sleep(delay)
        r_setStep(0, 0, 1, 0)
        time.sleep(delay)
        r_setStep(0, 1, 0, 0)
        time.sleep(delay)
        r_setStep(1, 0, 0, 0)
        time.sleep(delay)
        
# f--------------------------------------------

def f_setStep(w1, w2, w3, w4):
    GPIO.output(IN_f1, w1)
    GPIO.output(IN_f2, w2)
    GPIO.output(IN_f3, w3)
    GPIO.output(IN_f4, w4)
     
def f_stop():
    f_setStep(0, 0, 0, 0)
 
def f_clockwise(delay, steps):  
    for i in range(0, steps):
        f_setStep(1, 0, 0, 0)
        time.sleep(delay)
        f_setStep(0, 1, 0, 0)
        time.sleep(delay)
        f_setStep(0, 0, 1, 0)
        time.sleep(delay)
        f_setStep(0, 0, 0, 1)
        time.sleep(delay)
 
def f_anticlockwise(delay, steps):  
    for i in range(0, steps):
        f_setStep(0, 0, 0, 1)
        time.sleep(delay)
        f_setStep(0, 0, 1, 0)
        time.sleep(delay)
        f_setStep(0, 1, 0, 0)
        time.sleep(delay)
        f_setStep(1, 0, 0, 0)
        time.sleep(delay)
        
# d--------------------------------------------

def d_setStep(w1, w2, w3, w4):
    GPIO.output(IN_d1, w1)
    GPIO.output(IN_d2, w2)
    GPIO.output(IN_d3, w3)
    GPIO.output(IN_d4, w4)
     
def d_stop():
    d_setStep(0, 0, 0, 0)
 
def d_clockwise(delay, steps):  
    for i in range(0, steps):
        d_setStep(1, 0, 0, 0)
        time.sleep(delay)
        d_setStep(0, 1, 0, 0)
        time.sleep(delay)
        d_setStep(0, 0, 1, 0)
        time.sleep(delay)
        d_setStep(0, 0, 0, 1)
        time.sleep(delay)
 
def d_anticlockwise(delay, steps):  
    for i in range(0, steps):
        d_setStep(0, 0, 0, 1)
        time.sleep(delay)
        d_setStep(0, 0, 1, 0)
        time.sleep(delay)
        d_setStep(0, 1, 0, 0)
        time.sleep(delay)
        d_setStep(1, 0, 0, 0)
        time.sleep(delay)
        
# l--------------------------------------------

def l_setStep(w1, w2, w3, w4):
    GPIO.output(IN_l1, w1)
    GPIO.output(IN_l2, w2)
    GPIO.output(IN_l3, w3)
    GPIO.output(IN_l4, w4)
     
def l_stop():
    l_setStep(0, 0, 0, 0)
 
def l_clockwise(delay, steps):  
    for i in range(0, steps):
        l_setStep(1, 0, 0, 0)
        time.sleep(delay)
        l_setStep(0, 1, 0, 0)
        time.sleep(delay)
        l_setStep(0, 0, 1, 0)
        time.sleep(delay)
        l_setStep(0, 0, 0, 1)
        time.sleep(delay)
 
def l_anticlockwise(delay, steps):  
    for i in range(0, steps):
        l_setStep(0, 0, 0, 1)
        time.sleep(delay)
        l_setStep(0, 0, 1, 0)
        time.sleep(delay)
        l_setStep(0, 1, 0, 0)
        time.sleep(delay)
        l_setStep(1, 0, 0, 0)
        time.sleep(delay)
        
# b--------------------------------------------

def b_setStep(w1, w2, w3, w4):
    GPIO.output(IN_b1, w1)
    GPIO.output(IN_b2, w2)
    GPIO.output(IN_b3, w3)
    GPIO.output(IN_b4, w4)
     
def b_stop():
    b_setStep(0, 0, 0, 0)
 
def b_clockwise(delay, steps):  
    for i in range(0, steps):
        b_setStep(1, 0, 0, 0)
        time.sleep(delay)
        b_setStep(0, 1, 0, 0)
        time.sleep(delay)
        b_setStep(0, 0, 1, 0)
        time.sleep(delay)
        b_setStep(0, 0, 0, 1)
        time.sleep(delay)
 
def b_anticlockwise(delay, steps):  
    for i in range(0, steps):
        b_setStep(0, 0, 0, 1)
        time.sleep(delay)
        b_setStep(0, 0, 1, 0)
        time.sleep(delay)
        b_setStep(0, 1, 0, 0)
        time.sleep(delay)
        b_setStep(1, 0, 0, 0)
        time.sleep(delay)
        
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)      
    GPIO.setup(IN_u1, GPIO.OUT)      
    GPIO.setup(IN_u2, GPIO.OUT)
    GPIO.setup(IN_u3, GPIO.OUT)
    GPIO.setup(IN_u4, GPIO.OUT)
    GPIO.setup(IN_r1, GPIO.OUT)      
    GPIO.setup(IN_r2, GPIO.OUT)
    GPIO.setup(IN_r3, GPIO.OUT)
    GPIO.setup(IN_r4, GPIO.OUT)
    GPIO.setup(IN_f1, GPIO.OUT)      
    GPIO.setup(IN_f2, GPIO.OUT)
    GPIO.setup(IN_f3, GPIO.OUT)
    GPIO.setup(IN_f4, GPIO.OUT)
    GPIO.setup(IN_d1, GPIO.OUT)      
    GPIO.setup(IN_d2, GPIO.OUT)
    GPIO.setup(IN_d3, GPIO.OUT)
    GPIO.setup(IN_d4, GPIO.OUT)
    GPIO.setup(IN_l1, GPIO.OUT)      
    GPIO.setup(IN_l2, GPIO.OUT)
    GPIO.setup(IN_l3, GPIO.OUT)
    GPIO.setup(IN_l4, GPIO.OUT)
    GPIO.setup(IN_b1, GPIO.OUT)      
    GPIO.setup(IN_b2, GPIO.OUT)
    GPIO.setup(IN_b3, GPIO.OUT)
    GPIO.setup(IN_b4, GPIO.OUT)
 
def destroy():
    GPIO.cleanup()  
    
def move_U():
    print("U: 顶层顺时针旋转90度")
    u_clockwise(0.005, 14)

def move_U2():
    print("U2: 顶层顺时针旋转180度")
    u_clockwise(0.005, 28)

def move_U_prime():
    print("U': 顶层逆时针旋转90度")
    u_anticlockwise(0.005, 14)
    
def move_R():
    print("R: 右层顺时针旋转90度")
    r_clockwise(0.005, 14)

def move_R2():
    print("R2: 右层顺时针旋转180度")
    r_clockwise(0.005, 28)

def move_R_prime():
    print("R': 右层逆时针旋转90度")
    r_anticlockwise(0.005, 14)

def move_F():
    print("F: 前层顺时针旋转90度")
    f_clockwise(0.005, 14)

def move_F2():
    print("F2: 前层顺时针旋转180度")
    f_clockwise(0.005, 28)

def move_F_prime():
    print("F': 前层逆时针旋转90度")
    l_anticlockwise(0.005, 14)

def move_D():
    print("D: 底层顺时针旋转90度")
    d_clockwise(0.005, 14)

def move_D2():
    print("D2: 底层顺时针旋转180度")
    d_clockwise(0.005, 28)

def move_D_prime():
    print("D': 底层逆时针旋转90度")
    d_anticlockwise(0.005, 14)

def move_L():
    print("L: 左层顺时针旋转90度")
    l_clockwise(0.005, 14)

def move_L2():
    print("L2: 左层顺时针旋转180度")
    l_clockwise(0.005, 28)

def move_L_prime():
    print("L': 左层逆时针旋转90度")
    l_anticlockwise(0.005, 14)

def move_B():
    print("B: 后层顺时针旋转90度")
    b_clockwise(0.005, 14)

def move_B2():
    print("B2: 后层顺时针旋转180度")
    b_clockwise(0.005, 28)

def move_B_prime():
    print("B': 后层逆时针旋转90度")
    b_anticlockwise(0.005, 14)

# 其他魔方操作函数类似地定义

def solve_cube():
    # 定义魔方的初始状态
    cube_state = 'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'
    
    # 定义魔方的末状态
    final_state = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

    # 使用Kociemba算法求解还原步骤
    solution = kociemba.solve(cube_state, final_state)

    setup()
    
    # 输出还原步骤对应的函数调用
    print("还原步骤：")
    for move in solution.split():
        if move == 'U':
            move_U()
        elif move == "U2":
            move_U2()
        elif move == "U'":
            move_U_prime()
        elif move == 'R':
            move_R()
        elif move == "R2":
            move_R2()
        elif move == "R'":
            move_R_prime()
        elif move == 'F':
            move_F()
        elif move == "F2":
            move_F2()
        elif move == "F'":
            move_F_prime()
        elif move == 'D':
            move_D()
        elif move == "D2":
            move_D2()
        elif move == "D'":
            move_D_prime()
        elif move == 'L':
            move_L()
        elif move == "L2":
            move_L2()
        elif move == "L'":
            move_L_prime()
        elif move == 'B':
            move_B()
        elif move == "B2":
            move_B2()
        elif move == "B'":
            move_B_prime()
        else:
            print("未定义的操作步骤:", move)
            
    destroy()

# 调用函数解决魔方
solve_cube()