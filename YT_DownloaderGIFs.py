import os, tkinter
import time
from PIL import Image as PIM, ImageTk
from tkinter import *
import customtkinter
from customtkinter import *


def vidDownloadSuccessGIF():
    customtkinter.set_default_color_theme("green")
    customtkinter.set_appearance_mode("white")

    root = customtkinter.CTk()
    root.title("SCP-079")
    root.iconbitmap(r"C:\Users\HP\Desktop\ytVidDownloader\images\hitmanInsignia1.ico")
    # root.geometry("500x360")

    loco = r"C:\Users\HP\Desktop\ytVidDownloader\images\happy3.gif"
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
        root.after(100, update, ind)

    gif = Label(root)
    gif.grid(row=1, column=0)
    root.after(0, update, 0)

    gifLabel = customtkinter.CTkLabel(root, text="Downloaded Weyy!", fg_color="transparent", text_color="white")
    gifLabel.grid(row=0, column=0)
    root.mainloop()


def vidDownloadFailedGIF():
    root = customtkinter.CTk()
    root.title("SCP-079")
    root.iconbitmap(r"C:\Users\HP\Desktop\ytVidDownloader\images\hitmanInsignia1.ico")
    root.geometry("500x360")

    loco = r"C:\Users\HP\Desktop\ytVidDownloader\images\sad Dark.gif"
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
    gif.grid(row=0, column=0)
    root.after(0, update, 0)

    gifLabel = customtkinter.CTkLabel(root, text="Sowwey Download Failed!", fg_color="black",
                                      text_color="red", font=("", 24))
    gifLabel.place(relx=0.2, rely=0.1)

    root.mainloop()


# vidDownloadSuccessGIF()
# vidDownloadFailedGIF()

