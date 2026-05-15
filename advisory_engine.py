from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_advisory(data):

    prompt = f"""
    Crop: {data.crop}
    Temperature: {data.temperature}
    Humidity: {data.humidity}

    Give short farming advice.
    """

    try:

        response = client.models.generate_content(
            model="models/gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"API Error: {e}"