from xml.sax import make_parser
from xml.sax.handler import ContentHandler 
import re

class WikiHandler(ContentHandler):

	def __init__(self):
		self.inText = 0
		self.zatvorkyre = re.compile(r"\[+[^\[]*\]+")
		self.zatvorky1re = re.compile(r"\{+[^{]*\}+")
		self.uvodzovkyre = re.compile(r"'+[^']*'+")
		self.alphanumeric = re.compile(r"^[a-z]+$")

	def startElement(self, name, attrs):
		if name == 'text':
			self.inText = 1
			self.text = ""

	def endElement(self, name):
		if name == 'text':
			self.inText = 0
			self.processText()
			self.text = ""

	def characters(self, ch):
		if self.inText:
			self.text = self.text + " "+ ch

	def processText(self):
		c=self.text
		c=self.zatvorkyre.sub('',c)
		c=self.zatvorky1re.sub('',c)
		c=self.uvodzovkyre.sub('',c)
		c=c.lower()
		words=c.split()
		for w in words:
			if len(w)>3 and len(w)<9 and self.alphanumeric.match(w):
				print w

parser = make_parser()
curHandler = WikiHandler()
parser.setContentHandler(curHandler)
parser.parse(open('data/wiki.xml'))
