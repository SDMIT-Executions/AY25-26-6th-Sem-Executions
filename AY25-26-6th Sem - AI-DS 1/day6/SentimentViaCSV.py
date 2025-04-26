import csv
from textblob import TextBlob
def analysis():
    with open("dlithe.csv", "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        print(reader)
        for row in reader:
            for line in row:
                sentiment = TextBlob(line).sentiment.polarity
                if sentiment > 0:label = "Positive"
                elif sentiment < 0:label = "Negative"
                else: label = "Neutral"
                print(line,label,sentiment)
analysis()
