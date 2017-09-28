import preprocessor
from cleanTweet import CleanTweet
from remover import Remove
from emotionHandler import EmotionHandler
from tweet import Tweet

class TweetProcessor(object):
    def __init__(self):
        self.cleaner = CleanTweet()
        self.remover = Remove()

    def cleanTweet(self,stringList):
        tweetList = []
        for text in stringList:
            for cleanup_method in self.cleaner.iterate():
                text = cleanup_method(text)
            rawTokens = preprocessor.preprocess(text)
            finalTokens = self.remover.remove_hashtag(rawTokens)
            for token in finalTokens:
                if token == 'rt':
                    finalTokens.remove(token)
            if len(finalTokens) >= 1: 
                tweetList.append(Tweet(text,finalTokens))
        return tweetList

    def getTweetEmotion(self,stringList,apiKey):
        self.emotionHandler = EmotionHandler(apiKey)
        emotionList = []
        tweets = self.cleanTweet(stringList)
        emotionList = self.emotionHandler.getEmotion(tweets)
        return emotionList
        