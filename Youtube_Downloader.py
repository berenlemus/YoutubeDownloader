import tkinter as tk
from pytube import YouTube


def download_video():
    url = YouTube(str(yourlink.get()))
    video = url.streams.get_highest_resolution()
    # video = url.streams.first()
    # ---> if you write this code (instead of above line) it  will give you poor resolution
    video.download()
    # video.download('C:/Users/shwad/Documents/youube')
    tk.Label(root, text='Your Video is downloaded!', font='arial 15', fg="White",
             bg="#EC7063").place(x=10, y=140)


root = tk.Tk()
root.geometry("600x200")
root.config(bg="#EC7063")
root.resizable(0, 0)
# for above code, you can write window.resizable(width=False, height=False)
root.title('YouTube Video Downloader')

# this code changes the video link you enter to stringvar. yourlink is our variable
yourlink = tk.StringVar()

# we are creating two lables below

tk.Label(root, text='                   Youtube Video Downloader                    ', font='arial 20 bold',
         fg="White", bg="Black").pack()
# pack() organizes widgets in horizontal and vertical
# boxes that are limited to left, right, top, bottom positions.
tk.Label(root, text='                   Put your youtube link below                    ', font='arial 20 bold',
         fg="White", bg="purple").pack()
# insted of .pack() above, we can put .place(x=5, y=60)
# primary difference is that place lets you specify absolute coordinates,
# and pack uses a box model which allows you to place widgets along the
# sides of the box.

# code below will present blank space to type youtube link
# that textvariable is named yourlink variable (which we used applied twice)
link_enter = tk.Entry(root, width=53, textvariable=yourlink, font='arial 15 bold', bg="lightgreen").place(x=5, y=100)

# below we are creating a button that allows downloading
# command allows us to recall the def function
tk.Button(root, text='DOWNLOAD VIDEO', font='arial 15 bold', fg="white", bg='black', padx=2,
          command=download_video).place(x=385, y=140)

root.mainloop()
