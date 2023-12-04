import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import messagebox
import threading
import g4f
import os


main_window_width = 1200
main_window_height = 500

left_frame_background_color = '#202123'
right_frame_background_color = '#444654'


top_right_frame_background_color = '#444654'
bottom_right_frame_background_color = '#404040'

fg_loading_label = 'black'
bg_loading_label = '#606060'

text_color = '#444654'

loading_flag = False
file_path = None
loading_flag = False
created = False


def center_window(window, width, height): # đừng động vào cái này !!!!!!!
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
