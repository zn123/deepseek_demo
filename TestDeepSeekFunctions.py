import unittest
import os

# 假设上述代码位于名为utile.funtion.py的文件中
from utils.funtion import text_to_speech,GetDeepseekMsg


class TestDeepSeekFunctions(unittest.TestCase):

    def setUp(self):
        # 设置测试前的准备工作
        self.test_text = "你好，世界！"
        self.test_history = []

    # def tearDown(self):
    #     # 清理测试后留下的文件或数据
    #     if os.path.exists('./audio_cache/'):
    #         for file in os.listdir('./audio_cache/'):
    #             os.remove(os.path.join('./audio_cache/', file))
    #         os.rmdir('./audio_cache/')


    def test_text_to_speech(self):
        # 测试text_to_speech函数
        path = text_to_speech(self.test_text)
        self.assertTrue(os.path.exists(path))  # 检查文件是否存在
        # self.assertIn(self.test_text, path)  # 检查文件路径中是否包含测试文本的时间戳


    def test_GetDeepseekMsg(self):
        # 测试GetDeepseekMsg函数
        _, history, update_audio = GetDeepseekMsg(self.test_text, self.test_history)
        print(history[-1]["content"])
        self.assertNotEqual(history[-1]["content"], "你好，Python！")  # 检查历史记录是否正确更新
        self.assertTrue(os.path.exists(update_audio))  # 检查音频文件是否存在
        # self.assertIn("audio_", update_audio)  # 检查音频文件名是否正确


if __name__ == '__main__':
    unittest.main()