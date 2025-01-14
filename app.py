import gradio as gr

from utils.funtion import GetDeepseekMsg


with gr.Blocks() as demo:
    code = gr.Code(render=False)
    system_prompt = gr.Markdown("# 我是一个乐于助人的人工智能")
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(show_label=False)
    clear = gr.ClearButton([msg, chatbot])
    speech_file_path = gr.Audio(label="播放语音回应", type="filepath",autoplay=True,loop=False)

    msg.submit(GetDeepseekMsg, [msg, chatbot], [msg, chatbot,speech_file_path])

if __name__ == "__main__":
    demo.launch()