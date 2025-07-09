import tkinter as ttk
from tkinter import *
import cv2
from PIL import ImageTk, Image
class VideoPlayerApp:
    def __init__(self, root, path, width=300, height=200):
        self.root = root
        self.path = path
        self.cap = cv2.VideoCapture(self.path)

        self.width = width
        self.height = height

        self.label = ttk.Label(root)
        self.label.pack()

        self.id = None

        self.playing = True

    def frame_update(self):
        if self.playing:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, [self.width, self.height])
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))

                self.label.config(image = self.photo)

                self.id = self.root.after(50, self.frame_update)
            else:
                self.cap=cv2.VideoCapture(self.path)

    def play(self):
        self.playing = True
        self.frame_update()

    def stop(self):
        self.playing = False
        self.root.after_cancel(self.id)
