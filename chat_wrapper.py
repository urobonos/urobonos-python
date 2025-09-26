from langchain.schema.language_model import BaseLanguageModel
import os
from google import genai

class GeminiChatModel(BaseLanguageModel):
    model_name: str = "gemini-2.5-flash"

    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY 환경 변수가 설정되어 있지 않습니다.")
        self.client = genai.Client(api_key=api_key)

    def _call(self, prompt: str, stop=None) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )
        return response.text
