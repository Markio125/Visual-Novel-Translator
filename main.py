from tkinter import *
from screenshot import *


class ScreenshotApp():
    def __init__(self, master):
        self.highlight_window = None
        self.print_button = None
        self.text_area = None
        self.translation_window = None
        self.rect = None
        self.snip_surface = None
        self.master = master
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None

        self.master.geometry('300x50+0+0')
        self.master.title('VNdow Selector')
        root.resizable(False, False)

        self.menu_frame = Frame(master)
        self.menu_frame.pack(fill=BOTH, expand=YES, padx=1, pady=2)

        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.rowconfigure(0, weight=1)
        self.menu_frame.columnconfigure(1, weight=1)
        self.menu_frame.columnconfigure(2, weight=1)

        self.snipButton = Button(self.menu_frame, width=5, height=3, command=self.create_screen_canvas, background="green", text="START", fg="white")
        self.snipButton.grid(row=0, column=0)

        self.snipButton2 = Button(self.menu_frame, width=5, height=3, command=self.close_program, background="red", text="STOP", fg="white")
        self.snipButton2.grid(row=0, column=1)

        self.snipButton3 = Button(self.menu_frame, width=8, height=3, command=self.translator_window, background="grey", text="Translator", fg="white")
        self.snipButton3.grid(row=0, column=2)

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=BOTH, expand=YES)

    def create_screen_canvas(self):
        if self.snip_surface:
            self.snip_surface.destroy()
        self.master_screen.deiconify()
        root.withdraw()

        self.snip_surface = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.snip_surface.pack(fill=BOTH, expand=YES)

        self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
        self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
        self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        try:
            self.snip_surface.pack()
            global width, height, x, y
            width = int(abs(self.current_x - self.start_x))
            height = int(abs(self.current_y - self.start_y))
            x = int(min(self.start_x, self.current_x))
            y = int(min(self.start_y, self.current_y))
            self.display_rectangle_position()
            # self.snip_surface.destroy()
            self.master_screen.withdraw()
            self.master.deiconify()
        except Exception as e:
            print(f"An error occurred: {e}")

    def translator_window(self):
        self.translation_window = Toplevel(self.master)
        self.translation_window.title("Translation VNdow")
        self.translation_window.geometry("400x350")
        self.translation_window.configure(bg='black')
        self.text_area = Text(self.translation_window, wrap='word', height=15, bg='black', fg='white')
        self.text_area.pack(pady=10)
        self.print_button = Button(self.translation_window, text="Translate", command=self.translate, bg='grey', fg='black')
        self.print_button.pack(pady=5)

    def translate(self):
        data = loop_code(x, y, width, height)
        self.print_data(data)

    def print_data(self, data):
        self.text_area.insert(END, data+'\n')
        self.text_area.see(END)
    
    def exit_screenshot_mode(self):
        self.snip_surface.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def on_button_press(self, event):
        self.start_x = self.snip_surface.canvasx(event.x)
        self.start_y = self.snip_surface.canvasy(event.y)
        self.rect = self.snip_surface.create_rectangle(0, 0, 1, 1, outline='red', width=3, fill="maroon3")

    def on_snip_drag(self, event):
        self.current_x, self.current_y = (event.x, event.y)
        self.snip_surface.coords(self.rect, self.start_x, self.start_y, self.current_x, self.current_y)

    def display_rectangle_position(self):
        print(self.start_x)
        print(self.start_y)
        print('_________________')
        print(x)
        print(y)
        print('_________________')
        print(self.current_x)
        print(self.current_y)
        print('_________________')
        print(width)
        print(height)

    def close_program(self):
        root.destroy()

if __name__ == '__main__':
    root = Tk()
    app = ScreenshotApp(root)
    root.mainloop()