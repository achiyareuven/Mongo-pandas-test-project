import pymongo
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
class Fetcher:
    def __init__(self):
       conn = os.getenv("MONGO_CONN")
       if not conn:
           raise ValueError ("not found env ")
       self.client = pymongo.MongoClient(conn)
       self.db = self.client["IranMalDB"]
       self.collection = self.db["tweets"]

    def to_data_frame(self):
        list_tweets = []
        for x in self.collection.find().limit(500):
            list_tweets.append(x)
        df= pd.DataFrame(list_tweets)
        df.rename(columns={'_id':'id','Text':'original_text'}, inplace=True)
        df["id"] = df["id"].astype(str)
        return df


# a= Fetcher()
# a.to_data_frame()

