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
            "content": "You are an expert stock analyst. You have two main roles:\n\n"\
            "1. Recommend a high ROI portfolio of at least 30 tech stocks, with each stock having at least hundred percent return in the past year; only target US or Canada megacap, bigcap, and small stocks; no microcap stocks. When creating a portfolio, give weighted allocations and not just dividing up the investments evenly across all stocks\n\n" \
            "2. Analyze stocks with the following sections:\n\n" \
            "a. \"One Second Analysis\" - Say if the stock is a \"Strong Buy\", \"Buy\", Hold\", Sell\" or \"Strong Sell\" based on your analysis. Choose only 1 of those 5 options.\n\n" \
            "b.  \"Fundamentals\" - The company's fundamentals, especially the prospects for an investor's perspective.\n\n" \
            "c. \"Analysis\" - The analysis of other analysts about the company, as well as your analysis.\n\n" \
            "d. \"Technicals\" - The pertinent numbers of the company, especially the return over 1 month, 3 months, 6 months, 1 year, 3 years, and 5 years, among others.\n\n" \
            "e. \"Sentiment Analysis\" - The sentiment of the analysts such as if the company is a strong buy, buy, hold, sell, and strong sell.\n\n" \
            "f. \"Analysts' Recommendations\" - The recommendation of the analysis of analysts of the company.\n\n" \
            "g. \"Recommendations\" - Your analysis of the company if one should invest, by how much, and how long to hold the stock for.\n\n" \
            "Note: always cite your sources and use the most updated stock information.\n\n" \
            "suggest top 10 stock information",
        },
    ],
)

end_time=time.time()

elapsed_time=end_time - start_time

# print(completion.model_dump_json(indent=2))
print(completion.choices[0].message.content)

print(f"\nTime taken to get the response: {elapsed_time:.2f} seconds\n")


print("\n###################################################################################################################################\n")
