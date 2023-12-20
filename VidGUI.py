"""
This module handles all the GUI formats for end-user
"""
import tkinter as tk
from tkinter import ttk
from main import VidDownloader

#Initialization of GUI module and window formatting

root = tk.Tk()
iconPath = "app_icon.ico"
root.wm_iconbitmap(iconPath)
root.title("Youtube Downloader")
root.geometry(newGeometry="430x180")
root.resizable(False, False)
root.configure(bg="black")

#Handle user input, somewhat like a link to the backend of the program
#Handle responds and error messages

def get_input(event):
	"""
	This function gets user's input from the Input Box,
	Maintains all the options and properly send output
	
	Args:
		event (keyboard): This Parameter is associated with the Return key
	"""
	user_input = entry.get()
	good = "Download Successful!!!"
	bad = "Download Failed!!!"
	# Destroy the existing label if it exists
	if hasattr(get_input, 'write1') and get_input.write1.winfo_exists():
		get_input.write1.destroy()
	
	try:
		test = VidDownloader(user_input)

		# Create a new label widget
		get_input.write1 = ttk.Label(root, text=" ", font=("Helvetica", 10), background="black")
		get_input.write1.grid(row=2, column=0, padx=(5, 0), pady=(20, 10), sticky="w")
		test.download_audVid(quality_option.get(), download_option.get())
		get_input.write1.config(text=good, font=("Helvetica", 10), foreground="green",  background="black")
		get_input.write1.grid(row=2, column=0, padx=(5, 0), pady=(20, 10), sticky="w")
	except Exception as e:
		# Handle exceptions and display an error message
		get_input.write1 = ttk.Label(root, text=bad, foreground="red", background="black")
		get_input.write1.grid(row=2, column=0, padx=(5, 0), pady=(20, 10), sticky="w")


## Gets download option and sets default option
download_option = tk.StringVar()
download_option.set("Video")


## Gets download quality option and sets default option
quality_option = tk.StringVar()
quality_option.set("high")


## Instruction to user
Ins = "Paste your YouTube Link to Start Downloading"
write = ttk.Label(root, text=Ins, font=("Helvetica", 15), foreground="#066691", padding=10,  background="black")
write.grid(row=0, column=0)


## Input bar for user's input
entry = ttk.Entry(root, width=60)
entry.grid(row=1, column=0)
entry.bind("<Return>", get_input)


## Format for Download Button
download_button = tk.Button(root, text="Download", command=lambda: get_input("<Return>"), foreground="white", background="red")
download_button.grid(row=2, column=0, sticky="e", pady=5, padx=(0, 30))
download_button.configure(borderwidth=5, relief="flat")


## Format for download options
vidText = "Please select file type:\t"
video_frame = tk.Frame(root)
video_frame.grid(row=3, column=0, sticky="e", padx=(0, 100))
video_option = tk.Radiobutton(video_frame, text="Video", variable=download_option, value="Video", foreground="white", background="black")
audio_option = tk.Radiobutton(video_frame, text="Audio", variable=download_option, value="Audio", foreground="white", background="black")
vidType = tk.Label(root, text=vidText, foreground="white", background="black")

## Positioning download options
## Styling
vidType.grid(row=3, column=0, sticky="w", padx=(5, 0))
video_option.grid(row=0, column=0)
audio_option.grid(row=0, column=1)
video_option.configure(selectcolor="black")
audio_option.configure(selectcolor="black")


## Format for download quality options
qualText = "Please select file quality: "
quality_frame = tk.Frame(root)
quality_frame.grid(row=4, column=0, sticky="e", padx=(0, 114))
quality1 = tk.Radiobutton(quality_frame, text="High", variable=quality_option, value="high", foreground="white", background="black")
quality2 = tk.Radiobutton(quality_frame, text="Low", variable=quality_option, value="low", foreground="white", background="black")
vidQual = tk.Label(root, text=qualText, foreground="white", background="black")

## Positioning download quality options
## Styling
vidQual.grid(row=4, column=0, sticky="w", padx=(5, 0))
quality1.grid(row=0, column=0)
quality2.grid(row=0, column=1)
quality1.configure(selectcolor="black")
quality2.configure(selectcolor="black")


root.mainloop()
