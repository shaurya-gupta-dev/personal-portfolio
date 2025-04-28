import requests
import gradio as gr

API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
headers = {"Authorization": "Bearer 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"}

# Function that wraps your existing logic
def generate_captions(niche, vibe, product, other):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"niche : {niche}, vibe : {vibe}, product : {product}, extra : {other}, generate some captions with these information"
            }
        ],
        "model": "deepseek/deepseek-v3-0324",
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Handle potential errors
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("# 🖋️ Caption Generator Bot")
    gr.Markdown("**Enter details below and get high-quality captions instantly.**")

    with gr.Row():
        niche = gr.Textbox(label="Niche", placeholder="e.g., Fitness, Tech, Fashion")
        vibe = gr.Textbox(label="Vibe", placeholder="e.g., Funny, Professional, Motivational")

    with gr.Row():
        product = gr.Textbox(label="Product / Topic", placeholder="e.g., Protein powder, Smartwatch")
        other = gr.Textbox(label="Extra Detail", placeholder="Optional extra details...")

    output = gr.Textbox(label="Generated Captions", lines=8)

    generate_button = gr.Button("🚀 Generate Captions")

    generate_button.click(
        generate_captions,
        inputs=[niche, vibe, product, other],
        outputs=output
    )

app.launch()
