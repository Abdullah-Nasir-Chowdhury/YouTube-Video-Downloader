import customtkinter
from customtkinter import *
from pytube import YouTube


# Application:
app = customtkinter.CTk()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


radio_var = customtkinter.IntVar(app, 0)
text_var = customtkinter.StringVar(app, "value", "name")
print(text_var)


# URL:
url = "https://www.youtube.com/watch?v=-QWxJ0j9EY8&ab_channel=TheCodingBug"
# Create YouTube Object
ytObject = YouTube(url)
# count the streams:
stream_number = 0
for _ in ytObject.streams:
    print(_, "\n")
    stream_number = stream_number + 1
print(stream_number)

radio_var = customtkinter.IntVar(app, 0)
text_var = customtkinter.StringVar(app, "value", "name")
print(text_var)
# You can adjust height and width of the frame by uncommenting the line below:
# scrollable_frame = customtkinter.CTkScrollableFrame(master=app, width=200, height=200)
scrollable_frame = customtkinter.CTkScrollableFrame(master=app, width=1000)
scrollable_frame.grid(row=0, column=0)


def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())
    ytObject.streams[radio_var.get()].download()
    print("downloaded")


count = 0
for _ in ytObject.streams:
    text_var = str(_)
    print(text_var)
    customtkinter.CTkRadioButton(master=scrollable_frame, text=text_var,
                                 command=radiobutton_event, variable=radio_var,
                                 value=count).grid(padx=10, pady=10, sticky=W)
    count = count + 1

app.mainloop()
