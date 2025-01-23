from openai import OpenAI
import pyttsx3
import os
import time
# 初始化TTS引擎
engine = pyttsx3.init()

# 定义文本转语音函数
def text_to_speech(text):
    # if not engine:
    #     engine = pyttsx3.init()
    time_stamp = time.strftime("%Y%m%d-%H%M%S")
    directory = './audio_cache/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = directory + 'audio_' + time_stamp + '.wav'
    engine.save_to_file(text, path)  # 将生成的语音保存到文件
    engine.runAndWait()  # 运行并等待语音合成完成
    return path  # 返回语音文件的路径

# 导入 OpenAI 模块（假设已正确安装）
# 创建 OpenAI 客户端实例，配置基础 URL 和 API 密钥
client = OpenAI(
  base_url = "https://api.deepseek.com/v1",
  api_key = "xxxx"
)

# 定义函数 GetDeepseekMsg，用于获取 DeepSeek 的响应消息
def GetDeepseekMsg(message, history):
    isStream = False  # 设置是否以流的方式获取响应，默认为否

    # 调用 OpenAI 客户端的 chat.completions.create 方法来生成回复
    completion = client.chat.completions.create(
      model="deepseek-reasoner",  # 使用指定的模型 deepseek-chat deepseek-reasoner
      messages=[{"role":"user","content":message}],  # 输入消息，指定角色为 "user" 并提供消息内容
      temperature=0.2,  # 控制生成文本的随机性，值越低，生成的文本越确定
      top_p=0.7,  # 核概率，用于筛选最可能的词
      max_tokens=1024,  # 限制生成文本的最大长度
      stream=isStream  # 是否以流的方式获取响应
    )

    if isStream:
      for chunk in completion:
        if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="")
    else:
      msg = completion.choices[0].message.content
      # print(msg)

    update_audio= text_to_speech(msg)
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": msg})
    # history.append(ChatMessage(role="user", content=message))
    # history.append(ChatMessage(role="assistant", content=msg))
    # time.sleep(2)
    return "", history,update_audio