import gradio as gr

from vision.face_detection import detect_face


def analyze(image):

    face = detect_face(image)

    if face is None:
        return None, "No face detected."

    return face, "Face detected successfully!"


with gr.Blocks(title="SkinSense AI") as demo:

    gr.Markdown("# SkinSense AI")
    gr.Markdown(
        "Upload a selfie for skin analysis."
    )

    image_input = gr.Image(
        type="pil",
        label="Upload Selfie"
    )

    analyze_btn = gr.Button(
        "Detect Face"
    )

    cropped_face = gr.Image(
        label="Detected Face"
    )

    result = gr.Textbox(
        label="Status"
    )

    analyze_btn.click(
        fn=analyze,
        inputs=image_input,
        outputs=[cropped_face, result]
    )

demo.launch()