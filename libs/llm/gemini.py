import os

import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API"])


class GeminiLLM:

    def __init__(self):
        self.system_instruction = """
        당신은 전문 테크니컬 라이터입니다.
        """

    def model(self) -> genai.GenerativeModel:
        return genai.GenerativeModel(
            'gemini-2.5-flash',
            system_instruction=self.system_instruction,
            generation_config={"response_mime_type": "text/plain"}
        )

    def execute(self, content):
        with open("./libs/llm/_guide.txt", "r") as f:
            _template = f"""
                {f.read()}                
                -----
                {content}                        
                """

            response = self.model()

            try:
                return response.generate_content(_template)
            except ResourceExhausted as e:
                raise Exception(
                    "429 You exceeded your current quota, please check your plan and billing details. For more information on this error")
