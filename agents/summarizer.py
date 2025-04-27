import openai

class SummarizerAgent:
    """Agent that summarizes long texts into key points."""
    
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize(self, text: str) -> str:
        prompt = f"Summarize the following text into bullet points:\n\n{text}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error summarizing text: {str(e)}"
