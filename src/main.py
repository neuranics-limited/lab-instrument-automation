# main.py
# --- GUI Implementation ---
import tkinter as tk
from tkinter import ttk
from classes.GUIs import PowerSupplyGUI, SignalGeneratorGUI, OscilloscopeGUI


def create_window(title_text, parent=None, bg="#e9ecef"):
    # Only create one root window (tk.Tk), all others are Toplevel
    if not hasattr(create_window, "root_created"):
        win = tk.Tk()
        create_window.root_created = True
    else:
        win = tk.Toplevel(parent)
    win.title(title_text)
    win.configure(bg=bg)
    frame = ttk.Frame(win, padding=30, style='TFrame')
    frame.pack(padx=40, pady=40)
    title = ttk.Label(frame, text=title_text, font=("Segoe UI", 20, "bold"), background="#ffffff")
    title.pack(pady=(0, 30))
    return win, frame


def setup_styles():
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


def main():
    setup_styles()
    root, frame = create_window("Lab Instrument Automation")

    def open_ps():
        ps_win = tk.Toplevel(root)
        PowerSupplyGUI(ps_win)

    def open_sg():
        sg_win = tk.Toplevel(root)
        SignalGeneratorGUI(sg_win)

    ps_button = ttk.Button(frame, text="Power Supply Control", command=open_ps, style='Accent.Rounded.TButton', width=22)
    ps_button.pack(pady=18, padx=18)
    sg_button = ttk.Button(frame, text="Signal Generator Control", command=open_sg, style='Rounded.TButton', width=22)
    sg_button.pack(pady=18, padx=18)

    def open_measurements():
        meas_win = tk.Toplevel(root)
        meas_win.title("Measurements")
        meas_win.configure(bg="#e9ecef")
        frame = ttk.Frame(meas_win, padding=30, style='TFrame')
        frame.pack(padx=40, pady=40)
        title = ttk.Label(frame, text="Measurements", font=("Segoe UI", 20, "bold"), background="#ffffff")
        title.pack(pady=(0, 30))
        meas_win.protocol("WM_DELETE_WINDOW", lambda: meas_win.destroy())

    def open_manual():
        manual_win = tk.Toplevel(root)
        manual_win.title("Manual Control")
        manual_win.configure(bg="#e9ecef")
        frame = ttk.Frame(manual_win, padding=30, style='TFrame')
        frame.pack(padx=40, pady=40)
        title = ttk.Label(frame, text="Manual Control", font=("Segoe UI", 20, "bold"), background="#ffffff")
        title.pack(pady=(0, 30))
        buttons = [
            ("Power Supply", lambda: open_ps_in_manual(manual_win), 'Accent.Rounded.TButton'),
            ("Signal Generator", lambda: open_sg_in_manual(manual_win), 'Rounded.TButton'),
            ("Oscilloscope", lambda: open_osc_in_manual(manual_win), 'Accent.Rounded.TButton'),
        ]
        for text, command, style in buttons:
            button = ttk.Button(frame, text=text, command=command, style=style, width=22)
            button.pack(pady=12)
        manual_win.protocol("WM_DELETE_WINDOW", lambda: manual_win.destroy())

    def open_osc_in_manual(parent_win):
        parent_win.withdraw()
        osc_win = tk.Toplevel(parent_win)
        from classes.GUIs import OscilloscopeGUI
        OscilloscopeGUI(osc_win)
        osc_win.protocol("WM_DELETE_WINDOW", lambda: (osc_win.destroy(), parent_win.deiconify()))

    def open_ps_in_manual(parent_win):
        parent_win.withdraw()
        ps_win, _ = create_window("Power Supply Control", parent=parent_win)
        PowerSupplyGUI(ps_win)
        ps_win.protocol("WM_DELETE_WINDOW", lambda: (ps_win.destroy(), parent_win.deiconify()))

    def open_sg_in_manual(parent_win):
        parent_win.withdraw()
        sg_win, _ = create_window("Signal Generator Control", parent=parent_win)
        SignalGeneratorGUI(sg_win)
        sg_win.protocol("WM_DELETE_WINDOW", lambda: (sg_win.destroy(), parent_win.deiconify()))

    def open_osc_in_manual(parent_win):
        parent_win.withdraw()
        osc_win, _ = create_window("Oscilloscope Control", parent=parent_win)
        OscilloscopeGUI(osc_win)
        osc_win.protocol("WM_DELETE_WINDOW", lambda: (osc_win.destroy(), parent_win.deiconify()))

    # Redesign home page: only two buttons
    for widget in frame.winfo_children():
        widget.destroy()
    title = ttk.Label(frame, text="Lab Instrument Automation", font=("Segoe UI", 22, "bold"), background="#ffffff")
    title.pack(pady=(0, 30))
    meas_button = ttk.Button(frame, text="Measurements", command=open_measurements, style='Accent.Rounded.TButton', width=22)
    meas_button.pack(pady=18)
    manual_button = ttk.Button(frame, text="Manual", command=open_manual, style='Rounded.TButton', width=22)
    manual_button.pack(pady=18)

    root.mainloop()


if __name__ == "__main__":
    main()