import openai

class PlannerAgent:
    """Agent that creates step-by-step plans based on an idea."""
    
    def __init__(self, api_key):
        openai.api_key = api_key

    def plan(self, idea: str) -> str:
        prompt = f"Create a detailed step-by-step action plan for the following idea:\n\n{idea}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating plan: {str(e)}"
