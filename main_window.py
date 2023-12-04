from styleOopVersion import *


class Main_Window():
    def __init__(self, window):
        self.window = window
        window.resizable(True, True)
        self.left_frame = tk.Frame(window, width= main_window_width/4 , height=main_window_height, bg=left_frame_background_color)# Phần mành hình hiển thị các file.
        self.left_frame.pack(side="left",fill='both',expand= True)

        self.right_frame = tk.Frame(window, width= main_window_width - main_window_width/4 , height=main_window_height, bg=right_frame_background_color)
        self.right_frame.pack(side="right",fill='both', expand= True)

        self.top_right_frame = tk.Frame(self.right_frame, width= main_window_width - main_window_width/3 , height=main_window_height//2 , bg=top_right_frame_background_color)
        self.top_right_frame.pack_propagate(True)
        self.top_right_frame.pack(side = 'top', fill='both', expand=True)  # Fill và expand để frame mở rộng theo kích thước của parent

        self.top_right_text = tk.Text(self.top_right_frame, wrap=tk.WORD, state=tk.DISABLED, bg= text_color)
        self.top_right_text.pack(expand=True, fill='both')

        self.bottom_right_frame = tk.Frame(self.right_frame, width=main_window_width - main_window_width/3, height=main_window_height//2, bg=bottom_right_frame_background_color)
        self.bottom_right_frame.pack_propagate(True)
        self.bottom_right_frame.pack(side= 'bottom', fill='both', expand=True)

        self.entry = tk.Entry(self.bottom_right_frame, width=70, font=('Arial', 18))
        self.entry.pack(side='bottom', pady=10, padx=10)

        self.submit_button = tk.Button(self.bottom_right_frame, text="Submit", command= self.get_entry)
        self.submit_button.pack(side='right')

        self.loading_label = tk.Label(self.top_right_frame, text="Loading...", fg = fg_loading_label, bg = bg_loading_label)  # Đổi màu và font chữ
        self.loading_label.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.progress_bar = Progressbar(self.top_right_frame, mode='indeterminate', length = 83)
        self.progress_bar.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def display_message(self,message, sender): # chức năng hiện chữ lên màn hình.
        global file_path
        self.top_right_text.config(state=tk.NORMAL, fg="#FFFFFF")  # Cho phép cập nhật nội dung

        with open(str(file_path), 'a', encoding='utf-8') as file: #
            if sender == "user":
                self.top_right_text.insert(tk.END, f"You: {message}\n\n", "user_message")
                file.write(f"You: {message}\n\n")
            elif sender == "bot":
                self.top_right_text.insert(tk.END, f"Bot: {message}\n\n", "bot_message")
                file.write(f"Bot: {message}\n\n")

        self.top_right_text.config(state=tk.DISABLED)  # Khóa trạng thái
        self.top_right_text.see(tk.END)

    def process_message(self,user_message):
        global loading_flag
        self.window.after(0, lambda: self.loading_label.config(background='green'))  # Thay đổi màu của label khi bắt đầu loading
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            stream=True,
        )
        ans = ""
        for text in response:
            ans += text
        loading_flag = False
        self.window.after(0, lambda: self.display_message(ans, "bot"))  # Hiển thị tin nhắn của bot
        self.window.after(0, lambda: self.progress_bar.stop())
        self.window.after(0, lambda: self.loading_label.config(background="white"))

    def get_entry(self,event=None):
        global loading_flag,created
        if created:
            request = self.entry.get()
            self.display_message(request, "user")
            self.entry.delete(0, tk.END)

            loading_flag = True
            self.progress_bar.start()

            thread = threading.Thread(target= self.process_message, args=(request,))
            thread.start()
        else:
            messagebox.showerror("Warning", "You must create the file.txt first")