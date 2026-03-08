import customtkinter as ctk
from tkinter import Canvas

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

from tkinter import Canvas

class GradientProgressBar(ctk.CTkFrame):
    def __init__(self, parent, height=8, corner_radius=4, **kwargs):
        super().__init__(parent, height=height, fg_color="#0d1117", corner_radius=corner_radius, **kwargs)
        self.progress = 0.0
        self.canvas = Canvas(self, bg="#0d1117", highlightthickness=0, height=height)
        self.canvas.pack(fill="both", expand=True)
        self.bind("<Configure>", lambda e: self.draw())

    def set(self, value):
        self.progress = max(0.0, min(1.0, value))
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        fill_width = int(w * self.progress)
        if fill_width <= 0:
            return
        # draw gradient slice by slice
        steps = fill_width
        for i in range(steps):
            t = i / max(steps - 1, 1)
            r = int(220 * (1 - t) + 90 * t)
            g = 0
            b = int(20 * (1 - t) + 200 * t)
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(i, 0, i, h, fill=color)

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Phantom Trace")
        self.geometry("800x600")
        self.configure(fg_color="#0f111a")
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        #++++++++++ Left Column Container ++++++++++
        self.left_container = ctk.CTkFrame(self, fg_color="transparent")
        self.left_container.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")
        self.left_container.grid_columnconfigure(0, weight=1)
        self.left_container.grid_rowconfigure(1, weight=1)

        #++++++++++ Scan Control Panel ++++++++++
        self.control_panel = ctk.CTkFrame(self.left_container, fg_color="#161b22", border_width=1, border_color="#30363d")
        self.control_panel.configure(height=200)
        self.control_panel.grid_propagate(False)
        self.control_panel.pack_propagate(False)
        self.control_panel.grid(row=0, column=0, pady=(40, 10), sticky="ew")
        self.control_panel.grid_columnconfigure(0, weight=0)
        self.control_panel.grid_columnconfigure(1, weight=0)
        self.control_panel.grid_columnconfigure(2, weight=0)

        #--------- Quick Scan Button ----------
        self.quick_scan_btn = ctk.CTkButton(
            self.control_panel,
            text="▶ QUICK SCAN",
            width=120,
            height=35,
            fg_color="#202127",
            hover_color="#0d8b51",
            text_color="#169c55",
            corner_radius=4,
            border_width=1,
            border_color="#169c55"
        )
        self.quick_scan_btn.grid(row=0, column=0, padx=(20, 5), pady=40)

        # --------- Quick Scan Button ----------
        self.deep_scan_btn = ctk.CTkButton(
            self.control_panel,
            text="◯ DEEP SCAN",
            width=120,
            height=35,
            fg_color="#202127",
            text_color="#466c9c",
            corner_radius=4,
            border_width=1,
            border_color="#466c9c"
        )
        self.deep_scan_btn.grid(row=0, column=1, padx=(5, 5), pady=40)

        # --------- Stop Scan Button ----------
        self.stop_scan_btn = ctk.CTkButton(
            self.control_panel,
            text="⬛ STOP",
            width=120,
            height=35,
            fg_color="#202127",
            text_color="#4d4e53",
            hover_color="#f04449",
            corner_radius=4,
            border_width=1,
            border_color="#4d4e53"
        )
        self.stop_scan_btn.grid(row=0, column=2, padx=(5, 5), pady=40)

        #---------- Progress Bar ----------
        self.progress_bar = ctk.CTkProgressBar(
            self.control_panel,
            width=300,
            height=8,
            corner_radius=2,
            fg_color="#0d1117",
            progress_color="#169c55",
            border_width=0,
        )
        self.progress_bar = GradientProgressBar(self.control_panel, height=8)
        self.progress_bar.grid(row=1, column=0, columnspan=3, padx=20, pady=(0, 15), sticky="ew")
        self.progress_bar.set(0)

        #---------- Severity Counters ----------
        self.counter_frame = ctk.CTkFrame(self.control_panel, fg_color="transparent")
        self.counter_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=(0, 10), sticky="ew")
        self.counter_frame.grid_columnconfigure((0, 1, 2), weight=1)

        #---------- HIGH Severity ----------
        self.high_frame = ctk.CTkFrame(self.counter_frame, fg_color="#1a0a0a", border_width=1, border_color="#ff3355", corner_radius=4)
        self.high_frame.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.high_count = ctk.CTkLabel(self.high_frame, text="0", font=("Courier", 22, "bold"), text_color="#ff3355")
        self.high_count.pack(pady=(8, 0))
        self.high_label = ctk.CTkLabel(self.high_frame, text="HIGH", font=("Courier", 10), text_color="#ff3355")
        self.high_label.pack(pady=(0, 8))

        #---------- MEDIUM Severity ----------
        self.high_frame = ctk.CTkFrame(self.counter_frame, fg_color="#1a0a0a", border_width=1, border_color="#ff8c00", corner_radius=4)
        self.high_frame.grid(row=0, column=1, padx=10, sticky="ew")
        self.high_count = ctk.CTkLabel(self.high_frame, text="0", font=("Courier", 22, "bold"), text_color="#ff8c00")
        self.high_count.pack(pady=(8, 0))
        self.high_label = ctk.CTkLabel(self.high_frame, text="MEDIUM", font=("Courier", 10), text_color="#ff8c00")
        self.high_label.pack(pady=(0, 8))

        #---------- LOW Severity ----------

        self.high_frame = ctk.CTkFrame(self.counter_frame, fg_color="#1a0a0a", border_width=1, border_color="#169c55", corner_radius=4)
        self.high_frame.grid(row=0, column=2, padx=10, pady=0, sticky="ew")
        self.control_panel.configure(height=250)
        self.high_count = ctk.CTkLabel(self.high_frame, text="0", font=("Courier", 22, "bold"), text_color="#169c55")
        self.high_count.pack(pady=(8, 0))
        self.high_label = ctk.CTkLabel(self.high_frame, text="LOW", font=("Courier", 10), text_color="#169c55")
        self.high_label.pack(pady=(0, 8))




if __name__ == "__main__":
    app = App()
    app.mainloop()