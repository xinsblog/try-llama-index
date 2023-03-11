import os
import logging
import sys
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# 设置api key
api_key = os.getenv('OPENAI_API_KEY', default="<填入你的api key>")
# 读取data文件夹下的文档
documents = SimpleDirectoryReader('data').load_data()
# 按最大token数500来把原文档切分为多个小的chunk，每个chunk转为向量，并构建索引
index = GPTSimpleVectorIndex(documents, chunk_size_limit=500)
# 保存索引
index.save_to_disk('index.json')

