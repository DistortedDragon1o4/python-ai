import requests
import json

API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-1-pythia-12b"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def promptGen():
    crntPrompt = input("Please ask your question: ")
    if crntPrompt.lower() == "exit":
        return "exit"
    crntPrompt = "<|prompter|>" + crntPrompt + "<|endoftext|><|assistant|>"
    return crntPrompt

def promptQuery(prompt):
    outputStr = prompt
    output = []
    i = 0
    while i < 10:
        output = query({"inputs": outputStr, "parameters": {"temperature": 1.0}})
        try:
            outputStr = output[0]["generated_text"]
        except:
            print(output["error"])
            break
        i += 1
    outputStr += "<|endoftext|>"
    return outputStr

def fetchReply(output):
    i1 = output.rfind("<|assistant|>")
    i2 = output.rfind("<|endoftext|>")
    return output[i1 + 13:i2]

def deleteLast(output):
    i = output.find("<|endoftext|>")
    output = output[i + 13:]
    i = output.find("<|endoftext|>")
    return output[i + 13:]

def numPrompts(output):
    return output.count("<|assistant|>")

allPrompts = ""

while True:
    prompt = promptGen()
    if prompt == "exit":
        break
    output = promptQuery(allPrompts + prompt)
    print(fetchReply(output))
    allPrompts = output
    if numPrompts(allPrompts) > 5:
        deleteLast(allPrompts)
