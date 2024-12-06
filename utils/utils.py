import pandas as pd
import zipfile
import math
import io
from utils.logger import logging

def create_dataset(response) -> pd.DataFrame:
    '''
    Creates dataset out of zipped response object and returns dataframe

    Args:
        Takes api response as argument

    Returns:
        Dataframe 
    '''
    try:
        # Check if the content is a ZIP file
        if 'zip' in response.headers.get('Content-Type', ''):
            logging.info("ZIP file detected, extracting...")
            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            
            extracted_file = zip_file.namelist()[0]
            with zip_file.open(extracted_file) as my_file:
                # Load the file directly into a pandas DataFrame
                df = pd.read_csv(my_file)
                logging.info(f"{len(df.columns)} columns {len(df)} rows loaded successfully!")
                return df
        else:
            logging.info("No ZIP file found.")
            return None
    except Exception as e:
        logging.error(f"Exception occured: {e}")


def split_dataset(dataset, split_count):
    '''
    Splits dataset into chunks 
    Args:
        1. Dataset
        2. No. of splits
    Returns:
        Returns list with chunks of data
    '''
    try:
        splits = []
        split = 0
        single_split = math.ceil(len(dataset) / split_count)
        for i in range(split_count):
            splits.append(dataset[split:split+single_split])
            split += single_split
        return splits
    except Exception as e:
        logging.error(f"Exception occured: {e}")
