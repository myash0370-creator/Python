from gemini_test import genai

client = genai.Client(api_key="YOU API KEY")

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Hello bhai kaise ho?"
)

print(response.text)