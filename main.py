import tkinter as tk
from tkinter import ttk
from datetime import datetime
import math

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CooCoo")
        self.root.geometry("675x325")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c2f33")

        self.clock = tk.Frame(self.root, bg="#625E5E")
        self.clock.place(x=20, y=25, width=230, height=275)

        self.time = datetime.now()

        self.analog_clock = tk.Canvas(self.clock, bg="#625E5E", highlightthickness=0)
        self.analog_clock.create_oval(0, 0, 145, 145, fill="#ffffff", outline="#ffffff")
        self.hour_hand = self.analog_clock.create_line(72, 72, 72, 32, fill="#000000", width=3)
        self.minute_hand = self.analog_clock.create_line(72, 72, 72, 22, fill="#000000", width=3)
        self.second_hand = self.analog_clock.create_line(72, 72, 72, 12, fill="#000000", width=3)
        self.analog_clock.place(x=40, y=25, width=145, height=145)

        self.time_label = tk.Label(self.clock, text=self.time.strftime("%H:%M:%S"), font=("Arial", 32), bg="#625E5E", fg="#ffffff")
        self.time_label.place(x=0, y=175, width=230, height=60)

        self.date_label = tk.Label(self.clock, text=self.time.strftime("%a %d %b %Y"), font=("Arial", 18), bg="#625E5E", fg="#ffffff")
        self.date_label.place(x=0, y=235, width=230, height=40)

        self.alarms_frame = tk.Frame(self.root, bg="#2c2f33")
        self.alarms_frame.place(x=265, y=25, width=150, height=275)

        tk.Label(self.alarms_frame, text="Alarms", font=("Arial", 18), bg="#2c2f33", fg="#ffffff").place(x=0, y=0, width=150, height=40)
        self.alarms_list = tk.Listbox(self.alarms_frame, font=("Arial", 14), bg="#2c2f33", fg="#ffffff", highlightthickness=0, selectbackground="#ffffff", selectforeground="#000000")
        self.alarms_list.place(x=0, y=40, width=150, height=235)
        
        alarms_scrollbar = tk.Scrollbar(self.alarms_frame, orient="vertical", command=self.alarms_list.yview)
        alarms_scrollbar.place(x=130, y=40, width=20, height=235)
        self.alarms_list.config(yscrollcommand=alarms_scrollbar.set)

        self.update()
    
    def draw_analog_clock(self):
        seconds = self.time.second
        length = 60
        s_x, s_y = length * math.sin(math.radians(seconds*6)), -1 * length * math.cos(math.radians(seconds*6))
        self.analog_clock.coords(self.second_hand, 72, 72, 72+s_x, 72+s_y)

        minutes = self.time.minute
        length = 50
        m_x, m_y = length * math.sin(math.radians(minutes*6)), -1 * length * math.cos(math.radians(minutes*6))
        self.analog_clock.coords(self.minute_hand, 72, 72, 72+m_x, 72+m_y)

        hours = self.time.hour
        length = 40
        h_x, h_y = length * math.sin(math.radians(hours*30)), -1 * length * math.cos(math.radians(hours*30))
        self.analog_clock.coords(self.hour_hand, 72, 72, 72+h_x, 72+h_y)
    
    def update(self):
        self.time = datetime.now()
        self.draw_analog_clock()
        self.time_label.config(text=self.time.strftime("%H:%M:%S"))
        self.date_label.config(text=self.time.strftime("%a %d %b %Y"))
        self.root.after(100, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()