## 安装
```
conda create -n deep python=3.10 
conda activate deep 
pip install -r requirements.txt 
```

## 注册 deepseek 账号
* https://www.deepseek.com/ 
* 申请 appkey
* 编辑 uitls/funtion.py

```
client = OpenAI(
  base_url = "https://api.deepseek.com/v1",
  api_key = "xxxx"  <<==替换成自己的
)
```

## 运行
```
python app.py
```