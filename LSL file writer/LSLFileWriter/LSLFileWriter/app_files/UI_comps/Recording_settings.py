import tkinter as tk
from tkinter import ttk, filedialog


class Recording_settings(tk.Frame):

    file_type_select = None
    
    def __init__(self, parent):
        super().__init__(parent)

        output_settings = output_path_frame(self)
        output_settings.grid(row = 0, column = 0, sticky = 'nsew', padx = 5, pady = 5)

        file_type_frame = tk.Frame(self)
        file_type_frame.grid(row = 1, column = 0, sticky = 'nsew', padx = 5, pady = 5)

        tk.Label(file_type_frame, text = 'file_type:').grid(row = 1, column = 0, padx = (5,1), pady = 5)
        file_values = ['.csv']
        file_type_select = ttk.Combobox(file_type_frame, values = file_values)
        file_type_select.set(file_values[0])

        file_type_select.grid(row = 1, column = 1, sticky = 'nsew',padx = (1,5), pady = 5)


        

    




class output_path_frame(tk.Frame):

    path = None
    path_entry = None

    def __init__(self, parent): 
        super().__init__(parent)
        tk.Button(self, text = 'change path', command = self.change_path).grid(row = 0, column = 0, sticky = 'nsew', padx = 2, pady = 5)
        self.path_entry = tk.Entry(self, width= 50)
        self.path_entry.grid(row = 0, column = 1, sticky = 'ew', padx = 1, pady = 5)


    def change_path(self):
        direct = tk.filedialog.askdirectory(mustexist = True)
        if direct != '':
            self.path_entry.delete(0, tk.END)
            self.path = direct
            self.path_entry.insert(0,direct)

    def get_path(self):
        return self.path
