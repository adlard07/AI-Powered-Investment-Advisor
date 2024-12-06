from typing import Union, List, Optional
import chromadb
import os

from dataclasses import dataclass
from utils.logger import logging
from utils.utils import split_dataset


@dataclass
class Talk2Chroma:
    chroma_db_path: str = 'database'
    distance_measure: str = 'cosine'
    embeddings: str = ''

    def __post_init__(self):
        self.client = chromadb.PersistentClient(path=self.chroma_db_path)
        logging.info(f"Heartbeat: {self.client.heartbeat()}")


    def vector_embedding(self, document):
        '''
        Converts text into multidimentional vector embeddings (numerical representation for plain text)
        Args:
            1. Document
        Returns:
            Tensor of embeddings
        '''


    def add_to_collection(self, collection_name: str, document: Union[str, List[str]], ids: Union[str, List[str]], splits: int) -> None:
        '''
        Creates collection if doesnt exist, splits the document into chunks and pushes it into db
        Args:
            1. Collection name
            2. Document (string or list)
            3. Ids (string or list)
            4. Number of split (int)
        Returns:
            None
        '''
        try:
            # check whether the lengths maths
            if len(document) != len(ids):
                raise ValueError('Lengths of document and Ids do not match')


            # get or create collection
            collection = self.client.get_or_create_collection(name=collection_name)
            logging.info(f"Collection {collection_name} initiated!")

            # check the datatype of the document and ids
            if isinstance(document, str) and isinstance(ids, str):
                collection.add(documents=[document], ids=[ids])
                logging.info(f"Document added to collection {collection_name}!")

            elif isinstance(document, List) and isinstance(ids, List):
                document_splits = split_dataset(dataset=document, split_count=splits)
                ids_split = split_dataset(dataset=ids, split_count=splits)

                for i in range(len(document_splits)):
                    collection.add(documents=document_splits[i], ids=ids_split[i]) 

            else:
                raise ValueError('The document and Ids datatype do not match!')

            logging.info(f"Document added to collection '{collection_name}'")

        except Exception as e:
            logging.error(f"Error occurred while creating collection: {e}")


    def delete(self, collection_name: str, ids: Optional[Union[str, List]]) -> None:
        '''
        Deletes the ids that are passed as a parameter, if none are passed deletes the entire collection

        Args: 
            1. collection_name: Name of the collection to delete
            2. ids: Ids of the document

        Returns: 
            None
        '''
        try:
            collection = self.client.get_collection(name=collection_name)
            if ids:
                if isinstance(ids, str):
                    collection.delete(ids=[ids])
                elif isinstance(ids, List[str]):
                    collection.delete(ids=ids)

            else:
                # deletes the whole collection
                collections = [coll.name for coll in self.client.list_collections()]
                if collection_name in collections:
                    self.client.delete_collection(collection_name)
                    logging.info(f"Document deleted from collection {collection_name}")
                else:
                    logging.info(f"Collection '{collection_name}' does not exist!")


        except Exception as e:
            logging.error(f"Error occurred while deleting from collection: {e}")





def main(collection_name: str, text: Union[str, List[str]], ids: Union[str, List[str]]) -> None:
    db = Talk2Chroma()
    client = db.client

    # Add data into the collection
    db.add_to_collection(collection_name, text, ids, 3)

    # Delete the collection
    db.delete(collection_name, '2')

    logging.info([coll.name for coll in client.list_collections()])
    logging.info(client.get_collection(collection_name).peek())

if __name__ == '__main__':
    collection_name = 'test'
    text = ['This is a test text to test that the test script works.',
    'This is a 2nd test script to test that the test sript works on list.',
    'I need to tough grass!']

    ids = ['1', '2', '3']

    main(collection_name, text, ids)