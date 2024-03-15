import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from customtkinter import *
import scanner_funcs
import cv2
import information
import excel_manipulation
import os

ctk.set_appearance_mode('Sysem')
ctk.set_default_color_theme('dark-blue')
appWidth, appHeight = 300, 150
allScoutingPath = 'py/app/data/all_scouting_data.txt'
matchScoutingPath = 'py/app/data/match_scouting_data.txt'
pitScoutingPath = 'py/app/data/pit_scouting_data.txt'
excelWorkbookPath = 'py/app/data/Test.xlsx'
excelWorkbookPath = os.path.abspath(excelWorkbookPath)
matchScoutingInfo = information.getAllMatchInfoList(matchScoutingPath)
pitScoutingInfo = information.getAllMatchInfoList(pitScoutingPath)
teams = information.getTeam('frc2508')

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.scannerPage = CTkFrame(self)
        self.dataPage = CTkFrame(self)
        self.navBar = CTkFrame(self, fg_color='black')
        # self.navBar.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=0.05)
        self.scannerPage.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)
        # self.scannerPage.pack(pady=40)
        self.dataPage.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

        self.scannerPage.lift()
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
        # self.matchScoutingRadioButton.place(relx=0.3,rely=0.2,anchor='center')
        self.pitScoutingRadioButton = ctk.CTkRadioButton(self.scannerPage,
                                                          text='Pit Scouting', 
                                                          variable=self.scoutingType,
                                                          value='Pit Scouting')
        # self.pitScoutingRadioButton.place(relx=0.7,rely=0.2, anchor='center')
        
        #Upload File                              
        self.scanCodesButton = ctk.CTkButton(self.scannerPage,
                                             text='Open QRcode Scanner',
                                             command=self.scanCodesButtonPressed)
        self.scanCodesButton.place(relx=0.5,rely=0.4,anchor='center')
        # self.scanCodesButton.pack(pady=40)

        self.updateSheets = ctk.CTkButton(self.scannerPage,
                                              text="Update Spreadsheet",
                                              command=self.updateSheet)
        self.updateSheets.place(relx=0.5,rely=0.6,anchor='center')

        self.openExcelButton = ctk.CTkButton(self.scannerPage,
                                             text='Open Excel Workbook',
                                             command=self.openExcelButtonPressed)
        self.openExcelButton.place(relx=0.5,rely=0.8,anchor='center')



        """-------------------------------------PAGE 2(Data)-------------------------------------"""
        self.updateTeamButton = ctk.CTkButton(self.dataPage,
                                              text='Update Data',
                                              command=self.changeTeam)
        self.updateTeamButton.place(relx=0.5,rely=0.8, anchor='center')

        self.dataComboBox = ctk.CTkEntry(self.dataPage)
        # self.dataComboBox.bind('<<ComboboxSelected>>', self.changeTeam)
        self.dataComboBox.place(relx=0.5,rely=0.4,anchor='center')
        
        self.dataLabel = ctk.CTkLabel(self.dataPage, text='Team Location')

        self.dataLabel.place(relx=0.5,rely=0.6,anchor='center')

    """-------------------------------------FUNCTIONS-------------------------------------"""

    def scanCodesButtonPressed(self):
        tk.messagebox.showinfo(title='Closing Scanner',message='To close the QRcode scanner, hold \'q\'')
        scanner_funcs.openQRScanner(allScoutingPath)
        # if self.scoutingType.get()=='Match Scouting':
        #     tk.messagebox.showinfo(title='Closing Scanner',message='To close the QRcode scanner, hold \'q\'')
        #     scanner_funcs.openQRScanner(matchScoutingPath)
        # elif self.scoutingType.get()=='Pit Scouting':
        #     tk.messagebox.showinfo(title='Closing Scanner',message='To close the QRcode scanner, hold \'q\'')
        #     scanner_funcs.openQRScanner(pitScoutingPath)
        #     print('Button Pressed')
        # else: tk.messagebox.showerror(title='Missing Input',message='Please select the type of scouting input')
        return
    
    def changePage(self):
        self.dataPageButton.configure(fg_color='#808080')
        self.scannerPageButton.configure(fg_color='black')
        self.dataPage.lift()
        self.dataPage.tkraise()
        self.navBar.tkraise()

    def updateData(self):
        self.scannerPageButton.configure(fg_color='#00008B')
        self.dataPageButton.configure(fg_color='black')
        self.scannerPage.tkraise()
        self.navBar.tkraise()
    
    def changeTeam(self):
        print('Combo Changed')
        self.dataLabel.configure(text=information.getTeam(f'frc{self.dataComboBox.get()}').city)

    def updateSheet(self):
        try:
            excel_manipulation.populateSheet()
            tk.messagebox.showinfo(title='Sheet Update',message='Spreadsheet successfully updated')
        except PermissionError:
            tk.messagebox.showerror(title='Error',message='Please Close the spreadsheet')

    def openExcelButtonPressed(self):
        if os.path.exists(excelWorkbookPath):
            os.startfile(excelWorkbookPath)
        else:
            tk.messagebox.showinfo(title='File Not Found',message='Excel File not found')
        return

if __name__ == '__main__':
    app = App()
    app.mainloop()
