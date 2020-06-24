# Import Library
import tkinter as tk
import tkinter.font as tkFont


class VideoToAudio(tk.Frame):
    # Constructor
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master

        # Display the application title
        self.AppTitle()

        # Define the application window size
        self.AppSize()

        # This is the body of the application itself
        self.create_widget()


    def AppTitle(self):
        # Setting the title of the Application
        self.master.title("MP4 to MP3 Converter")


    def AppSize(self):
        self.master.geometry("700x500")


    def create_widget(self):
        # Font Style
        fontStyleTitle = tkFont.Font(family = "Times", size = 24, weight = "bold")
        fontStyleInner = tkFont.Font(family = "Times", size = 12, weight = "normal")

        # This will center the text
        self.master.grid_columnconfigure(0, weight = 1)

        # Inner Title
        self.inner_title = tk.Label(text = "MP4 to MP3 Converter", font = fontStyleTitle)
        self.inner_title.grid(row = 0, column = 0)

        # Prompt User for MP4 file
        self.select_mp4_file_label = tk.Label(text = "Select the mp4 file you wish to convert",
            font = fontStyleInner)
        self.select_mp4_file_label.grid(row = 2, column = 0, sticky = 'w')



root = tk.Tk()
app = VideoToAudio(master = root)
app.mainloop()
