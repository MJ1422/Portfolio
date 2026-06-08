import gradio as gr


def hello():
    return "Skin Type Ready"

demo = gr.Interface(
       fn = hello,
       inputs = "none",
       outputs = "text",
       title = "Skin Type Analysis"
)

demo.launch()