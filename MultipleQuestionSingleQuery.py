import time
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="",
    api_version="2023-07-01-preview",
    azure_endpoint="",
)

questions =[
    "How do I output all files in a directory using Python?",
    "what is the future of AI?",
    "what is the process of bill passing in Indian parliament?",
    "Who was the first president of the United States?",
    "Explain the process of photosynthesis and its importance in the ecosystem.",
    "How do you implement a binary search algorithm in Python?",
    "Who invented the light bulb?",
    "What is the chemical formula for water?",
    "Who won the Nobel Prize in Literature in 2023?",
    "Explain Einstein's theory of relativity."
]

#  Time taken to get the response: 24.46 seconds together for all questions at once but the answers are too short but concise
combined_questions="\n".join(questions)


start_time = time.time()
completion = client.chat.completions.create(
model="", 
messages=[
{
"role": "user",
"content": combined_questions
},
],
)
end_time=time.time()
elapsed_time=end_time - start_time
# print(completion.model_dump_json(indent=2))
response_text = completion.choices[0].message.content
print(f"Question:{combined_questions}\n")
print(f"Answer:{response_text}\n")
print(f"\nTime taken to get the response: {elapsed_time:.2f} seconds\n")
print("\n###################################################################################################################################\n")