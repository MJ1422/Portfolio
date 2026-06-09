import gradio as gr

def hello(image):
    return "SkinSense AI Ready"

demo = gr.Interface(
    fn=hello,
    inputs=gr.Image(),
    outputs=gr.Textbox()
)

demo.launch(share=True)