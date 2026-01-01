import os

import google.generativeai as genai
from dotenv import load_dotenv

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
        _template = f"""
            아래 내용을 순수 Markdown(.md) 형식으로 변환해주세요
            -----
            {content}
            -----
            출력 결과를 그대로 복사하여 `.md` 파일로 저장할 예정입니다.
            ❗ 절대 규칙 (위반 시 실패):
                - 출력은 Markdown 문서 본문만 포함한다    
                - 설명, 머리말, 꼬리말, 안내 문장 절대 금지        
                - "다음은", "아래는", "번역", "설명", "결과" 같은 문구 절대 사용 금지        
                - Markdown 이외의 형식(JSON, HTML, 일반 텍스트 설명) 절대 출력 금지

            ❗️중요 규칙 (반드시 지킬 것):
                📐 Markdown 규칙:
                    1. 문서 제목은 최상단에 `#` 사용
                    2. 섹션은 `##`, `###`으로만 계층화
                    3. 목록은 `-` 또는 `1.` 형식만 사용
                    4. 코드, 명령어, 파일 경로는 반드시 백틱(`) 또는 ``` 코드 블록 사용
                    5. 표가 적합한 경우 Markdown 테이블 문법 사용
                    6. 원문의 순서와 의미를 변경하지 말 것
                    7. 요약, 해설, 해석, 의견 추가 금지
            """
        response = self.model()
        return response.generate_content(_template)
