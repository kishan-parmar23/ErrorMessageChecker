from google import genai
import temp.constants as constants 


client = genai.Client(api_key=constants.User_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash-lite", 
    contents="Explain how AI works in a few words"
)
print(response.text)