from create_file_window import *
from main_window import *

root = tk.Tk()
create_file_window = Login_window(root)
center_window(root,550,140)
root.mainloop() 

mainwin = tk.Tk()
main_window = Main_Window(mainwin)
center_window(mainwin,main_window_width,main_window_height)
mainwin.mainloop()