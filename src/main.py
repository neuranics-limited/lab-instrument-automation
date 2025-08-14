# main.py
# --- GUI Implementation ---
import tkinter as tk
from tkinter import ttk
from classes.GUIs import PowerSupplyGUI, SignalGeneratorGUI


def main():
    root = tk.Tk()
    root.title("Lab Instrument Automation")
    root.configure(bg="#e9ecef")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background="#ffffff")
    style.configure('TLabel', background="#ffffff", font=("Segoe UI", 12))
    style.configure('Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#e3f2fd", foreground="#222")
    style.map('Rounded.TButton',
        background=[('active', '#bbdefb'), ('!active', '#e3f2fd')],
        relief=[('pressed', 'groove'), ('!pressed', 'flat')],
        bordercolor=[('focus', '#90caf9'), ('!focus', '#e3f2fd')]
    )
    style.configure('Accent.Rounded.TButton', font=("Segoe UI", 12, "bold"), padding=[14, 8], borderwidth=2, relief="flat", background="#4CAF50", foreground="white")
    style.map('Accent.Rounded.TButton',
        background=[('active', '#388E3C'), ('!active', '#4CAF50')],
        relief=[('pressed', 'groove'), ('!pressed', 'flat')],
        bordercolor=[('focus', '#388E3C'), ('!focus', '#4CAF50')]
    )

    frame = ttk.Frame(root, padding=30, style='TFrame')
    frame.pack(padx=40, pady=40)

    title = ttk.Label(frame, text="Lab Instrument Automation", font=("Segoe UI", 20, "bold"), background="#ffffff")
    title.grid(row=0, column=0, columnspan=2, pady=(0, 30))

    def open_ps():
        ps_win = tk.Toplevel(root)
        PowerSupplyGUI(ps_win)

    def open_sg():
        sg_win = tk.Toplevel(root)
        SignalGeneratorGUI(sg_win)

    ps_button = ttk.Button(frame, text="Power Supply Control", command=open_ps, style='Accent.Rounded.TButton', width=22)
    ps_button.grid(row=1, column=0, pady=18, padx=18)
    sg_button = ttk.Button(frame, text="Signal Generator Control", command=open_sg, style='Rounded.TButton', width=22)
    sg_button.grid(row=1, column=1, pady=18, padx=18)

    root.mainloop()


if __name__ == "__main__":
    main()