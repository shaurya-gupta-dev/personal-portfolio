import gradio as gr
import requests
import time
from colorama import Fore, init
import pyfiglet

API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
HEADERS = {"Authorization": "Bearer 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"}

def generate_caption(niche, vibe, product, other):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"niche : {niche}, vibe : {vibe}, product : {product}, extra : {other}, generate some captions with these information"
            }
        ],
        "model": "deepseek/deepseek-v3-0324",
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()["choices"][0]["message"]['content']

def generate_hashtags(niche, product, keywords):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"You are a viral marketing expert. Based on the niche '{niche}', the product '{product}', and the keywords '{keywords}', generate 10 trending and viral Instagram hashtags. Use a mix of popular and niche tags. Only return the hashtags, nothing else. and don't just give the inputs again that I gave."
            }
        ],
        "model": "deepseek/deepseek-v3-0324",
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    hashtags = response.json()["choices"][0]["message"]["content"]
    with open("hashtags.txt", "a", encoding="utf-8") as file:
        file.write(f"Niche: {niche}, Product: {product}, Keywords: {keywords}\n\n")
        file.write("Hashtags:\n" + hashtags + "\n\n\n")
    return hashtags

def rewrite_script(platform, vibe, sample):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"You are a professional YouTube script writer known for creating viral, high-retention videos. Rewrite the following script for the platform: {platform}, using a {vibe} tone. Make the first 10 seconds extremely hook-driven, use emotional storytelling, add urgency, and ensure a natural, conversational tone. Do not repeat my input. Only return the final rewritten script, clearly structured. Script: {sample}"
            }
        ],
        "model": "deepseek/deepseek-v3-0324",
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    script = response.json()['choices'][0]['message']['content']
    return script

def save_script(script):
    with open("scripts.txt", "a", encoding="utf-8") as file:
        file.write(script + "\n\n\n")
    return "Script saved successfully!"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 3-in-1 Tool")
    gr.Markdown("### Choose a tool below:")

    with gr.Tab("Generate Caption"):
        with gr.Row():
            niche = gr.Textbox(label="Niche (e.g., Fitness, Tech, Fashion)")
            vibe = gr.Textbox(label="Vibe (e.g., Funny, Professional, Motivational)")
            product = gr.Textbox(label="Product/Topic (e.g., Protein powder, Smartwatch)")
            other = gr.Textbox(label="Extra Details (optional)")
        caption_output = gr.Textbox(label="Generated Caption", interactive=False)
        caption_button = gr.Button("Generate Caption")
        caption_button.click(generate_caption, inputs=[niche, vibe, product, other], outputs=caption_output)

    with gr.Tab("Generate Hashtags"):
        with gr.Row():
            niche = gr.Textbox(label="Niche (e.g., Fitness, Tech, Fashion)")
            product = gr.Textbox(label="Product/Topic (e.g., Protein powder, Smartwatch)")
            keywords = gr.Textbox(label="Keywords (optional)")
        hashtags_output = gr.Textbox(label="Generated Hashtags", interactive=False)
        hashtags_button = gr.Button("Generate Hashtags")
        hashtags_button.click(generate_hashtags, inputs=[niche, product, keywords], outputs=hashtags_output)

    with gr.Tab("Rewrite Script"):
        with gr.Row():
            platform = gr.Textbox(label="Platform (e.g., YouTube, Instagram)")
            vibe = gr.Textbox(label="Vibe (e.g., Funny, Professional, Motivational)")
            sample = gr.Textbox(label="Script to Rewrite", lines=5)
        script_output = gr.Textbox(label="Rewritten Script", interactive=False)
        rewrite_button = gr.Button("Rewrite Script")
        rewrite_button.click(rewrite_script, inputs=[platform, vibe, sample], outputs=script_output)

demo.launch()
