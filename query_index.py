import os
import logging
import sys
from llama_index import GPTSimpleVectorIndex

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# 设置api key
api_key = os.getenv('OPENAI_API_KEY', default="<填入你的api key>")
# 加载索引
new_index = GPTSimpleVectorIndex.load_from_disk('index.json')
# 查询索引
response = new_index.query("What did the author do in 9th grade?")
# 打印答案
print(response)
