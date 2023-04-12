import requests
import json

API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-1-pythia-12b"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
# outputStr = "<|prompter|>tell me about India's history<|endoftext|><|assistant|>"
# output = []

# i = 0
# while i < 10:
#     output = query({"inputs": outputStr, "parameters": {"temperature": 1.11}})
#     outputStr = output[0]["generated_text"]
#     i += 1

# outputStr = outputStr + "<|endoftext|><|prompter|>tell me about yourself<|endoftext|><|assistant|>"

# i = 0
# while i < 10:
#     output = query({"inputs": outputStr})
#     outputStr = output[0]["generated_text"]
#     i += 1

# output = query({
# 	"inputs": "<|prompter|>What is a meme, and what\'s the history behind this word?<|endoftext|><|assistant|>The word \"meme\" was first used in the 1960s by Richard Dawkins to describe an idea, behavior, or style that is transmitted from one individual to another within a culture. The concept",
# })

# outputStr = output[0]["generated_text"]

def promptGen():
    crntPrompt = input("Please ask your question: ")
    crntPrompt = "<|prompter|>" + crntPrompt + "<|endoftext|><|assistant|>"
    return crntPrompt

def promptQuery(prompt):
    outputStr = prompt
    output = []
    i = 0
    while i < 10:
        output = query({"inputs": outputStr, "parameters": {"temperature": 1.11}})
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

prompt = promptGen()
output = promptQuery(prompt)
print(fetchReply(output))



# print(outputStr)
