import tkinter as tk
class recording_controls(tk.Frame):

    recording_button = None

    def __init__(self, parent):
        super().__init__(parent)

        self.recording_button = tk.Button(self, text = 'Record')
        self.recording_button.grid(row = 0, column = self.grid_size()[0], sticky = 'se', padx = 5, pady = 5)

    def start_recording(self):
        pass

    

     