import tkinter as tk
from tkinter import *
import customtkinter as ctk
from customtkinter import *
import scanner_funcs
import cv2
class DotDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
def getAllMatchInfo():
#Create Dictionary
    scouting_info = []

    with open('py/qrscanner/allStrings.txt','r') as file:
        lines = file.readlines()
        
        for line in lines:
            line_array = line.split('\t')
            line_info = DotDict()
            line_info['key'] = 'frc' + str(line_array[5])
            line_info['initials'] = line_array[0]
            line_info['event'] = line_array[1]
            line_info['match_level'] = line_array[2]
            line_info['match_number'] = line_array[3]
            line_info['robot_number'] = line_array[4]
            line_info['team_number'] = line_array[5]
            line_info['auto_start_position'] = line_array[6]
            line_info['left_starting_zone'] = line_array[7]
            line_info['auto_amp_score'] = line_array[8]
            line_info['auto_speaker_score'] = line_array[9]
            line_info['teleop_amp_score'] = line_array[10]
            line_info['teleop_speaker_score'] = line_array[11]
            line_info['times_amplified'] = line_array[12]
            line_info['pickup_from'] = line_array[13]
            line_info['climb_time'] = line_array[14]
            line_info['climb_status'] = line_array[15]
            line_info['trap_status'] = line_array[16]
            line_info['driver_skill'] = line_array[17]
            line_info['defense_rating'] = line_array[18]
            line_info['speed_rating'] = line_array[19]
            line_info['immobilized'] = line_array[20]
            line_info['tippy'] = line_array[21]
            line_info['dropped_notes_status'] = line_array[22]
            line_info['good_partner'] = line_array[23]
            line_info['comment'] = line_array[24].rstrip('\n')
            line_info = DotDict(line_info)
            scouting_info.append(line_info)
    return scouting_info


ctk.set_appearance_mode('Sysem')
ctk.set_default_color_theme('dark-blue')
appWidth, appHeight = 600, 700
matchScoutingPath = 'py/app/data/match_scouting_data.txt'
pitScoutingPath = 'py/app/data/pit_scouting_data.txt'
def button_function():
    print('To be made')

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

        """-------------------------------------PAGE 2(Data)-------------------------------------"""
        self.updateDataButton = ctk.CTkButton(self.dataPage,
                                              text='Update Data',
                                              command=self.updateData)
        self.updateDataButton.place(relx=0.5,rely=0.8, anchor='center')

    def scanCodesButtonPressed(self):
        if self.scoutingType.get()=='Match Scouting':
            tk.messagebox.showinfo(title='Closing Scanner',message='To close the QRcode scanner, hold \'q\'')
            scanner_funcs.openQRScanner(matchScoutingPath)
        elif self.scoutingType.get()=='Pit Scouting':
            tk.messagebox.showinfo(title='Closing Scanner',message='To close the QRcode scanner, hold \'q\'')
            scanner_funcs.openQRScanner(pitScoutingPath)
        else: tk.messagebox.showerror(title='Missing Input',message='Please select the type of scouting input')
        #scanner_funcs.openQRScanner('py/app/data/match_scouting_data.txt')
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































