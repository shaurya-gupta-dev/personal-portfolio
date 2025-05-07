def generate_caption():

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
    other = input("enter any extra detail you want. leave empty if no use: ")
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

def generate_hashtags():
    import requests

    API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
    headers = {"Authorization": "Bearer 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"}

    def generate():
        niche = input("Enter the niche (e.g., Fitness, Tech, Fashion): ")
        product = input("Enter the product/topic (e.g., Protein powder, Smartwatch): ")
        keywords = input("Enter any keyword you want (leave empty if not applicable): ")

        payload = {
        "messages": [
            {
                "role": "user",
                "content": f"You are a viral marketing expert. Based on the niche '{niche}', the product '{product}', and the keywords '{keywords}', generate 10 trending and viral Instagram hashtags. Use a mix of popular and niche tags. Only return the hashtags, nothing else. and don't just give the inputs again that i given."

            }
        ],
        "model": "deepseek/deepseek-v3-0324",
        }

        response = requests.post(url=API_URL, headers=headers, json=payload)
        data = response.json()
        generated_hashtags = (data["choices"][0]["message"]["content"])
        print(generated_hashtags)

        # with open("hashtags.txt", "a") as hashtags:
        #     hashtags.write(f"niche : {niche}, product : {product},keywords : {keywords} \n")
        #     hashtags.write(data["choices"][0]["message"]["content"])

        with open("hashtags.txt", "a", encoding="utf-8") as hashtags:
            hashtags.write(f"Niche: {niche}, Product: {product}, Keywords: {keywords}\n\n")
            hashtags.write("Hashtags:" + "\n" + generated_hashtags + "\n\n\n")

        take_input()

    def take_input():
        a = input("Press Enter to start or type 'exit' to exit the program: ")
        if a == "":
            generate()
        elif a == "exit":
            print("Program exited...")
            exit()
        else:
            print("invalid input")
            take_input()


    take_input()

def rewrite_script():
    import requests
    import pyfiglet
    from colorama import Fore, init
    import time

    API_URL = "https://router.huggingface.co/novita/v3/openai/chat/completions"
    headers = {"Authorization": "Bearer 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"}

    init(autoreset = True)

    banner = pyfiglet.figlet_format("SCRIPT REWRITER")
    print(Fore.LIGHTYELLOW_EX + banner)
    time.sleep(1)
    print(Fore.GREEN + "Welcome to script rewriter bot.")
    time.sleep(1)
    print(Fore.BLUE + "Please enter the respective details below.")
    time.sleep(1)
    platform = input("Enter the name of platform for which your script is: ")
    vibe = input("Enter the vibe in which you want your script: ")
    sample = input("Enter your script here which you want to be rewrite: ")
    print("Rewriting, please wait")
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"You are a professional YouTube script writer known for creating viral, high-retention videos. Rewrite the following script for the platform: {platform}, using a {vibe} tone. Make the first 10 seconds extremely hook-driven, use emotional storytelling, add urgency, and ensure a natural, conversational tone. Do not repeat my input. Only return the final rewritten script, clearly structured. Script: {sample}"

            }
        ],
        "model": "deepseek/deepseek-v3-0324",
        }

    response = requests.post(url=API_URL, headers=headers, json=payload)
    data = response.json()
    script = (data['choices'][0]['message']['content'])
    print(script)

    def download():
        a = input("do you want to download the downloaded script, y/n: ")
        if a == "y":
            with open("scripts.txt", "a", encoding="utf-8") as scripts:
                scripts.write(f"{script} \n\n\n")
        elif a == "n":
            print("ok")
        else:
            print("invalid input, please try again")
            download()

starting = input("Press Enter to start or type 'exit' to exit the program: ")
if starting == "":
    print("Welcome to 3 in 1 tool")
    print("1. Caption generator")
    print("2. Hashtag generator")
    print("3. Script rewriter")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        generate_caption()
    elif choice == "2":
        generate_hashtags()
    elif choice == "3":
        rewrite_script()
    elif choice == "4":
        print("Program exited...")
        exit()
    else:
        print("Invalid input, please try again.")
elif starting == "exit":
    print("Program exited...")
    exit()
else:
    print("Invalid input")
