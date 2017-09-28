### Tweet-Emotion - A library to clean your tweets and with an extension of getting emotion from indicio

#### How to install ?

```sh
git clone git@github.com:nmhegde/Tweet-Emotion.git && cd Tweet-Emotion
sudo python setup.py install
```

#### How to use the cleanTweet module?

```sh
from tweetemotion import TweetProcessor
obj = TweetProcessor()
#Sample list of tweets
stringList = ["Happy Drink Beer Day! #beer #drinkbeerday","RT @muftimenk: Many are guilty of this. We make ourselves unhappy because we're trapped in our own thoughts. Snap out of it. Have a positiv…"]
tokenList = obj.cleanTweet(stringList)
for token in tokenList: 
...     print "original String: {0},tokenlist: {1}".format(token.string,token.tokenList)
... 
original String: Happy Drink Beer Day  ,tokenlist: ['happy', 'drink', 'beer', 'day']
original String: RT Many are guilty of this We make ourselves unhappy because were trapped in our own thoughts Snap out of it Have a positiv, tokenlist: ['many', 'are', 'guilty', 'of', 'this', 'we', 'make', 'ourselves', 'unhappy', 'because', 'were', 'trapped', 'in', 'our', 'own', 'thoughts', 'snap', 'out', 'of', 'it', 'have', 'a', 'positiv']
```
Before you go ahead and use this module please get your free api-key from [Indico](https://indico.io)
#### How to get the emotion for your tweets?

```sh
from tweetemotion import TweetProcessor
obj = TweetProcessor()
#Sample list of tweets
stringList = ["Happy Drink Beer Day! #beer #drinkbeerday","RT @muftimenk: Many are guilty of this. We make ourselves unhappy because we're trapped in our own thoughts. Snap out of it. Have a positiv…"]
emotionList = obj.getTweetEmotion(stringList,apiKey="<Your Api-Key>")
for emotion in emotionList:
...     print "tokens: {0}\nfear: {1}\njoy: {2}\nsadness: {3}\nanger: {4}\nsurprise {5}".format(emotion.tokenList,emotion.fear,emotion.joy,emotion.sadness,emotion.anger,emotion.surprise)
... 
tokens: ['happy', 'drink', 'beer', 'day']
fear: 0.040277876
joy: 0.6477931738
sadness: 0.0429587737
anger: 0.028304141
surprise 0.2406660914
tokens: ['many', 'are', 'guilty', 'of', 'this', 'we', 'make', 'ourselves', 'unhappy', 'because', 'were', 'trapped', 'in', 'our', 'own', 'thoughts', 'snap', 'out', 'of', 'it', 'have', 'a', 'positiv']
fear: 0.1442052722
joy: 0.046138525
sadness: 0.5312283039
anger: 0.170050174
surprise 0.1083777398
```


