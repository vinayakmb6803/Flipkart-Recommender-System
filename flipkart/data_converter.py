import pandas as pd
import os
from langchain_core.documents import Document


class DataConverter:
    def __init__(self,file_path:str): # filepath is basically the filpkat data file
        self.file_path = file_path

    def convert(self):
        df =pd.read_csv(self.file_path)[["product_title","review"]]
        #convert the dataframe to a list of Document objects
        docs = [
            Document(
                page_content=row["review"],
                metadata={"product_name": row["product_title"]}
            ) for _, row in df.iterrows()
        ]
        return docs
    
