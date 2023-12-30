"""
This module handles all the GUI formats for end-user
"""
import customtkinter
from tkinter import *
from main import VidDownloader

#Initialization of GUI module and window formatting
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Youtube Downloader")
root.geometry("380x180+400+200")
root.resizable(False, False)

def change_theme(theme):
	"""
	Function to Switch between Light and dark mode
	
	theme (str): This is the theme passed as a parameter
	
	By default code uses system mode as default value for theme
	"""
	if theme == "light":
		customtkinter.set_appearance_mode("light")
		write.configure(text_color="#3f48cc")
		vidType.configure(text_color="black")
		video_option.configure(text_color="black", fg_color="#3f48cc")
		audio_option.configure(text_color="black", fg_color="#3f48cc")
		vidQual.configure(text_color="black")
	elif theme == "dark":
		customtkinter.set_appearance_mode("dark")
		write.configure(text_color="#00eeff")
		vidType.configure(text_color="white")
		video_option.configure(text_color="white", fg_color="#00eeff")
		audio_option.configure(text_color="white", fg_color="#00eeff")
		vidQual.configure(text_color="white")

# Create Menu Bar for Options from User
my_menu = Menu(root)
root.config(menu=my_menu)

theme_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Themes", menu=theme_menu)
theme_menu.add_command(label="Light", command=lambda: change_theme("light"))
theme_menu.add_command(label="Dark", command=lambda: change_theme("dark"))

#Font formatting
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
	
	download_status = customtkinter.CTkFrame(root, fg_color="transparent")
	download_status.grid(row=2, column=0, padx=(5, 0), sticky="w")
	progress_bar = customtkinter.CTkProgressBar(download_status)
	progress_bar.grid(row=1, column=0)

	try:
		test = VidDownloader(user_input)

		# Create a new label widget
		test.download_audVid(download_option.get(), quality(optionmenu_var.get()))
		get_input.write1= customtkinter.CTkLabel(download_status, text=good, font=customFont, text_color="green")
		get_input.write1.grid(row=0, column=0, sticky="w")
		progress_bar.configure(mode="determinate", progress_color="green")
		progress_bar.set(1)	
		progress_bar.stop()
	except Exception as e:
		# Handle exceptions and display an error message
		get_input.write1 = customtkinter.CTkLabel(download_status, text=bad, font=customFont, text_color="red")
		get_input.write1.grid(row=0, column=0, sticky="w")
		progress_bar.configure(mode="determinate", progress_color="red")
		progress_bar.set(0)
		progress_bar.stop()


## Gets download option and sets default option
download_option = customtkinter.StringVar()
download_option.set("Video")


## Gets download quality option and sets default option
quality_option = customtkinter.StringVar()
quality_option.set("high")


## Instruction to user
Ins = "The YouTube Video Downloader"
write = customtkinter.CTkLabel(root, text=Ins, 
							   font=customtkinter.CTkFont("Comic Sans MS", 15, "bold"), 
							   text_color="#00eeff", 
							   padx=10)
write.grid(row=0, column=0)


## Input bar for user's input
entry = customtkinter.CTkEntry(root, width=350)
entry.configure(corner_radius=5, 
				placeholder_text="Paste the youtube video URL", 
				placeholder_text_color="grey", 
				font=customFont)
entry.grid(row=1, column=0, padx=15)
entry.bind("<Return>", get_input)


## Format for Download Button
download_button = customtkinter.CTkButton(root, text="Download", command=lambda: get_input("<Return>"))
download_button.configure(text_color="white", 
						  fg_color="red", 
						  corner_radius=5, 
						  hover=True, width=80, 
						  hover_color="#ff5057", 
						  font=customFont)
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
video_option.configure(radiobutton_width=10, 
					   radiobutton_height=10, 
					   fg_color="#00eeff", 
					   font=customFont)
audio_option.configure(radiobutton_width=10, 
					   radiobutton_height=10, 
					   fg_color="#00eeff", 
					   font=customFont)
video_option.grid(row=0, column=0)
audio_option.grid(row=0, column=1)


## Format for download quality options
qualText = "Please select file quality:\t"
quality_frame = customtkinter.CTkFrame(root, fg_color="transparent")
quality_frame.grid(row=4, column=0, padx=(0, 130), sticky="e")
vidQual = customtkinter.CTkLabel(root, text=qualText, text_color="white", font=customFont)

## Positioning download quality options
## Styling
vidQual.grid(row=4, column=0, sticky="w", padx=(5, 0))

##returuns the value of the option menu
def quality(choice):
	return (choice)

## option menu for selecting video Options
optionmenu_var = customtkinter.StringVar(value="720p")
optionmenu = customtkinter.CTkOptionMenu(quality_frame,values=["720p", "480p", "360p", "240p"],
                                         command=quality,
                                         variable=optionmenu_var)
optionmenu.configure(width=20,
					 font=customFont,
					 button_color="red",
					 fg_color="red", 
					 button_hover_color="#ff5057")
optionmenu.grid(row=0, column=0, sticky="w")


root.mainloop()
