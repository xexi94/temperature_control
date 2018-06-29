import tkinter as tk                # python 3
#from tkinter import font  as tkfont # python 3
import os
import PIL
from PIL import Image

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        def exit():
            self.destroy()
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        MenuBar=tk.Menu(self)
        #self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("ProgramName") #windowtitle
        self.resizable(0,0) #resizable?
        if os.name == 'nt':
            self.iconbitmap("Images/thermometer.ico") #small corner icon
        elif os.name == 'posix':
            null   
        self.geometry("850x550") #window dimension
        self.config(menu=MenuBar)
        
        

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        
        MenuFile=tk.Menu(MenuBar, tearoff=0)
        MenuFile.add_command(label="New measure",command=lambda: self.show_frame("PageOne"))
        MenuFile.add_separator()
        MenuFile.add_command(label="Export Data")
        MenuFile.add_separator()
        MenuFile.add_command(label="Close",command=lambda: self.show_frame("StartPage"))
        MenuFile.add_command(label="Exit",command=exit)

        EditFile=tk.Menu(MenuBar, tearoff=0)

        ToolFile=tk.Menu(MenuBar,tearoff=0)
        ToolFile.add_command(label="Serial Configuration",command=lambda: self.show_frame("PageTwo"))

        HelpFile=tk.Menu(MenuBar, tearoff=0)
        HelpFile.add_command(label="About ProgramName ...")
        
        MenuBar.add_cascade(label="File",menu=MenuFile)
        MenuBar.add_cascade(label="Edit",menu=EditFile)
        MenuBar.add_cascade(label="Tools",menu=ToolFile)
        MenuBar.add_cascade(label="Help",menu=HelpFile)
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page")#, font=controller.title_font
        label.pack(side="top", fill="x", pady=10)
        '''
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
        '''


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #label = tk.Label(self, text="This is the measure page")#, font=controller.title_font
        #label.pack(side="top", fill="x", pady=10)
        start = tk.Button(self)
        self.start_photo=tk.PhotoImage(file="Images/if_Right_arrow_2104160.png")
        
        start.config(image=self.start_photo,width="20",height="20")
        start.pack(side=tk.TOP,anchor=tk.W)
        '''
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        '''

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is serial configuration page")#, font=controller.title_font
        label.pack(side="top", fill="x", pady=10)
        '''
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        '''

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()