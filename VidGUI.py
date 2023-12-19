import tkinter as tk
from tkinter import ttk
from main import VidDownloader

root = tk.Tk()
root.title("Youtube Downloader")
root.geometry(newGeometry="600x120")
root.resizable(False, False)

def get_input(event):
	user_input = entry.get()
	
	# Destroy the existing label if it exists
	if hasattr(get_input, 'write1') and get_input.write1.winfo_exists():
		get_input.write1.destroy()
	
	try:
		test = VidDownloader(user_input)

		# Create a new label widget
		get_input.write1 = ttk.Label(root, text=" ", font=("Helvetica", 10))
		get_input.write1.pack(side=tk.LEFT, padx=(1, 0), pady=(1, 0))
		if download_option.get() == "Video":
			test.vid()
		elif download_option.get() == "Audio":
			test.only_audio()
		get_input.write1.config(text="Succesfully Downloaded!!!", font=("Helvetica", 10), foreground="green")
		get_input.write1.pack(side=tk.LEFT, padx=(1, 0), pady=(1, 0))
	except Exception as e:
		# Handle exceptions and display an error message
		get_input.write1 = ttk.Label(root, text="Download Failed!!", foreground="red")
		get_input.write1.pack(side=tk.LEFT, padx=(1, 0), pady=(1, 0))
		print(e)

download_option = tk.StringVar()
download_option.set("Video")

write = ttk.Label(root, text="Paste your youtube Link to Start Downloading", font=("Helvetica", 15), foreground="#066691", padding=10)
write.pack()

entry = ttk.Entry(root, width=80)
entry.pack()
entry.bind("<Return>", get_input)

download_button = tk.Button(root, text="Download", command=lambda: get_input("<Return>"), foreground="white", background="red")
download_button.pack(side=tk.RIGHT, padx=(0, 50), pady=(5, 0))

video_option = tk.Radiobutton(root, text="Video", variable=download_option, value="Video")
audio_option = tk.Radiobutton(root, text="Audio", variable=download_option, value="Audio")

video_option.pack(side=tk.LEFT, padx=(1, 0), pady=(1, 0))
audio_option.pack(side=tk.LEFT, padx=(1, 0), pady=(1, 0))

root.mainloop()
