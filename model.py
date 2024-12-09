import pickle
import pandas as pd
import numpy as np


class SentimentRecommender:
   
     def __init__(self):
       
     
         self.user_final_rating = pickle.load(open(
              'user_final_rating.pkl','rb'))

         self.self_mapping =pickle.load(open(
             'prod_id_name_mapping.pkl','rb'))
        
     def top5_recommendations(self, user_name_input):
        
         if user_name_input not in self.user_final_rating.index:
             print(f"The User {user_name_input} does not exist. Please provide a valid user name")
             return None
         else:
             # Get top 20 recommended products from the best recommendation model
             recommendations = self.user_final_rating.loc[user_name_input].sort_values(ascending=False)[0:5]
             mapping= self.self_mapping[['id','name']]
             mapping = pd.DataFrame.drop_duplicates(mapping)
             recommendations = pd.merge(recommendations,mapping, left_on='id', right_on='id', how = 'left')
             result=recommendations['name']
         return result