import requests
import time

API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
headers = {"Authorization": "Bearer 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"}

print("Welcome to caption generator bot.")
print("just put some details and get your captions.")
time.sleep(1)

niche = input("Enter the niche (e.g., Fitness, Tech, Fashion): ")
vibe = input("Enter the vibe (e.g., Funny, Professional, Motivational): ")
product = input("Enter the product/topic (e.g., Protein powder, Smartwatch): ")
other = input("enter any extra detail you want. leave epty if no use: ")
payload = {
"messages": [
    {
        "role": "user",
        "content": f"niche : {niche}, vibe : {vibe}, product : {product},extra : {other}, generate some captions with these information"
    }
],
"model": "deepseek/deepseek-v3-0324",
}
response = requests.post(API_URL, headers=headers, json=payload)
# print(response.json()["choices"][0]["message"])
print(response.json()["choices"][0]["message"]['content'])
