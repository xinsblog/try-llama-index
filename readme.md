## 前置准备

### 安装依赖

```shell
pip3 install -r requirments.txt
```

### 获取openai的API Key

可以参考openai的官方文档：https://platform.openai.com/account/api-keys

## 运行

#### 在代码中填入API key，或者设置环境变量

```shell
export OPENAI_API_KEY=XXYYZZ
```

#### 建立索引

```shell
python3 build_index.py
```

#### 查询索引

```shell
python3 query_index.py
```