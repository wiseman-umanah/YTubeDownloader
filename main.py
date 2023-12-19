from pytube import YouTube
import re
import os

class VidDownloader(YouTube):
	def __init__(self, link=None):
		self.download_path = str(os.path.expanduser("~\Downloads"))
		if link == None or "":
			raise TypeError("Only links to youtube videos are allowed")
		try:
			self.__link = link
			self.ylink = YouTube(link)
		except:
			raise TypeError("Only links to youtube videos are allowed")


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
		
	def vid(self):
		print(self.download_path)
		self.ylink.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(self.download_path)
	
	def only_audio(self):
		self.ylink.streams.filter(mime_type="audio/mp4", type="audio").order_by("bitrate").desc().first().download(self.download_path)

