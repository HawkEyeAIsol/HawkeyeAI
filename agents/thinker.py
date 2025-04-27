import openai

class ThinkerAgent:
    """Agent that generates creative ideas based on a given topic."""
    
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_idea(self, topic: str) -> str:
        prompt = f"Generate a futuristic and innovative idea about: {topic}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating idea: {str(e)}"
