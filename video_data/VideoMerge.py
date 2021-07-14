# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 16:35:29 2021

@author: HP
"""

from moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip


clip1 = VideoFileClip("death_57.mp4",audio=True)
clip2 = VideoFileClip("death_58.mp4",audio=True)
clip3 = VideoFileClip("death_60.mp4",audio=True)
clip4 = VideoFileClip("death_62.mp4",audio=True)
clip5 = VideoFileClip("death_68.mp4",audio=True)

clip6 = VideoFileClip("kill_132.mp4",audio=True)
clip7 = VideoFileClip("kill_140.mp4",audio=True)
clip8 = VideoFileClip("kill_141.mp4",audio=True)
clip9 = VideoFileClip("kill_142.mp4",audio=True)
clip10 = VideoFileClip("kill_143.mp4",audio=True)


final_clip = concatenate_videoclips([clip1, clip2, clip5, clip6, clip7, clip8, clip3,
                                     clip4, clip9, clip10], method="compose")
final_clip.write_videofile("merged.mp4")

