# pip install pyautogui

from time import sleep

import pyautogui
import time

def bbox_to_coords(bbox, screen_width, screen_height):
    """将 bbox 坐标转换为屏幕坐标."""
    xmin, ymin, xmax, ymax = bbox
    x_center = int((xmin + xmax) / 2 * screen_width)
    y_center = int((ymin + ymax) / 2 * screen_height)
    return x_center, y_center

def click_bbox(bbox):
    """点击指定的 bbox."""
    screen_width, screen_height = pyautogui.size()
    x, y = bbox_to_coords(bbox, screen_width, screen_height)

    # 移动鼠标到指定位置
    pyautogui.moveTo(x, y, duration=0.2)  # duration 是移动时间，单位为秒

    # 点击鼠标
    pyautogui.click()

    print(f"点击了坐标: x={x}, y={y}")

if __name__ == '__main__':

    sleep(5)

    # 示例 bbox (来自您提供的数据)
    bbox = [0.36728453636169434, 0.9408491849899292, 0.39909330010414124, 0.9875121712684631] # chrome

    # 点击 bbox
    click_bbox(bbox)
