import tkinter
from tkinter import ttk

class Toplevel(tkinter.Tk):
    def __init__(self):
        super().__init__()
        height = 400
        width = 400
        '''Hiển thị chính giữa màn hình'''
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        center_x = screen_w//2 - width//2
        center_y = screen_h//2 - height//2

        self.geometry(f'{width}x{height}+{center_x}+{center_y}')

        self.configure(background='red')
        self.attributes('-alpha',0.5)
        self.iconbitmap(r'C:\Users\My Computer\Downloads\instagram_logo_brand_social_media_application_icon_197362.ico')


if __name__ == '__main__':
    app = Toplevel()
    app.mainloop()