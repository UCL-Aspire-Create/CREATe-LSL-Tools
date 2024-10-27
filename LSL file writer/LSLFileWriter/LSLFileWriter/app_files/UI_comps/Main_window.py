import tkinter as tk
from tkinter import ttk
from . import Stream_list, Stream_search, Recording_settings, Recording_controls
class main_window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("1200x700")

        stream_frame = tk.Frame(self)
        stream_frame.grid(row = 0, column = 0, sticky = 'nsew')
        
        stream_search_frame = Stream_search.Stream_search_window(stream_frame)
        stream_search_frame.grid(row = 0, column = 0)

        stream_list_frame = Stream_list.stream_list(stream_frame)
        stream_list_frame.grid(row = 1, column = 0)
        stream_search_frame.set_stream_list(stream_list_frame)

        ttk.Separator(self,orient='vertical').grid(row = 0, column = 1, sticky = 'ns', padx = 5, pady = 5)

        recording_frame = tk.Frame(self)
        recording_frame.grid(row = 0, column = 2, sticky = 'nsew')
        record_settings_frame = Recording_settings.Recording_settings(recording_frame)
        record_settings_frame.grid(row = 0, column = 0, sticky = 'nsew', padx = 5, pady = 5)

        record_controls = Recording_controls.recording_controls(recording_frame)
        record_controls.grid(row = 1, column = 0, sticky = 'se', padx = 5, pady = 5)

        
    