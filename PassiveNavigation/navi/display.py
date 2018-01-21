import tkinter as tk

class Display():
    def __init__(self):
        self.before_text = ''

        self.root = tk.Tk()
        self.root.title('PassiveNavigation')
        self.root.geometry('480x320+0+0')

        self.text_widget = tk.Text(self.root)
        self.text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        tmp_text = open('./temp.txt', 'r').read()
        if self.before_text != tmp_text:
            self.text_widget.insert('end', tmp_text);
            self.before_text = tmp_text
        self.root.after(1000, self.update_clock)

if __name__ == '__main__':
    display = Display()
