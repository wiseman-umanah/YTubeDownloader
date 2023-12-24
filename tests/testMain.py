import main
import os
import unittest

class MajorTest(unittest.TestCase):
	def setUp(self):
		self.link = "https://youtu.be/eKwdX2An2ts?si=xmnjOOHlSlKMVayH"
		self.path2 = os.path.expanduser("~\Downloads")
	def test_classExist(self):
		backend = main.VidDownloader(self.link)
		self.assertIsNotNone(backend)
	def test_init1(self):
		path2 = os.path.expanduser("~\Downloads")
		backend = main.VidDownloader(self.link)
		self.assertEqual(backend.download_path, self.path2)
	def test_init2(self):
		with self.assertRaises(TypeError):
			backend = main.VidDownloader("")
	def test_init3(self):
		with self.assertRaises(TypeError):
			backend = main.VidDownloader(None)
	def test_init4(self):
		with self.assertRaises(TypeError):
			backend = main.VidDownloader("Wrong Value")
	def test_getValue(self):
		backend = main.VidDownloader(self.link)
		self.assertEqual(self.link, "https://youtu.be/eKwdX2An2ts?si=xmnjOOHlSlKMVayH")
	def test_setValue(self):
		backend = main.VidDownloader(self.link)
		with self.assertRaises(TypeError):
			backend.link = "Fail"


if __name__ == "__main__":
	unittest.main()
