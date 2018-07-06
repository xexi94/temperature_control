import tkinter as tk                # python 3
from tkinter import filedialog
#from tkinter import font  as tkfont # python 3
import os
#import PIL
#from PIL import Image

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        def exit():
            self.destroy()
        
        
        def popupmsg():
            popup = tk.Tk()
            popup.resizable(0,0)
            popup.geometry("200x100")
            if os.name == 'nt':
                popup.iconbitmap("Images/thermometer.ico") 
            elif os.name == 'posix':
                b=0 # see how to add logo
            popup.wm_title("")
            message=tk.Label(popup,text="description")
            Bl = tk.Button(popup,text="Okay",command=popup.destroy)
            message.pack()
            Bl.pack(side=tk.BOTTOM,pady=4)
            popup.mainloop()
        def file_save():
            if os.name == 'posix':
                f = filedialog.asksaveasfilename(initialdir = "/media/sergi/HDD/AN/INTSRUMENTS/temperature_control",title = "Save file",filetypes = (("Text files","*.txt"),("all files","*.*")))
            elif os.name == 'nt':
                f = filedialog.asksaveasfilename(initialdir = "C:/",title = "Save file",filetypes = (("Text files","*.txt"),("all files","*.*")))
            
            if f is None:
                return None
            else:
                file = open(f,'w')
                file.write(self.variable)
                

        tk.Tk.__init__(self, *args, **kwargs)    
        MenuBar=tk.Menu(self)
        #self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("ProgramName")
        self.variable = "Hellomellow" 
        self.resizable(0,0) 
        if os.name == 'nt':
            self.iconbitmap("Images/thermometer.ico") 
        elif os.name == 'posix':
            b=0   
        self.geometry("850x550") 
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
        MenuFile.add_command(label="Export Data",command=file_save)
        MenuFile.add_separator()
        MenuFile.add_command(label="Close",command=lambda: self.show_frame("StartPage"))
        MenuFile.add_command(label="Exit",command=exit)

        EditFile=tk.Menu(MenuBar, tearoff=0)

        ToolFile=tk.Menu(MenuBar,tearoff=0)
        ToolFile.add_command(label="Serial Configuration",command=lambda: self.show_frame("PageTwo"))

        HelpFile=tk.Menu(MenuBar, tearoff=0)
        HelpFile.add_command(label="About ProgramName ...",command=popupmsg)
        
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
        
        def option_changed(*args):
            #print (self.option.get())
            
            return self.option.get() 
        tk.Frame.__init__(self, parent)
        
        def _create_circle(self, x, y, r, **kwargs):
            return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
        tk.Canvas.create_circle = _create_circle
        self.controller = controller
        #label = tk.Label(self, text="This is the measure page")#, font=controller.title_font
        #label.pack(side="top", fill="x", pady=10)
        
        # BUTTONS
        start = tk.Button(self)
        self.start_photo=tk.PhotoImage(file="Images/if_Right_arrow_2104160.png")
        start.config(image=self.start_photo,width="20",height="20")
        stop = tk.Button(self)
        self.stop_photo=tk.PhotoImage(file="Images/if_Arrows_62_2104119.png")
        stop.config(image=self.stop_photo,width="20",height="20")
        restart = tk.Button(self)
        self.restart_photo=tk.PhotoImage(file="Images/if_Arrow_42_2104127.png")
        restart.config(image=self.restart_photo,width="20",height="20")
        aux1 = tk.Button(self)
        self.aux1_photo=tk.PhotoImage(file="Images/if_Arrow_21_2104182.png")
        aux1.config(image=self.aux1_photo,width="20",height="20")
        aux2 = tk.Button(self)
        aux2.config(image=self.aux1_photo,width="20",height="20")
        aux3 = tk.Button(self)
        aux3.config(image=self.aux1_photo,width="20",height="20")
        aux4 = tk.Button(self)
        aux4.config(image=self.aux1_photo,width="20",height="20")
        aux5 = tk.Button(self)
        aux5.config(image=self.aux1_photo,width="20",height="20")
        aux6 = tk.Button(self)
        aux6.config(image=self.aux1_photo,width="20",height="20")
        aux7 = tk.Button(self)
        aux7.config(image=self.aux1_photo,width="20",height="20")
        
        start.pack(side=tk.LEFT,anchor=tk.N)
        stop.pack(side=tk.LEFT,anchor=tk.N)
        restart.pack(side=tk.LEFT,anchor=tk.N)
        aux1.pack(side=tk.LEFT,anchor=tk.N)
        aux2.pack(side=tk.LEFT,anchor=tk.N)
        aux3.pack(side=tk.LEFT,anchor=tk.N)
        aux4.pack(side=tk.LEFT,anchor=tk.N)
        aux5.pack(side=tk.LEFT,anchor=tk.N)
        aux6.pack(side=tk.LEFT,anchor=tk.N)
        aux7.pack(side=tk.LEFT,anchor=tk.N)

        # GRAPH OPTIONS SELCTOR
        self.option = tk.StringVar(self)
        self.option.set("Temperature")
        self.option.trace("w",option_changed)
        
        w=tk.OptionMenu(self,self.option,"Temperature","Intensity","Voltage","Resistance")
        #w.config(width="20")
        w.pack(side=tk.RIGHT,anchor=tk.N)
        
        # SERIAL LED
        self.state=True
        serial_text = tk.Label(self, text="Serial Connection")
        serial_text.pack(side=tk.LEFT,anchor=tk.N,padx="20",pady="3")
        canvas = tk.Canvas(self, width=25, height=25)
        if self.state != False:
            canvas.create_circle(13,13,6, fill="green2",outline="black",width=1)
        else:
            canvas.create_circle(13,13,6,outline="black",width=1)
        canvas.pack(side=tk.LEFT,anchor=tk.N)
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