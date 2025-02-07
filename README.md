- 2025.2 deepseek api 申请平替网站，deepseek 官网api已经不能用了
硅基流动：https://cloud.siliconflow.cn/i/myqE5Km4
- 2025.1 DeepSeek-R1 上线 API，对用户开放思维链输出，通过设置 model='deepseek-reasoner' 即可调用。

## 安装
```
conda create -n deep python=3.10 
conda activate deep 
pip install -r requirements.txt 
```

## 注册 deepseek 账号
* https://www.deepseek.com/ 
* 申请 appkey
* 编辑 utils/funtion.py

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