import YT_VidDownloadedGIF
import customtkinter
from customtkinter import *
from pytube import YouTube
import time
import YT_DownloaderGIFs
import YT_DownloaderAskDirectory


def Streams_scrollbar(url, app):
    # Application:
    stream_window = customtkinter.CTk()
    # Set Radio Variable:
    radio_var = customtkinter.IntVar(stream_window, 0)

    # You can adjust height and width of the frame by uncommenting the line below:
    # scrollable_frame = customtkinter.CTkScrollableFrame(master=app, width=200, height=200)
    scrollable_frame = customtkinter.CTkScrollableFrame(master=stream_window, width=1000)
    scrollable_frame.grid(row=0, column=0)
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    def radiobutton_event():
        # Ask path
        path = YT_DownloaderAskDirectory.fileDir()
        # Download Progress Bar Window:
        IndividualDownload_Window = customtkinter.CTkToplevel()
        IndividualDownload_Window.lift()
        IndividualDownload_Window.wm_positionfrom()
        IndividualDownload_Window.attributes("-topmost", True)
        IndividualDownload_Window.title("Download Stats")
        x = app.winfo_x()
        y = app.winfo_y()
        IndividualDownload_Window.geometry("+%d+%d" % (x + 200, y + 200))

        # Set Progress:
        progressPercentage = customtkinter.CTkLabel(master=IndividualDownload_Window, text="0%")
        progressPercentage.pack(padx=10, pady=10)
        progressBar = customtkinter.CTkProgressBar(master=IndividualDownload_Window, width=300)
        progressBar.set(0)
        progressBar.pack(padx=10, pady=10)

        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            print(percentage_of_completion)
            str_percentage_of_completion = str(int(percentage_of_completion))

            # Update Progress:
            progressPercentage.configure(text=str_percentage_of_completion + "%")
            progressPercentage.update()

            progressBar.set(float(percentage_of_completion) / 100)
            progressBar.update()

            IndividualDownload_Window.update_idletasks()

        # Create YouTube Object
        ytObject = YouTube(url, on_progress_callback=on_progress)
        # count the streams:
        stream_number = 0
        for _ in ytObject.streams:
            print(_, "\n")
            stream_number = stream_number + 1
        print(stream_number)


        # Clear Row 3 in app:
        print("Downloading...")
        InformationLabel = customtkinter.CTkLabel(master=app, text="Downloading...", text_color="green")
        InformationLabel.grid(row=3, padx=10, pady=10)
        print("radiobutton toggled, current value:", radio_var.get())
        stream_window.destroy()
        ytObject.streams[radio_var.get()].download(path)
        time.sleep(2)
        IndividualDownload_Window.destroy()
        print("downloaded")
        InformationLabel.grid_forget()
        # Clear Row 3 in app:
        DownloadCompleteLabel = customtkinter.CTkLabel(master=app, text="Download Complete!")
        DownloadCompleteLabel.grid(row=3, padx=10, pady=10)
        DownloadCompleteLabel.after(2000, DownloadCompleteLabel.destroy)
        # YT_DownloaderGIFs.vidDownloadSuccessGIF()

    print("Trying...")
    # Define the radio buttons:
    yt_Object2 = YouTube(url)
    count = 0
    for text in yt_Object2.streams:
        customtkinter.CTkRadioButton(master=scrollable_frame, text=text,
                                     command=radiobutton_event, variable=radio_var,
                                     value=count).grid(padx=10, pady=10, sticky=W)
        count = count + 1

    stream_window.mainloop()

