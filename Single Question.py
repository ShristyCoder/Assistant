import time
from openai import AzureOpenAI


client = AzureOpenAI(
    api_key="",
    api_version="2023-07-01-preview",
    azure_endpoint="",
    
)

start_time = time.time()

completion = client.chat.completions.create(
    model="", 
    messages=[
        {
            "role": "user",
            "content": "\nHow do I output all files in a directory using Python?\n",
        },
    ],
)

end_time=time.time()

elapsed_time=end_time - start_time

# print(completion.model_dump_json(indent=2))
print(completion.choices[0].message.content)

print(f"\nTime taken to get the response: {elapsed_time:.2f} seconds\n")


print("\n###################################################################################################################################\n")

start_time = time.time()

completion = client.chat.completions.create(
    model="", 
    messages=[
        {
            "role": "user",
            "content": "\nwhat is the future of AI?\n",
        },
    ],
)

end_time=time.time()

elapsed_time=end_time - start_time

# print(completion.model_dump_json(indent=2))
print(completion.choices[0].message.content)

print(f"\nTime taken to get the response: {elapsed_time:.2f} seconds\n")


print("\n###################################################################################################################################\n")

start_time = time.time()

completion = client.chat.completions.create(
    model="", 
    messages=[
        {
            "role": "user",
            "content": "\nwhat is the process of bill passing in Indian praliament?\n",
        },
    ],
)

end_time=time.time()

elapsed_time=end_time - start_time

# print(completion.model_dump_json(indent=2))
print(completion.choices[0].message.content)

print(f"\nTime taken to get the response: {elapsed_time:.2f} seconds\n")

print("\n###################################################################################################################################\n")




