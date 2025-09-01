# main.py
# --- GUI Implementation ---
import tkinter as tk
from tkinter import ttk
from classes.GUIs import ManualTestingGUI, AutomatedTestsGUI
from classes.measurements_AP import Noise



def main():
    def create_window(title_text, parent=None, bg="#e9ecef"):
        # Only create one root window (tk.Tk), all others are Toplevel
        if not hasattr(create_window, "root_created"):
            win = tk.Tk()
            create_window.root_created = True
        else:
            win = tk.Toplevel(parent)
        win.title(title_text)
        win.configure(bg=bg)
        # Prevent window from being resized or maximized
        win.resizable(False, False)
        win.minsize(600, 400)
        win.maxsize(600, 400)
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

    setup_styles()
    root, frame = create_window("Neuranics ASIC Lab Automation")

    def open_manual():
        manual_win = tk.Toplevel(root)
        ManualTestingGUI(manual_win)

    def open_automated():
        auto_win = tk.Toplevel(root)
        AutomatedTestsGUI(auto_win)

    # Main menu buttons
    btn_manual = ttk.Button(frame, text="Manual Testing", style='Rounded.TButton', command=open_manual)
    btn_manual.pack(pady=10, fill='x')
    btn_auto = ttk.Button(frame, text="Automated Tests", style='Accent.Rounded.TButton', command=open_automated)
    btn_auto.pack(pady=10, fill='x')

    def close_programme():
        # Destroys all Tk windows and exits
        for window in root.winfo_toplevel().winfo_children():
            try:
                window.destroy()
            except:
                pass
        root.destroy()

    btn_close = ttk.Button(frame, text="Close Application", style='Rounded.TButton', command=close_programme)
    btn_close.pack(pady=20, fill='x')

    root.mainloop()


if __name__ == "__main__":
    main()