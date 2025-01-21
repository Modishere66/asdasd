import tkinter as tk
from tkinter import ttk


class ScannerUI:
    def __init__(self, start_scan_callback, stop_scan_callback):
        self.root = tk.Tk()
        self.root.title("3D Scanner")

        self.start_scan_callback = start_scan_callback
        self.stop_scan_callback = stop_scan_callback

        self.progress = ttk.Progressbar(self.root, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=20)

        self.status_label = tk.Label(self.root, text="Status: Ready")
        self.status_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Scan", command=self.start_scan)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Scan", command=self.stop_scan, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def start_scan(self):
        self.start_scan_callback()
        self.status_label.config(text="Status: Scanning...")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_scan(self):
        self.stop_scan_callback()
        self.status_label.config(text="Status: Ready")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()