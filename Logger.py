import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os

class LoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Outage and Work Logger')
        
        self.log_type = tk.StringVar()
        self.outage_severity = tk.StringVar()
        
        self.type_options = ['Outage', 'Work']
        self.severity_options = ['P1', 'P2', 'P3', 'P4']

        self.type_select = ttk.Combobox(self.root, textvariable=self.log_type)
        self.type_select['values'] = self.type_options
        self.type_select.bind('<<ComboboxSelected>>', self.type_selected)
        self.type_select.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.severity_select = ttk.Combobox(self.root, textvariable=self.outage_severity)
        self.severity_select['values'] = self.severity_options
        self.severity_select.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.text_box = tk.Text(self.root, width=50, height=10)
        self.text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.timestamp_button = tk.Button(self.root, text='Insert Timestamp', command=self.insert_timestamp)
        self.timestamp_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        
        self.submit_button = tk.Button(self.root, text='Submit', command=self.submit_log)
        self.submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Make widgets resize with the window
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(1, weight=1)

    def type_selected(self, event):
        if self.log_type.get() == 'Work':
            self.severity_select.configure(state='disabled')
        else:
            self.severity_select.configure(state='enabled')

    def insert_timestamp(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.text_box.insert(tk.INSERT, f"{timestamp}\n")

    def submit_log(self, base_path=r'Enter your file location'):  # Specify your directory
        log_type = self.log_type.get()
        log_content = self.text_box.get("1.0", 'end-1c')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if log_type == 'Work':
            file_name = 'How I keep busy.txt'
            full_path = os.path.join(base_path, file_name)
            with open(full_path, 'a') as file:
                file.write(f"{timestamp}\n{log_content}\n\n")
        else:
            outage_severity = self.outage_severity.get()
            file_name = f"{outage_severity}_{timestamp.split()[0]}.txt"
            full_path = os.path.join(base_path, file_name)
            with open(full_path, 'a') as file:
                file.write(f"Severity: {outage_severity}\nStart Time: {timestamp}\n\n{log_content}\n\n")

        self.text_box.delete('1.0', tk.END)

root = tk.Tk()
app = LoggerApp(root)
root.mainloop()
