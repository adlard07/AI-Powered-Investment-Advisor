import pandas as pd

from data_ingestion.get_data import RequestDataset
from data_ingestion.chroma_db import Talk2Chroma
from utils.logger import logging


# request kaggle for the dataset
dataset_df = pd.DataFrame(RequestDataset().load_data())[['Sentiment', 'Sentence']]
logging.info(dataset_df.head())

# initiate chroma db
db = Talk2Chroma()
client = db.client

collection_name = 'financial_news'

db.add_to_collection()