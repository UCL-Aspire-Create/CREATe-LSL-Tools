import tkinter as tk
from pylsl import StreamInfo
class stream_list(tk.Frame):

    list_frame = None
    stream_list = None

    def __init__(self, parent):
        super().__init__(parent)

        self.stream_list = []
        
        self.list_frame = tk.Frame(self, width=600, height=300, bg = 'white', highlightthickness=1, highlightbackground='black')
        self.list_frame.grid(row = 1, column = 0, sticky = 'nsew', padx = 5, pady = 5)
        self.list_frame.grid_propagate(0)
    def display_streams(self, stream_infos:[StreamInfo]):

        for s in self.stream_list:
            s.destroy()
            del s
        self.stream_list.clear()

        
        for str_inf in stream_infos:
            self.stream_list.append(stream_box(self.list_frame,str_inf))
            self.stream_list[-1].grid(row = len(self.stream_list)-1, column = 0, sticky = 'nsew', padx = 2, pady = 2)

        self.list_frame.config(width=700, height=300)


class stream_box(tk.Frame):

    selected = None
    
    def __init__(self, parent, stream_info):
        super().__init__(parent)
        self.config(bg = 'white')

        self.selected = tk.IntVar()

        check_box = tk.Checkbutton(self, text = '', variable=self.selected, onvalue=1, offvalue=0, bg = 'white')
        check_box.grid(row = 0, column = 0, sticky = 'we', padx = 5, pady = 2)

        tk.Label(self, text = stream_info.name(), bg = 'white').grid(row = 0, column = 1, sticky = 'we', padx = 5, pady = 2)
        tk.Label(self, text = stream_info.type(), bg = 'white').grid(row = 0, column = 2, sticky = 'we', padx = 5, pady = 2)
        tk.Label(self, text = stream_info.channel_count(), bg = 'white').grid(row = 0, column = 3, sticky = 'we', padx = 5, pady = 2)

        



