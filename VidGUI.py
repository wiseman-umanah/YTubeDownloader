import tkinter as tk
from tkinter import ttk
#from main import VidDownloader

root = tk.Tk()
root.title("Youtube Downloader")
root.geometry(newGeometry="600x120")
root.resizable(False, False)

def get_input(event):
	user_input = entry.get()
	print(user_input)

write = ttk.Label(root, text="Paste your youtube Link to Start Downloading", font=("Helvetica", 15), foreground="#066691", padding=10)
write.pack()
entry = ttk.Entry(root, width=80)
entry.pack()
entry.bind("<Return>", get_input)
download_button = tk.Button(root, text="Download", command=lambda: get_input("<Return>"), foreground="white", background="red")
download_button.pack(side=tk.RIGHT, padx=(0, 50), pady=(5, 0))


root.mainloop()