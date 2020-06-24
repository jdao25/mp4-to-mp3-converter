# Import Library
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog


class VideoToAudio(tk.Frame):
    # Constructor
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.mainframe = None
        # self.filePath = None
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
        self.master.geometry('700x500')


    def configure_mainframe(self):
        '''
            Configure the mainframe in the root
        '''

        self.mainframe = tk.Frame(self.master, background = 'white')
        self.mainframe.grid(row = 0, column = 0, sticky = ('N', 'S', 'E', 'W'))
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 0)
        self.mainframe.rowconfigure(1, weight = 1)
        self.mainframe.rowconfigure(2, weight = 1)
        self.mainframe.rowconfigure(3, weight = 1)


    def configure_banner(self):
        '''
            Configure the application title banner
        '''

        banner = tk.Label(self.mainframe, background = 'black',
            text = "MP4 to MP3 Converter", font = ('Times', 32, 'bold'), fg = 'white')
        banner.grid(row = 0, column = 0, sticky = ('N', 'S', 'E', 'W'),
            padx = 5, pady = 5)


    def configure_body(self):
        '''
            Configure the appliation user inputs
            Prompt user for the mp4 file to convert
        '''

        input_frame = tk.Frame(self.mainframe, background = 'white',
            borderwidth = 2, relief = 'flat')
        input_frame.grid(row = 1, column = 0, sticky = ('N', 'S', 'E', 'W'))
        input_frame.columnconfigure(0, weight = 1)
        input_frame.columnconfigure(1, weight = 1)
        input_frame.columnconfigure(2, weight = 1)
        input_frame.rowconfigure(0, weight = 1)
        input_frame.rowconfigure(1, weight = 1)

        # Ask user to select file to convert
        mp4_file = tk.Entry(input_frame, width = 50, borderwidth = 2)
        mp4_file.grid(row = 0, column = 0)
        user_upload_text = "Select MP4 file you want to convert"
        mp4_file.insert(0, user_upload_text)

        # User upload mp4 file to convert
        def uploadFile(event = None):
            mp4_filename = filedialog.askopenfilename()
            mp4_file.delete(0, len(user_upload_text))
            mp4_file.insert(0, mp4_filename)

        upload_mp4 = tk.Button(input_frame, text = "Open", command = uploadFile)
        upload_mp4.grid(row = 0, column = 1)

        # Ask user to set new mp3 filename
        mp3_file = tk.Entry(input_frame, width = 50, borderwidth = 2)
        mp3_file.grid(row = 1, column = 0)
        user_download_text = "Type your mp3 filename"
        mp3_file.insert(0, user_download_text)
        mp3_file.icursor(0)

        def downloadFile(event = None):
            mp3_filename = None
            print("Downloaded")

        download_mp3 = tk.Button(input_frame, text = "Convert", command = downloadFile)
        download_mp3.grid(row = 1, column = 1)


root = tk.Tk()
app = VideoToAudio(master = root)
app.mainloop()
