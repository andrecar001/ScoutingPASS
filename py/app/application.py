import tkinter as tk
from tkinter import *
import customtkinter as ctk
from customtkinter import *
import scanner_funcs
import cv2
import scouting


ctk.set_appearance_mode('Sysem')
ctk.set_default_color_theme('dark-blue')
appWidth, appHeight = 600, 700
matchScoutingPath = 'py/app/data/match_scouting_data.txt'
pitScoutingPath = 'py/app/data/pit_scouting_data.txt'
matchScoutingInfo = scouting.getAllMatchInfo(matchScoutingPath)
pitScoutingInfo = scouting.getAllMatchInfo(pitScoutingPath)
teams = scouting.getTeam('frc2508')

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.scannerPage = CTkFrame(self)
        self.dataPage = CTkFrame(self)
        self.navBar = CTkFrame(self, fg_color='black')
        self.navBar.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=0.1)
        self.scannerPage.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)
        self.dataPage.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

        self.scannerPage.tkraise()
        self.navBar.tkraise()
        self.title("ScoutingApp")
        self.geometry(f"{appWidth}x{appHeight}")

        """-------------------------------------NAVBAR-------------------------------------"""
        self.navBar.grid_rowconfigure(0,weight=1)
        self.scannerPageButton = ctk.CTkButton(self.navBar,
                                             text='Scanner',
                                             command=self.updateData,
                                             height=50,
                                             corner_radius=0,
                                             fg_color='#808080')
        
        self.scannerPageButton.grid(row=0,column=0,sticky='nswe')

        self.dataPageButton = ctk.CTkButton(self.navBar,
                                             text='Data',
                                             command=self.changePage,
                                             height=50,
                                             corner_radius=0,
                                             fg_color='black')
        self.dataPageButton.grid(row=0,column=1,sticky='nswe')

        self.unknownPageButton = ctk.CTkButton(self.navBar,
                                             text='Change Page',
                                             command=self.changePage,
                                             height=50,
                                             corner_radius=0,
                                             fg_color='black')
        self.unknownPageButton.grid(row=0,column=3,sticky='nswe')

        """-------------------------------------PAGE 1(Scanner)-------------------------------------"""
        # Pit or Match Scouting
        self.scoutingType = tk.StringVar(value="Other")
        self.matchScoutingRadioButton = ctk.CTkRadioButton(self.scannerPage, 
                                                           text='Match Scouting', 
                                                           variable=self.scoutingType,
                                                           value='Match Scouting')
        # self.matchScoutingRadioButton.grid(row=2,column=3, 
        #                                    padx=20, pady=20, 
        #                                    sticky='ew')
        self.matchScoutingRadioButton.place(relx=0.6,rely=0.5,anchor='center')
        self.pitScoutingRadioButton = ctk.CTkRadioButton(self.scannerPage,
                                                          text='Pit Scouting', 
                                                          variable=self.scoutingType,
                                                          value='Pit Scouting')
        self.pitScoutingRadioButton.place(relx=0.4,rely=0.5, anchor='center')
        
        #Upload File                              
        self.scanCodesButton = ctk.CTkButton(self.scannerPage,
                                             text='Open QRcode Scanner',
                                             command=self.scanCodesButtonPressed)
        self.scanCodesButton.place(relx=0.5,rely=0.6,anchor='center')

        self.dataLabel = ctk.CTkLabel(self.dataPage,
                                      text=teams)
        self.dataLabel.place(relx=0.5,rely=0.4,anchor='center')


        """-------------------------------------PAGE 2(Data)-------------------------------------"""
        self.updateDataButton = ctk.CTkButton(self.dataPage,
                                              text='Update Data',
                                              command=self.updateData)
        self.updateDataButton.place(relx=0.5,rely=0.8, anchor='center')

        self.teamDropDown = ctk.CTkComboBox(self.dataPage)

    """-------------------------------------FUNCTIONS-------------------------------------"""

    def scanCodesButtonPressed(self):
        if self.scoutingType.get()=='Match Scouting':
            tk.messagebox.showinfo(title='Closing Scanner',message='To close the QRcode scanner, hold \'q\'')
            scanner_funcs.openQRScanner(matchScoutingPath)
        elif self.scoutingType.get()=='Pit Scouting':
            tk.messagebox.showinfo(title='Closing Scanner',message='To close the QRcode scanner, hold \'q\'')
            scanner_funcs.openQRScanner(pitScoutingPath)
            print('Button Pressed')
        else: tk.messagebox.showerror(title='Missing Input',message='Please select the type of scouting input')

    def changePage(self):
        self.dataPageButton.configure(fg_color='#808080')
        self.scannerPageButton.configure(fg_color='black')
        self.dataPage.tkraise()
        self.navBar.tkraise()

    def updateData(self):
        self.scannerPageButton.configure(fg_color='#00008B')
        self.dataPageButton.configure(fg_color='black')
        self.scannerPage.tkraise()
        self.navBar.tkraise()
    


if __name__ == '__main__':
    app = App()
    app.mainloop()































