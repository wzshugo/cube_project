import RPi.GPIO as GPIO
import time

# 定义引脚编号
IN1 = 12    # 引脚11
IN2 = 11    # 引脚12
IN3 = 15    # 引脚15
IN4 = 13    # 引脚13

def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)    # 设置引脚IN1的输出状态
    GPIO.output(IN2, w2)    # 设置引脚IN2的输出状态
    GPIO.output(IN3, w3)    # 设置引脚IN3的输出状态
    GPIO.output(IN4, w4)    # 设置引脚IN4的输出状态

def stop():
    setStep(0, 0, 0, 0)     # 停止电机转动，将所有引脚置为低电平

def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 0)     # 步进电机顺时针转动一步
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)

def backward(delay, steps):
    for i in range(0, steps):
        setStep(0, 0, 0, 1)     # 步进电机逆时针转动一步
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # 设置引脚编号模式为物理引脚编号
    GPIO.setup(IN1, GPIO.OUT)      # 设置引脚为输出模式
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def loop():
    while True:
        print("backward...")        # 输出提示信息
        backward(0.005, 14)         # 向后转动步进电机，共转动14步，约为逆时针转动90度

        print("stop...")
        stop()                      # 停止步进电机的转动
        time.sleep(3)               # 等待3秒

        print("forward...")
        forward(0.005, 14)          # 向前转动步进电机，共转动14步，约为顺时针转动90度

        print("stop...")
        stop()                      # 停止步进电机的转动
        time.sleep(3)               # 等待3秒

def destroy():
    GPIO.cleanup()                  # 清理GPIO资源

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:       # 捕获键盘中断异常，执行清理操作
        destroy()