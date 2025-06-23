import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_plan(self, goal: str):
        prompt = f"Break down this goal into an ordered list of steps:\nGoal: {goal}"
        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You're an AI planner that breaks user goals into steps."},
                {"role": "user", "content": prompt}
            ]
        )
        steps = response.choices[0].message.content.strip().split('\n')
        return [s.strip("-•1234567890. ") for s in steps if s]

    def summarize(self, context: str):
        prompt = f"Summarize the following information clearly:\n{context}"
        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You're a helpful summarizer."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
