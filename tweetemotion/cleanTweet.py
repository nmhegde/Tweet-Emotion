import HTMLParser
import re

class CleanTweet(object):
	def __init__(self):
		self.htmlParser = HTMLParser.HTMLParser()

	def iterate(self):
		for cleanup_method in [self.escape_HTML,
							   self.remove_urls,
		                       self.remove_usernames,
		                       self.remove_na,
		                       self.decode_data,
		                       self.remove_special_chars,
		                       self.remove_numbers,
		                       self.remove_hashtags]:
			yield cleanup_method


	@staticmethod
	def remove_by_regex(tweet, regexp):
	    tweet = re.sub(regexp, "", tweet)
	    return tweet

	def escape_HTML(self,tweet):
		return self.htmlParser.unescape(tweet)

	def decode_data(self,tweet):
		return tweet.decode("utf8").encode('ascii','ignore')

	def remove_urls(self, tweet):
		return CleanTweet.remove_by_regex(tweet, re.compile(r"http.?://[^\s]+[\s]?"))
	
	def remove_na(self,tweet):
		if tweet != "Not Available":
			return tweet

	def remove_hashtags(self,tweet):
		return CleanTweet.remove_by_regex(tweet,re.compile(r"#(\w+)"))

	def remove_special_chars(self,tweet):
		for remove in map(lambda r: re.compile(re.escape(r)), [",", ":", "\"", "=", "&", ";", "%", "$",
	                                                                 "@", "%", "^", "*", "(", ")", "{", "}",
	                                                                 "[", "]", "|", "/", "\\", ">", "<", "-",
	                                                                 "!", "?", ".", "'",
	                                                                 "--", "---"]):
			tweet = re.sub(remove,"",tweet)
		return tweet

	def remove_usernames(self, tweet):
	    return CleanTweet.remove_by_regex(tweet, re.compile(r"@[^\s]+[\s]?"))

	def remove_numbers(self, tweet):
	    return CleanTweet.remove_by_regex(tweet, re.compile(r"\s?[0-9]+\.?[0-9]*"))
