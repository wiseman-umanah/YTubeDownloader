"""
This Module is the backbone of the youtube video/audio downloader
"""
from pytube import YouTube
import re
import os


class VidDownloader(YouTube):
	"""
	This class inherits from pytube to download youtube Video

	Parameters:
		link (any): The link passed to the class

	Attributes:
		download_audVid: This function downloads the video/audio from youtube
	
	Raises:
		TypeError: If argument is empty or None
		TypeError: If link fails to intialize
	"""
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
		"""Sets/Get the value of link
		
		Parameters:
			value: the new link that is set
		
		Raises:
			TypeError: If a wrong Url is passed
			
		"""
		return self.__link
	
	@link.setter
	def link(self, value):
		if re.match("http|https", value) is not None:
			self.__link = value
			self.ylink = YouTube(self.__link)
		else:
			raise TypeError("Wrong url passed")
		
	def download_audVid(self, quality="high", type="Video"):
		"""The function to download the audio/video from youtube
		
		Parameters:
			quality (str): The quality option of the youtube video
			
			type (str): The type of media whether Video or Audio
		"""
		if type == "Audio":
			if quality == "low":
				self.ylink.streams.filter(mime_type="audio/mp4", type="audio").order_by("bitrate").desc().last().download(self.download_path)
			else:
				self.ylink.streams.filter(mime_type="audio/mp4", type="audio").order_by("bitrate").desc().first().download(self.download_path)
		elif type == "Video":
			if quality == "low":
				self.ylink.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().last().download(self.download_path)
			else:
				self.ylink.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(self.download_path)
