import tkinter as tk                # python 3
from tkinter import filedialog
import serial
import os

'''
ser = serial.Serial('/dev/ttyACM0', 9600) # device, BAUD

while True:

    data = ser.readline()
    if data:
        print(data)

'''
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)    
        #MenuBar=tk.Menu(self)
        #self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("ProgramName")
        self.variable = "Hellomellow" 
        self.resizable(0,0)

        if os.name == 'nt':
            self.iconbitmap("Images/thermometer.ico") 
        elif os.name == 'posix':
            b=0   
        self.geometry("850x550") 
        #self.config(menu=MenuBar)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (MainPage,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    
class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the main page")#, font=controller.title_font
        label.pack(side="top", fill="x", pady=10)

        #Device selection
        optionList=["     "]
        if os.name == 'nt':
        	None
            
        elif os.name == 'posix':
        	lines = os.popen("dmesg | grep tty").readlines()
        	for i in lines:
        		aux = i[i.find('tty')::]
        		device = aux[0:(aux.find(" "))-1]
        		if (bool(os.popen("test -e /dev/"+device+" && echo True || echo False").readlines()) == True):
        			optionList.append(device)
        		else:
        			optionList.append("     ")
        	optionList = list(set(optionList))
        	
        		
        #optionList = ["ttyS0","ttyUSB1","ttyASM0","ttyS0"]
        self.option = tk.StringVar(self)
        self.option.set(optionList[0])
        #self.option.trace("w",option_changed)
        
        w=tk.OptionMenu(self,self.option,*optionList)
        #w.config(width="20")
        w.pack(side=tk.LEFT,anchor=tk.N)
        
        '''
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
        '''

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
