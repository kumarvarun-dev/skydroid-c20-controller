import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import cv2
import threading
import socket


CAMERA_IP = "192.168.144.108"
UDP_PORT = 9002

RTSP_URL = "rtsp://192.168.144.108:554/stream=1"


class C20Controller:

    def __init__(self):
        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

    def send(self, cmd):
        self.sock.sendto(
            cmd.encode(),
            (CAMERA_IP, UDP_PORT)
        )

        print(cmd)


class App:

    def __init__(self, root):

        self.root = root
        self.root.title("Skydroid C20 Ground Station")
        self.root.geometry("1400x800")

        self.ctrl = C20Controller()

        self.video_label = tk.Label(root)
        self.video_label.pack(side=tk.LEFT,
                              fill=tk.BOTH,
                              expand=True)

        right = tk.Frame(root)
        right.pack(side=tk.RIGHT,
                   fill=tk.Y)

        self.create_gimbal(right)
        self.create_camera(right)
        self.create_log(right)

        self.cap = cv2.VideoCapture(RTSP_URL)

        self.update_video()

    def send(self, cmd):

        self.ctrl.send(cmd)

        self.log.insert(
            tk.END,
            cmd + "\n"
        )

        self.log.see(tk.END)

    def create_gimbal(self, parent):

        frame = tk.LabelFrame(
            parent,
            text="Gimbal"
        )

        frame.pack(
            fill=tk.X,
            padx=5,
            pady=5
        )

        tk.Button(
            frame,
            text="UP",
            width=10,
            command=lambda:
            self.send("#TPUG2wPTZ01")
        ).grid(row=0, column=1)

        tk.Button(
            frame,
            text="LEFT",
            width=10,
            command=lambda:
            self.send("#TPUG2wPTZ03")
        ).grid(row=1, column=0)

        tk.Button(
            frame,
            text="STOP",
            width=10,
            command=lambda:
            self.send("#TPUG2wPTZ00")
        ).grid(row=1, column=1)

        tk.Button(
            frame,
            text="RIGHT",
            width=10,
            command=lambda:
            self.send("#TPUG2wPTZ04")
        ).grid(row=1, column=2)

        tk.Button(
            frame,
            text="DOWN",
            width=10,
            command=lambda:
            self.send("#TPUG2wPTZ02")
        ).grid(row=2, column=1)

        tk.Button(
            frame,
            text="CENTER",
            width=15,
            command=lambda:
            self.send("#TPUG2wPTZ09")
        ).grid(
            row=3,
            column=0,
            columnspan=3,
            pady=5
        )

    def create_camera(self, parent):

        frame = tk.LabelFrame(
            parent,
            text="Camera"
        )

        frame.pack(
            fill=tk.X,
            padx=5,
            pady=5
        )

        tk.Button(
            frame,
            text="PHOTO",
            width=15,
            command=lambda:
            self.send("#TPUD2wCAP01")
        ).pack(pady=2)

        tk.Button(
            frame,
            text="REC START",
            width=15,
            command=lambda:
            self.send("#TPUD2wREC01")
        ).pack(pady=2)

        tk.Button(
            frame,
            text="REC STOP",
            width=15,
            command=lambda:
            self.send("#TPUD2wREC00")
        ).pack(pady=2)

        tk.Button(
            frame,
            text="ZOOM +",
            width=15,
            command=lambda:
            self.send("#TPUD2wDZM0A")
        ).pack(pady=2)

        tk.Button(
            frame,
            text="ZOOM -",
            width=15,
            command=lambda:
            self.send("#TPUD2wDZM0B")
        ).pack(pady=2)

        #tk.Button(
        #    frame,
        #    text="LED ON",
        #    width=15,
        #    command=lambda:
        #    self.send("#tpUD4wEXT0001")
        #).pack(pady=2)
#
        #tk.Button(
        #    frame,
        #    text="LED OFF",
        #    width=15,
        #    command=lambda:
        #    self.send("#tpUD4wEXT0000")
        #).pack(pady=2)

    def create_log(self, parent):

        frame = tk.LabelFrame(
            parent,
            text="Log"
        )

        frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=5
        )

        self.log = scrolledtext.ScrolledText(
            frame,
            height=15
        )

        self.log.pack(
            fill=tk.BOTH,
            expand=True
        )

    def update_video(self):

        ret, frame = self.cap.read()

        if ret:

            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            img = Image.fromarray(frame)

            img = img.resize(
                (1000, 700)
            )

            photo = ImageTk.PhotoImage(img)

            self.video_label.configure(
                image=photo
            )

            self.video_label.image = photo

        self.root.after(
            10,
            self.update_video
        )


root = tk.Tk()
app = App(root)
root.mainloop()