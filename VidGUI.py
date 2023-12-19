import tkinter as tk
from tkinter import ttk
from main import VidDownloader

root = tk.Tk()
root.title("Youtube Downloader")
root.geometry(newGeometry="430x180")
root.resizable(False, False)
root.configure(bg="black", fg="white")


def get_input(event):
	user_input = entry.get()
	
	# Destroy the existing label if it exists
	if hasattr(get_input, 'write1') and get_input.write1.winfo_exists():
		get_input.write1.destroy()
	
	try:
		test = VidDownloader(user_input)

		# Create a new label widget
		get_input.write1 = ttk.Label(root, text=" ", font=("Helvetica", 10))
		get_input.write1.grid(row=2, column=0, padx=(5, 0), pady=(20, 10), sticky="w")
		test.download_audVid(quality_option.get(), download_option.get())
		get_input.write1.config(text="Downloaded Successful!!!", font=("Helvetica", 10), foreground="green")
		get_input.write1.grid(row=2, column=0, padx=(5, 0), pady=(20, 10), sticky="w")
	except Exception as e:
		# Handle exceptions and display an error message
		get_input.write1 = ttk.Label(root, text="Download Failed!!", foreground="red")
		get_input.write1.grid(row=2, column=0, padx=(5, 0), pady=(20, 10), sticky="w")

download_option = tk.StringVar()
download_option.set("Video")

quality_option = tk.StringVar()
quality_option.set("high")

write = ttk.Label(root, text="Paste your youtube Link to Start Downloading", font=("Helvetica", 15), foreground="#066691", padding=10)
write.grid(row=0, column=0)

entry = ttk.Entry(root, width=60)
entry.grid(row=1, column=0)
entry.bind("<Return>", get_input)

download_button = tk.Button(root, text="Download", command=lambda: get_input("<Return>"), foreground="white", background="red")
download_button.grid(row=2, column=0, sticky="e", pady=5, padx=(0, 30))

video_frame = tk.Frame(root)
video_frame.grid(row=3, column=0, sticky="e", padx=(0, 100))
video_option = tk.Radiobutton(video_frame, text="Video", variable=download_option, value="Video")
audio_option = tk.Radiobutton(video_frame, text="Audio", variable=download_option, value="Audio")
vidType = tk.Label(root, text="Please select file type: ").grid(row=3, column=0, sticky="w", padx=(5, 0))

video_option.grid(row=0, column=0)
audio_option.grid(row=0, column=1)

quality_frame = tk.Frame(root)
quality_frame.grid(row=4, column=0, sticky="e", padx=(0, 114))
quality1 = tk.Radiobutton(quality_frame, text="High", variable=quality_option, value="high")
quality2 = tk.Radiobutton(quality_frame, text="Low", variable=quality_option, value="low")
vidQual = tk.Label(root, text="Please select file quality: ").grid(row=4, column=0, sticky="w", padx=(5, 0))

quality1.grid(row=0, column=0)
quality2.grid(row=0, column=1)

root.mainloop()
