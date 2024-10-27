import tkinter as tk
from pylsl import StreamInlet, resolve_stream, resolve_streams
import pylsl

class Stream_search_window(tk.Frame):

    stream_name_search = None
    stream_type_search = None 
    search_button = None

    stream_list = None

    def __init__(self,parent):
        super().__init__(parent)

        tk.Label(self, text = 'Stream search').grid(row = 0, column = 0, sticky = 'w', padx = 5, pady = 5)

        tk.Label(self, text = 'Stream name:').grid(row = 0, column = 1, sticky = 'w', padx = (5,2), pady = 5)
        self.stream_name_search = tk.Entry(self)
        self.stream_name_search.grid(row = 0, column = 2, sticky = 'w', padx = (1,5), pady = 5)

        tk.Label(self, text = 'Stream type').grid(row = 0, column = 3, sticky = 'w', padx = (5,2), pady = 5)
        self.stream_type_search = tk.Entry(self)
        self.stream_type_search.grid(row = 0, column = 4, sticky = 'w', padx = (1,5), pady = 5)

        tk.Button(self, text = 'Search', command = self.search_for_streams).grid(row = 0, column = 5 ,padx = 5, pady = 5)



    def search_for_streams(self):

        name_search = self.stream_name_search.get().strip()
        type_search = self.stream_type_search.get().strip()

        if name_search == '' and type_search == '':

            streams = resolve_streams(wait_time=0.5)
            self.stream_list.display_streams(streams)




    def set_stream_list(self, stream_list):
        self.stream_list = stream_list


