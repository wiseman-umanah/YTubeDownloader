import tkinter as tk
from tkinter import ttk
from main import VidDownloader

root = tk.Tk()
root.title("Youtube Downloader")
# root.geometry(newGeometry="600x120")
# root.resizable(False, False)

def get_input(event):
	user_input = entry.get()
	
	# Destroy the existing label if it exists
	if hasattr(get_input, 'write1') and get_input.write1.winfo_exists():
		get_input.write1.destroy()
	
	try:
		test = VidDownloader(user_input)

		# Create a new label widget
		get_input.write1 = ttk.Label(root, text=" ", font=("Helvetica", 10))
		get_input.write1.grid(row=0, column=2, rowspan=1)
		if download_option.get() == "Video":
			test.vid()
		elif download_option.get() == "Audio":
			test.only_audio()
		get_input.write1.config(text="Succesfully Downloaded!!!", font=("Helvetica", 10), foreground="green")
		get_input.write1.grid(row=0, column=2, rowspan=1)
	except Exception as e:
		# Handle exceptions and display an error message
		get_input.write1 = ttk.Label(root, text="Download Failed!!", foreground="red")
		get_input.write1.grid(row=2, column=0)

download_option = tk.StringVar()
download_option.set("Video")

quality_option = tk.StringVar()
quality_option.set("High")

write = ttk.Label(root, text="Paste your youtube Link to Start Downloading", font=("Helvetica", 15), foreground="#066691", padding=10)
write.grid(row=0, column=1, rowspan=2, pady=(0, 50))

entry = ttk.Entry(root, width=80)
entry.grid(row=1, column=1, rowspan=2, pady=(0, 30), padx=15)
entry.bind("<Return>", get_input)

download_button = tk.Button(root, text="Download", command=lambda: get_input("<Return>"), foreground="white", background="red")
#download_button.grid(row=2, column=3)

video_option = tk.Radiobutton(root, text="Video", variable=download_option, value="Video")
audio_option = tk.Radiobutton(root, text="Audio", variable=download_option, value="Audio")

#video_option.grid(row=3, column=0)
#audio_option.grid(row=3, column=1)

quality1 = tk.Radiobutton(root, text="High", variable=quality_option, value="high")
quality2 = tk.Radiobutton(root, text="Low", variable=quality_option, value="low")

#quality1.grid(row=4, column=0)
#quality2.grid(row=4, column=1)

root.mainloop()
