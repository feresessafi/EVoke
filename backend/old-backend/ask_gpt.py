import json
from openai import AzureOpenAI

API_KEY = ""
API_ENDPOINT_GPT4 = "https://hackatum-2024.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"

client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=API_ENDPOINT_GPT4,
    api_version="2024-08-01-preview"
    )

# load articles.json
with open("articles.json", "r") as f:
    articles = json.load(f)
    
    
article_texts = [article["article_text"] for article in articles.values()]
prompt_text = f"Without using the same wording for the headlines or repetitive content, generate a new article in English based on the following combined information from the articles: {' '.join(article_texts)}"
prompt2system = "You are an expert article writer with extensive experience at top news outlets like The New York Times, FAZ, and other leading publications in the fields of automotive, sustainability, and technology. Your role is to create original, engaging, and well-researched articles based on the provided information, combining insights from multiple sources in a way that enhances the message while remaining truthful and ethical. You are tasked with writing an article that is fresh, creative, and compelling, without directly copying any content from the sources provided."
prompt2user = f"Here is the latest information. Please create a completely new, original article based on the facts provided, using your own words and ideas. Do not reuse headlines or specific phrases from the source articles: {' '.join(article_texts)}"

# prompt3user = f"Here is the latest information. Please create a completely new 3, original articles based on the 3 main headlines, using your own words and ideas. Do not reuse headlines or specific phrases from the source articles and separate each article in a json format where there's title and text pair: {' '.join(article_texts)}"
# response = client.chat.completions.create(
#     model="gpt-4",  # Ensure correct model identifier
#     messages=[
#         {"role": "system", "content": prompt2system},
#         {"role": "user", "content": prompt2user}
#     ],
#     max_tokens=1000,
#     temperature=0.5
# )

generated_articles = []

for i in range(3):
    prompt2user = f"Here is the latest information. Please create a completely new, original article based on the facts provided, using your own words and ideas. Do not reuse headlines or specific phrases from the source articles: {article_texts[i]}"

    # Request to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",  # Ensure you're using the correct model
        messages=[
            {"role": "system", "content": prompt2system},
            {"role": "user", "content": prompt2user}
        ],
        max_tokens=1000,
        temperature=0.5
    )

    generated_title = client.chat.completions.create(
        model="gpt-4o",  # Ensure you're using the correct model
        messages=[
            {"role": "system", "content": "You are an expert headline writer with extensive experience at top news outlets like The New York Times, FAZ, and other leading publications in the fields of automotive, sustainability, and technology. Your role is to create original, engaging, and well-researched headlines based on the provided information, combining insights from multiple sources in a way that enhances the message while remaining truthful and ethical. You are tasked with writing a headline that is fresh, creative, and compelling, without directly copying any content from the sources provided."},
            {"role": "user", "content": f"Create a headline for the article based on the facts provided: {response.choices[0].message.content} and don't write for the same thing as previous articles from here {generated_articles}"}
        ],
        max_tokens=50,
        temperature=0.5    
    )
    
    # Collect the generated article
    generated_articles.append({
        "title": f"{generated_title.choices[0].message.content}",  # You can modify to dynamically get titles if needed
        "text": response.choices[0].message.content  # Assuming 'choices' contains the generated text
    })

# print(response.choices[0].message.content)
print(generated_articles)

# response = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant."
#         },
#         {
#             "role": "user",
#             "content": "What is the capital of the United States?"
#         }
#     ]
# )
# print(response.choi)