import json
import requests
from dataclasses import dataclass
import chromadb
import pandas as pd

from utils.logger import logging
from utils.utils import create_dataset


@dataclass
class RequestDataset:
    dataset_name: str = 'avisheksood/stock-news-sentiment-analysismassive-dataset'
    kaggle_json: str = 'kaggle.json'

    def __post_init__(self):
        self.dataset_url = f'https://www.kaggle.com/api/v1/datasets/download/{self.dataset_name}'

    def load_data(self) -> pd.DataFrame:
        '''
        Asynchronous function that makes request to the "https://www.kaggle.com/api/v1/datasets/" to
        pull zipped dataframe, unzips and returns dataframe.

        Args: None

        Returns:
            Dataframe pulled from "https://www.kaggle.com/api/v1/datasets/"
        '''
        with open(self.kaggle_json) as kaggle_key:
            headers = {
                'Authorization': f"Bearer {json.load(kaggle_key).get('key')}"
            }
            response = requests.get(self.dataset_url, headers=headers)

            if response.status_code == 200:
                logging.info("Request successful!")
            else:
                logging.info("Request failed!")
                return None

            self.dataset = create_dataset(response)
        return self.dataset


if __name__ == '__main__':
    dataset_df = RequestDataset().load_data()
