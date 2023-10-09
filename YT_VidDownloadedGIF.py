import os, tkinter
import time
from PIL import Image as PIM, ImageTk
from tkinter import *
import customtkinter
from customtkinter import *


# //////////////////////        GIF         //////////////////////////
def vidDownloadSuccessGIF():
    root = customtkinter.CTk()
    root.title("SCP-079")
    root.iconbitmap(r"C:\Users\HP\Desktop\ytVidDownloader\images\hitmanInsignia1.ico")
    root.geometry("500x360")

    loco = r"C:\Users\HP\Desktop\ytVidDownloader\images\jump.gif"
    im = PIM.open(loco)
    frames_number = im.n_frames
    output = "".join("Number of frames: " + str(frames_number))
    print(output)
    ph = ImageTk.PhotoImage(master=root, image=im)
    gif = Label(master=root, image=ph)
    gif.image = ph

    frames = [PhotoImage(master=root, file=loco,
                         format='gif -index %i' % i) for i in range(frames_number)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind > frames_number - 1:
            ind = 0
        gif.configure(image=frame)
        root.after(50, update, ind)

    gif = Label(root)
    gif.grid(row=1, column=0)
    root.after(0, update, 0)

    gifLabel = customtkinter.CTkLabel(root, text="Downloaded Weyy!", fg_color="transparent", text_color="black")
    gifLabel.grid(row=0, column=0, columnspan=3)

    root.mainloop()

# ////////////////////////// GIF OVER ///////////////////////////

# vidDownloadedGIF()
