# Import dependencies
import nltk
from nltk.corpus import words
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd



class TextProcessor:
    def __init__(self,weapon_list:str =None):
        with open(weapon_list,"r")as file:
            self.weapon = file.read().split("\n")
        self.analyzer =  SentimentIntensityAnalyzer()

    def find_weapon(self,text:str):
        text_clean = text.lower().split()
        for word in text_clean:
            if word in self.weapon:
                return word
        return ""


    def find_rarest_word(self,text:str):
        count_word= {}
        text_clean = text.lower().split()
        for word in text_clean:
            if word in count_word:
                count_word [word] +=1
            else:
                count_word[word] = 1
        min_val = min(count_word.values())
        res = [k for k, v in count_word.items() if v == min_val]
        return res[0]

    def find_sentiment(self,text:str):
        score = SentimentIntensityAnalyzer().polarity_scores(text)["compound"]
        if score >= 0.5:
            return "positive"
        elif score <= -0.5:
            return "negative"
        else:
            return "neutral"


    def process(self,df:pd.DataFrame):
        df =df
        df["rarest_word"] = df["original_text"].apply(self.find_rarest_word)
        df["weapons_detected"] = df["original_text"].apply(self.find_weapon)
        df["sentiment"] =df ["original_text"].apply(self.find_sentiment)
        return df



# s= TextProcessor(r"C:\Users\achiy\PycharmProjects\Mongo-pandas-test-project\data\weapon_list.txt")
# s.find_weapon("gun ,mmm od")
#
# s=TextProcessor()
# s.find_sentiment("hgdfkhghk jherio ufgk jehrjnfk")
