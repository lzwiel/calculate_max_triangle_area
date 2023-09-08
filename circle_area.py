import math

def calculate_max_triangle_area(circle_area):
    # 计算最大半径
    radius = math.sqrt(circle_area / math.pi)
    
    # 计算最大边长
    triangle_side = 2 * radius
    
    # 计算最大高度
    triangle_height = radius
    
    # 计算最大三角形的面积
    triangle_area = (triangle_side * triangle_height) / 2
    
    return triangle_area

# 输入圆的面积
circle_area = float(input("请输入圆的面积："))

max_triangle_area = calculate_max_triangle_area(circle_area)
print("在圆内能够画出的最大三角形的面积：", max_triangle_area)
