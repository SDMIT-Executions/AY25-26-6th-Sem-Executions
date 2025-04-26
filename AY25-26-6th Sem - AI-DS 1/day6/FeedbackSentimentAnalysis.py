# sentiment analysis using textblob
# pip install textblob
from textblob import TextBlob
line = input("Tell us your feedback ")
sentiment = TextBlob(line).sentiment.polarity
if sentiment > 0:label = "Positive"
elif sentiment < 0:label = "Negative"
else: label = "Neutral"
print(line,label,sentiment)