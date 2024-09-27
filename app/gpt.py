import json
from yandex_cloud_ml_sdk import YCloudML
from app.config import settings


class GPTClient:
    def __init__(self):
        self.sdk = YCloudML(folder_id=settings.FOLDER_ID, auth=settings.YANDEX_API_KEY)
        self.model = self.sdk.models.completions("yandexgpt").configure(temperature=0.5)
        self.context = settings.LLM_CONTEXT

    def generate_response(self, question):
        try:
            full_prompt = f"{self.context}\nВопрос: {question}"
            result = self.model.run(full_prompt)

            if result.alternatives:
                response_text = result.alternatives[0].text.replace("\\n", "\n")
                print(response_text)
                return response_text
            else:
                return "Нет доступных альтернатив."
        except Exception as e:
            return f"Ошибка при работе с GPT: {e}"


gpt_client = GPTClient()
