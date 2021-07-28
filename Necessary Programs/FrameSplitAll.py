# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 23:48:33 2021

@author: HP
"""

import os
import numpy as np
import cv2
from glob import glob


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")


def save_frame(video_path, save_dir, gap=1):
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    none_path = os.path.join(save_dir, 'none', name)
    create_dir(save_path)
    create_dir(none_path)
    
    cap = cv2.VideoCapture(video_path)
    idx = 1
    
    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break


        if idx <= 10:
            filename = none_path + "_" + str(idx) + ".png"
            cv2.imwrite(filename, frame)
        elif idx > 10:
            if idx % gap == 0:
                filename = save_path + "_" + str(idx) + ".png"
                cv2.imwrite(filename, frame)

        idx += 1


if __name__ == "__main__":
    
    # All kill
    #video_paths = glob("kill/*")
    
    # All death
    #video_paths = glob("death/*")
    
    # All none
    video_paths = glob("none/*")
    
    save_dir = "frames"

    for path in video_paths:
        save_frame(path, save_dir, gap=1)
        
