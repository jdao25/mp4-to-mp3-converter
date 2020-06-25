# Import Library
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import messagebox
import os
from moviepy.editor import *


class VideoToAudio(tk.Frame):
    # Constructor
    def __init__(self, master = None):
        # Call the constructor of the parent class (tkinter)
        super().__init__(master)
        self.master = master
        self.master.title("MP4 to MP3 Converter")
        self.mainframe = None
        self.set_up()


    def set_up(self):
        '''
            Run view and widget configuration functions
        '''

        self.configure_root()
        self.configure_mainframe()
        self.configure_banner()
        self.configure_body()


    def configure_root(self):
        '''
            Run root window of the application
        '''

        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight = 1)
        self.master.geometry('500x300')


    def configure_mainframe(self):
        '''
            Configure the mainframe in the root
        '''

        self.mainframe = tk.Frame(self.master, background = 'white')
        self.mainframe.grid(row = 0, column = 0, sticky = ('N', 'S', 'E', 'W'))
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 0)

        for i in range(1, 4):
            self.mainframe.rowconfigure(i, weight = 1)


    def configure_banner(self):
        '''
            Configure the application title banner
        '''

        banner = tk.Label(self.mainframe, background = 'black',
            text = "MP4 to MP3 Converter", font = ('Times', 32, 'bold'), fg = 'white')

        banner.grid(row = 0, column = 0, sticky = ('N', 'S', 'E', 'W'),
            padx = 10, pady = 10)


    def configure_body(self):
        '''
            Configure the appliation user inputs
            Prompt user for the mp4 file to convert, etc.
        '''

        input_frame = tk.Frame(self.mainframe, background = 'white',
            borderwidth = 2, relief = 'flat')
        input_frame.grid(row = 1, column = 0, sticky = ('N', 'S', 'E', 'W'))

        for i in range(3):
            input_frame.columnconfigure(i, weight = 1)

        for i in range(2):
            input_frame.rowconfigure(i, weight = 1)

        # Ask user to select file to convert
        mp4_file = tk.Entry(input_frame, width = 40, borderwidth = 2)
        mp4_file.grid(row = 0, column = 0)
        mp4_file.insert(0, "Choose a file to convert")

        # User upload mp4 file to convert
        def uploadFile(event = None):
            filename = filedialog.askopenfilename(filetypes = [('MPEG4 video file', '*.mp4')])
            mp4_file.delete(0, 'end')
            mp4_file.insert(0, filename)

            # File
            file = mp4_file.get()

            filename = file[file.rfind('/') + 1 : file.rfind('.')] if (os.name != 'nt') \
                else file[file.rfind('\\') + 1 : file.rfind('.')]

            uploaded(filename)

        upload_mp4 = tk.Button(input_frame, text = "Open", command = uploadFile)
        upload_mp4.grid(row = 0, column = 1)

        # Ask user to set new mp3 filename
        mp3_file = tk.Entry(input_frame, width = 40, borderwidth = 2)
        mp3_file.grid(row = 1, column = 0)
        mp3_file.insert(0, 'default.mp3')

        def uploaded(filename):
            mp3_file.delete(0, 'end')
            mp3_file.insert(0, filename + '.mp3')

        def downloadFile(event = None):
            file = mp4_file.get()
            file_path = file[ : file.rfind('/') + 1] if (os.name != 'nt') \
                else file[ : file.rfind('\\')]

            if '.mp4' in file:
                print(f"Converting {mp4_file.get()} to {file_path}{mp3_file.get()}")

                wait_message = tk.messagebox.showinfo(title = "File converting",
                    message = "Please wait while file is being converted to mp3")

                # Start converting using moviepy
                video_clip = VideoFileClip(mp4_file.get()) # The mp4 file (video)
                audio_clip = video_clip.audio # Extracting the audio from mp4 file
                audio_clip.write_audiofile(file_path + mp3_file.get())

                audio_clip.close()
                video_clip.close()

                complete_frame = tk.Frame(self.mainframe, background = 'white')
                complete_frame.grid(row = 2, column = 0, sticky = ('N', 'S', 'E', 'W'))

                for i in range(3):
                    complete_frame.columnconfigure(i, weight = 1)

                for i in range(2):
                    complete_frame.rowconfigure(i, weight = 1)

                complete_message = tk.Label(self.mainframe, text = "Done",
                    font = ('Times', 32), fg = 'Blue', background = 'white')
                complete_message.grid(row = 3, column = 0, sticky = ('N', 'S', 'W', 'E'))
            else:
                mp4_file.delete(0, 'end')
                mp4_file.insert(0, 'Please choose a file')

        download_mp3 = tk.Button(input_frame, text = "Convert", command = downloadFile)
        download_mp3.grid(row = 1, column = 1)


root = tk.Tk()
app = VideoToAudio(master = root)
app.mainloop()
