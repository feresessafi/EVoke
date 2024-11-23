from openai import AzureOpenAI

API_KEY = ""
API_ENDPOINT_GPT4 = "https://hackatum-2024.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"

client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=API_ENDPOINT_GPT4,
    api_version="2024-08-01-preview"
    )


response = client.chat.completions.create(
    model="gpt-4",  # Ensure you're using the correct model
    messages=[
        {"role": "system", "content": "You are an expert headline writer with extensive experience at top news outlets like The New York Times, FAZ, and other leading publications in the fields of automotive, sustainability, and technology. Your role is to create original, engaging, and well-researched headlines based on the provided information, combining insights from multiple sources in a way that enhances the message while remaining truthful and ethical. You are tasked with writing a headline that is fresh, creative, and compelling, without directly copying any content from the sources provided."},
        {"role": "user", "content": "Create a headline for the article based on the facts provided: The latest information on the automotive industry, sustainability, and technology."}
    ],
    max_tokens=50,
    temperature=0.5    
)