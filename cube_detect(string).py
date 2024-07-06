import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

color_map = {
    'W': 'white',   # 白色
    'G': 'green',   # 绿色
    'R': 'red',     # 红色
    'B': 'blue',    # 蓝色
    'O': 'orange',  # 橙色
    'Y': 'yellow'   # 黄色
}

color_string_total = []

class ColorRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Recognition")  # 设置窗口标题为"Color Recognition"
        self.camera = cv2.VideoCapture(0)  # 打开摄像头
        self.original_canvas = tk.Canvas(root, width=300, height=300)  # 创建用于显示原始图像的画布
        self.original_canvas.pack(side=tk.LEFT)
        self.recognized_canvas = tk.Canvas(root, width=300, height=300)  # 创建用于显示识别结果的画布
        self.recognized_canvas.pack(side=tk.RIGHT)
        self.recognize_button = tk.Button(root, text="Recognize Colors", command=self.recognize_colors)  # 创建识别颜色的按钮
        self.recognize_button.pack()
        self.export_button = tk.Button(root, text="Export Colors", command=self.export_colors)  # 创建导出颜色的按钮
        self.export_button.pack()
        self.update()

    def update(self):
        ret, frame = self.camera.read()  # 读取摄像头图像
        if ret:
            self.display_frame(frame, self.original_canvas)  # 在原始画布上显示图像
        self.root.after(10, self.update)  # 每隔10毫秒更新一次画面

    def recognize_colors(self):
        ret, frame = self.camera.read()  # 读取摄像头图像
        if not ret:
            return

        self.colors = self.get_grid_colors(frame)  # 获取九宫格中每个小方块的颜色
        self.draw_gui(self.colors)  # 在识别结果画布上绘制九宫格及颜色

    def get_grid_colors(self, frame):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 将图像转换为HSV颜色空间

        color_ranges = {
            'red': ((0, 100, 100), (10, 255, 255)),      # 红色的HSV范围
            'orange': ((11, 100, 100), (25, 255, 255)),  # 橙色的HSV范围
            'yellow': ((26, 100, 100), (34, 255, 255)),  # 黄色的HSV范围
            'green': ((35, 100, 100), (80, 255, 255)),   # 绿色的HSV范围
            'blue': ((81, 100, 100), (130, 255, 255)),   # 蓝色的HSV范围
            'white': ((0, 0, 200), (255, 40, 255)),      # 白色的HSV范围
        }

        colors = []

        for i in range(3):
            row_colors = []
            for j in range(3):
                cell_hsv = hsv_frame[i * 100:(i + 1) * 100, j * 100:(j + 1) * 100]  # 获取九宫格中每个小方块的HSV值
                avg_color = np.mean(cell_hsv, axis=(0, 1))  # 计算每个小方块的平均颜色
                color_name = self.detect_color(avg_color, color_ranges)  # 判断颜色名称
                row_colors.append(color_name)
            colors.append(row_colors)

        return colors

    def detect_color(self, avg_color, color_ranges):
        for color_name, (lower, upper) in color_ranges.items():
            if np.all(avg_color >= lower) and np.all(avg_color <= upper):
                return color_name
        return 'unknown'

    def draw_gui(self, colors):
        self.recognized_canvas.delete("all")  # 清空识别结果画布

        for i in range(3):
            for j in range(3):
                color = colors[i][j]
                x1, y1 = j * 100, i * 100
                x2, y2 = (j + 1) * 100, (i + 1) * 100
                fill_color = color if color != 'unknown' else 'white'

                rect_id = self.recognized_canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline='black')
                self.recognized_canvas.tag_bind(rect_id, '<Button-1>', lambda event, i=i, j=j: self.change_color_on_click(i, j))

    def display_frame(self, frame, canvas):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 将图像颜色通道从BGR转换为RGB
        image = Image.fromarray(frame)  # 创建PIL图像对象
        photo = ImageTk.PhotoImage(image=image)  # 创建Tkinter图像对象
        canvas.config(width=300, height=300)  # 设置画布大小
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)  # 在画布上显示图像
        canvas.photo = photo

    def change_color_on_click(self, i, j):
        color_dialog = tk.Toplevel(self.root)  # 创建颜色选择对话框
        color_dialog.title("选择颜色")  # 设置对话框标题为"选择颜色"

        for color_code, color_name in color_map.items():
            color_button = tk.Button(color_dialog, bg=color_name, width=10, height=2,
                                     command=lambda c=color_name: self.set_color(i, j, c))
            color_button.pack(side=tk.LEFT, padx=5, pady=5)

    def set_color(self, i, j, color):
        self.colors[i][j] = color  # 更新选定小方块的颜色
        self.draw_gui(self.colors)  # 在识别结果画布上绘制九宫格及颜色

    def export_colors(self):
        global color_string_total
        color_map = {
            "white": "U",     # 白色对应的颜色字符
            "yellow": "D",    # 黄色对应的颜色字符
            "red": "F",       # 红色对应的颜色字符
            "orange": "B",    # 橙色对应的颜色字符
            "green": "R",     # 绿色对应的颜色字符
            "blue": "L"       # 蓝色对应的颜色字符
        }

        color_sequence = []
        for i, row in enumerate(self.colors):
            for j, color in enumerate(row):
                if color in color_map:
                    letter = color_map[color]
                    color_sequence.append(letter)
                else:
                    letter = color_map["white"]
                    color_sequence.append(letter)
                    
        output_string = ''.join(color_sequence)
        print("Color sequence:", output_string)       
        color_string_total.append(color_sequence)
        
        if len(color_string_total) % 6 == 0:
            total_string = ''.join([item for sublist in color_string_total for item in sublist])
            print("识别结果:", total_string)
            color_string_total = []

if __name__ == "__main__":
    root = tk.Tk()  # 创建Tkinter窗口
    app = ColorRecognitionApp(root)  # 创建应用程序对象
    root.mainloop()  # 运行主事件循环