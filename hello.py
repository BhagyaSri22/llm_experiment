#!/usr/bin/env python3


import os
os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'

print('Starting to build index')
from llama_index import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
query_engine.query("<question_text>?")