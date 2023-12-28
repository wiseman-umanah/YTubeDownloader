"""
This module handles all the GUI formats for end-user
"""
import customtkinter
from main import VidDownloader


#Initialization of GUI module and window formatting

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Youtube Downloader")
root.geometry("380x180+400+200")
root.resizable(False, False)

customFont = ("Comic Sans MS", 12, "bold")
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
		test.download_audVid(quality_option.get(), download_option.get())
		get_input.write1= customtkinter.CTkLabel(root, text=good, font=customFont, text_color="green")
		get_input.write1.grid(row=2, column=0, padx=(5, 0), sticky="w")
	except Exception as e:
		# Handle exceptions and display an error message
		get_input.write1 = customtkinter.CTkLabel(root, text=bad, font=customFont, text_color="red")
		get_input.write1.grid(row=2, column=0, padx=(5, 0), sticky="w")


## Gets download option and sets default option
download_option = customtkinter.StringVar()
download_option.set("Video")


## Gets download quality option and sets default option
quality_option = customtkinter.StringVar()
quality_option.set("high")


## Instruction to user
Ins = "The YouTube Video Downloader"
write = customtkinter.CTkLabel(root, text=Ins, font=customtkinter.CTkFont("Comic Sans MS", 15, "bold"), text_color="#00eeff", padx=10)
write.grid(row=0, column=0)


## Input bar for user's input
entry = customtkinter.CTkEntry(root, width=350)
entry.configure(corner_radius=5, placeholder_text="Paste the youtube video URL", placeholder_text_color="grey", font=customFont)
entry.grid(row=1, column=0, padx=15)
entry.bind("<Return>", get_input)


## Format for Download Button
download_button = customtkinter.CTkButton(root, text="Download", command=lambda: get_input("<Return>"))
download_button.configure(text_color="white", fg_color="red", corner_radius=5, hover=True, width=80, hover_color="#ff5057", font=customFont)
download_button.grid(row=2, column=0, sticky="e", pady=5, padx=(0, 15))


## Format for download options
vidText = "Please select file type:\t"
video_frame = customtkinter.CTkFrame(root, fg_color="transparent")
video_frame.grid(row=3, column=0, sticky="e")
video_option = customtkinter.CTkRadioButton(video_frame, text="Video", variable=download_option, value="Video", text_color="white")
audio_option = customtkinter.CTkRadioButton(video_frame, text="Audio", variable=download_option, value="Audio", text_color="white")
vidType = customtkinter.CTkLabel(root, text=vidText, text_color="white", font=customFont)

## Positioning download options
## Styling
vidType.grid(row=3, column=0, sticky="w", padx=(5, 0))
video_option.configure(radiobutton_width=10, radiobutton_height=10, fg_color="#00eeff", font=customFont)
audio_option.configure(radiobutton_width=10, radiobutton_height=10, fg_color="#00eeff", font=customFont)
video_option.grid(row=0, column=0)
audio_option.grid(row=0, column=1)


## Format for download quality options
qualText = "Please select file quality:\t"
quality_frame = customtkinter.CTkFrame(root, fg_color="transparent")
quality_frame.grid(row=4, column=0, sticky="e")
quality1 = customtkinter.CTkRadioButton(quality_frame, text="High", variable=quality_option, value="high", text_color="white")
quality2 = customtkinter.CTkRadioButton(quality_frame, text="Low", variable=quality_option, value="low", text_color="white")
vidQual = customtkinter.CTkLabel(root, text=qualText, text_color="white", font=customFont)

## Positioning download quality options
## Styling
vidQual.grid(row=4, column=0, sticky="w", padx=(5, 0))
quality1.configure(radiobutton_width=10, radiobutton_height=10, fg_color="#00eeff", font=customFont)
quality2.configure(radiobutton_width=10, radiobutton_height=10, fg_color="#00eeff", font=customFont)
quality1.grid(row=0, column=0)
quality2.grid(row=0, column=1)



root.mainloop()
