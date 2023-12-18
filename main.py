from pytube import YouTube
import re

class VidDownloader(YouTube):
	def __init__(self, link=None):
		if link == None or "":
			raise TypeError("Only links to youtube videos are allowed")
		self.__link = link
		self.ylink = YouTube(link)
		for i  in  self.ylink.streams:
			print(i)

	@property
	def link(self):
		return self.__link
	
	@link.setter
	def link(self, value):
		if re.match("http|https", value) is not None:
			self.__link = value
			self.ylink = YouTube(self.__link)
		else:
			raise TypeError("Wrong url passed")
		
	def vid(self, path=None):
		self.ylink.streams.filter(progressive=True, file_extension="mp.4").order_by("resolution").desc.first().download()
	
	def only_audio(self, path=None):
		self.ylink.streams.filter(mime_type="audio/mp4", type="audio").order_by("resolution").desc.first().download()

	def vid_details(self):
		title = self.ylink.title
		author = self.ylink.author
		length = self.ylink.length
		return (title, author, length)


test = VidDownloader("https://youtu.be/Rm2YVbN7Zsw?si=w5Krz0BkFw7JsJIU")
print(test.link)
test.link = "http://youtu.be/Rm2YVbN7Zsw?si=w5Krz0BkFw7JsJIU"
print(test.link)