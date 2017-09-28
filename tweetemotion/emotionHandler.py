import indicoio
from emotion import Emotion

class EmotionHandler(object):
	def __init__(self,api_key):
		indicoio.config.api_key = api_key

	def getEmotion(self,tweets):
		emotionList = []
		for tweet in tweets:
			emotion = indicoio.emotion(" ".join(tweet.tokenList))
			emotionList.append(Emotion(tweet.string,tweet.tokenList,emotion["anger"],emotion["joy"],emotion["fear"],emotion["sadness"],emotion["surprise"]))
		return emotionList



