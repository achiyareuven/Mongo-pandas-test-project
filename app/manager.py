from app.fetcher import Fetcher
from  app.processor import TextProcessor

class Manager:
    def __init__(self,path_weapon_file:str):
        self.fetcher= Fetcher()
        self.processor= TextProcessor(path_weapon_file)

    def run(self):
        df= self.fetcher.to_data_frame()
        df=self.processor.process(df)
        return df.to_dict(orient="records")
# c=Manager(r"C:\Users\achiy\PycharmProjects\Mongo-pandas-test-project\data\weapon_list.txt")
# c.run()