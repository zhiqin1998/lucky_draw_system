import time
import tkinter as tk
import tkinter.ttk as ttk
from configparser import ConfigParser
from random import randint
from threading import Thread


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        root = tk.Tk.__init__(self, *args, **kwargs)
        self.exitFlag = False
        self.outerFrame = tk.Frame(root)
        self.viewframe = tk.Frame(self.outerFrame)
        self.resizable(False, False)
        self.winfo_toplevel().title('Lucky Draw')
        self.load_home_page()
        self.counter = 0
        self.exclude = []
        self.configparser = ConfigParser()
        self.configparser.read('config.ini')
        self.start_num = int(self.configparser['NUM']['START'])
        self.end_num = int(self.configparser['NUM']['END'])
        self.timer = float(self.configparser['DRAW']['DRAW_TIME'])
        self.rand_count = int(self.configparser['DRAW']['RANDOM_COUNT'])

    def load_home_page(self):
        oframe = tk.ttk.Frame(self.outerFrame)
        oframe.pack(fill=tk.X, expand=True)
        titleLabel = tk.Label(oframe, text='Lucky Draw', font=("Helvetica", 25))
        titleLabel.pack(fill=tk.X, pady=5)
        frame = tk.ttk.Frame(oframe, relief=tk.GROOVE)
        frame.pack(pady=5, padx = 5)
        nameFrame = tk.ttk.Frame(frame)
        nameFrame.pack(fill=tk.X, pady=5, padx=5)
        nameLabel = tk.ttk.Label(nameFrame, text='{0:15}\t:'.format('Numbers to Exclude (use comma to seperate it): '))
        nameLabel.pack(side=tk.LEFT, padx=5)
        nameEntry = tk.ttk.Entry(nameFrame)
        nameEntry.pack(side=tk.LEFT)
        nameEntry.focus()

        def proceed():
            if nameEntry.get().strip() is not '':
                self.exclude = nameEntry.get().split(',')
                self.exclude = list(filter(None, self.exclude))
                self.exclude = list(map(int, self.exclude))

            self.new_pop_up()

        submit = tk.ttk.Button(frame, text='Draw Now', width=10,
                               command=lambda: proceed())
        submit.pack(pady=5, side=tk.RIGHT, padx=10)
        self.bind('<Return>', lambda _: proceed())
        self.outerFrame.pack(fill=tk.Y, expand=True)

    def new_pop_up(self):
        def proceed():
            submit.config(state='disabled')
            for i in range(self.rand_count):
                r_num = randint(self.start_num, self.end_num)
                while r_num in self.exclude:
                    r_num = randint(self.start_num, self.end_num)
                num.set('{:04d}'.format(r_num))
                time.sleep(self.timer/self.rand_count)
            submit.config(state='normal')
        win = tk.Toplevel()
        win.grab_set()
        win.wm_title('Lucky Draw')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        win.overrideredirect(1)
        win.geometry("%dx%d+0+0" % (w, h))
        win.bind("<Escape>", lambda e: e.widget.quit())
        frame = tk.ttk.Frame(win, border=2, relief=tk.GROOVE)
        frame.pack(fill=tk.BOTH,expand=True, padx=5, pady=5)
        codeFrame = tk.ttk.Frame(frame)
        num = tk.StringVar()
        num.set('')
        codeLabel = tk.ttk.Label(codeFrame, textvariable=num, font=("Helvetica", 300), anchor = 'center')
        codeLabel.pack(expand = True, side = tk.TOP, fill=tk.BOTH)
        codeFrame.pack(expand=True, side = tk.TOP, fill= tk.BOTH)

        submit = tk.ttk.Button(frame, text='Draw', width=10,
                               command=lambda: Thread(target=proceed).start())
        submit.pack(side=tk.BOTTOM, pady=5)
        win.bind('<Return>', lambda _: Thread(target=proceed).start())

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
