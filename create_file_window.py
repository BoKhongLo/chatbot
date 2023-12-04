from main_window import *

class Login_window(Main_Window):
    def __init__(self,frame):
        self.login_frame = frame

        # Tạo và thiết lập các thành phần giao diện
        self.label_folder = tk.Label(self.login_frame, text='Folder Location')
        self.entry_folder = tk.Entry(self.login_frame, width=50)
        self.button_browse = tk.Button(self.login_frame, text='Browser', command= self.browse_folder)

        self.label_file = tk.Label(self.login_frame, text='Filename.txt')
        self.entry_file = tk.Entry(self.login_frame, width=50)

        self.button_create = tk.Button(self.login_frame, text='Save',padx= 10, command= self.create_file)
        self.button_clear = tk.Button(self.login_frame, text='Back',padx= 10, command= self.clear_fields)

        self.result_label = tk.Label(self.login_frame, text='', font=('Arial', 10, 'italic'))

        # Định vị các thành phần giao diện
        self.label_folder.grid(row=0, column=0, padx=(10, 5), pady=5, sticky='e')
        self.entry_folder.grid(row=0, column=1, padx=5, pady=5)
        self.button_browse.grid(row=0, column=2, padx=(5, 10), pady=5)

        self.label_file.grid(row=1, column=0, padx=(10, 5), pady=5, sticky='e')
        self.entry_file.grid(row=1, column=1, padx=5, pady=5)

        self.button_create.grid(row=2, column=0, columnspan=2, pady=(10, 5))
        self.button_clear.grid(row=2, column=1, columnspan=2, pady=(10, 5))

        self.result_label.grid(row=3, column=0, columnspan=3, pady=(0, 10))

        self.login_frame.protocol("WM_DELETE_WINDOW", self.on_root_close)

        self.login_frame.resizable(False,False)

    def create_file(self):
        global created, file_path

        folder_path = self.entry_folder.get()
        file_name = self.entry_file.get()

        if folder_path and file_name:
            file_path = os.path.join(folder_path, file_name)

            try:
                with open(str(file_path), 'w',encoding='utf-8') as file: #
                    pass  # Tạo một file trống
                self.result_label.config(text=f'File {file_name} đã được tạo thành công trong {folder_path}')
                created = True 
                self.login_frame.after(1000, self.login_frame.destroy) # tắt cửa sổ.
            except Exception as e:
                self.result_label.config(text=f'Lỗi: {str(e)}')
        else:
            self.result_label.config(text='Hãy điền đầy đủ đường dẫn và tên file.')

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.entry_folder.delete(0, tk.END)
        self.entry_folder.insert(0, folder_path)

    def clear_fields(self):
        self.entry_folder.delete(0, tk.END)
        self.entry_file.delete(0, tk.END)
        self.result_label.config(text='')

    def on_root_close(self):
        if not created:
            self.login_frame.destroy() #Đóng cửa sổ tạo file
            self.window.destroy()  # Đóng cửa sổ chat chính


