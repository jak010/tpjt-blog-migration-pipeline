# Tistory 블로그 마이그레이션 파이프라인

이 프로젝트는 Tistory 블로그 게시물을 Markdown 형식으로 마이그레이션하기 위한 파이프라인입니다.
(최종적으로는 Obsidian으로 관리에 목표를 둡니다.)

특정 Tistory 게시물 URL에서 콘텐츠를 추출하고, Google Gemini LLM을 활용하여
이를 순수한 Markdown 형식으로 변환한 다음, 로컬 파일 시스템에 `.md` 파일로 저장합니다.

## 주요 기능

- **Tistory 게시물 파싱**: 주어진 Tistory 게시물 URL에서 HTML 소스를 가져와 게시물의 작성일과 본문 내용을 추출합니다.
- **콘텐츠 Markdown 변환**: 추출된 본문 내용을 Google Gemini LLM에 전달하여 Markdown 형식으로 변환합니다. 이 과정에서 Markdown 문서의 구조와 서식을 일관되게 유지하기 위한
  엄격한 규칙이 적용됩니다.
- **Markdown 파일 저장**: 변환된 Markdown 콘텐츠를 현재 날짜와 시간을 파일명으로 하는 `.md` 파일로 저장합니다.

## 프로젝트 구조

- `main.py`: 파이프라인의 진입점입니다. Tistory URL을 설정하고, `Engine`, `TistoryContentParser`, `GeminiLLM`을 사용하여 게시물을 처리하고 Markdown
  파일로 저장하는 전체 흐름을 제어합니다.
- `libs/`: 프로젝트의 핵심 로직을 포함하는 라이브러리 디렉토리입니다.
    - `libs/engine.py`: 웹 페이지의 HTML 소스를 가져오고 BeautifulSoup을 사용하여 파싱하는 역할을 합니다.
    - `libs/gemini.py`: Google Gemini API와 상호 작용하여 텍스트 콘텐츠를 Markdown 형식으로 변환하는 로직을 구현합니다. 변환 규칙을 정의하는 시스템 지침과 템플릿을
      포함합니다.
    - `libs/tistory_parser.py`: Tistory 게시물의 HTML에서 특정 콘텐츠(작성일, 본문 텍스트, 이미지 URL 등)를 추출하는 파서 로직을 구현합니다.

## 사용 방법

1. `requirements.txt`에 명시된 의존성을 설치합니다.
   ```bash
   pip install -r requirements.txt
   ```
2. Google Gemini API 키를 환경 변수 `GOOGLE_API`로 설정합니다. `.env` 파일을 생성하여 `GOOGLE_API=YOUR_API_KEY`와 같이 설정할 수 있습니다.
3. `main.py` 파일에서 마이그레이션하려는 Tistory 게시물의 URL을 `url` 변수에 설정합니다.
   ```python
   x = 482 # 게시물 번호
   url = f"https://jakpentest.tistory.com/{x}"
   ```
4. `main.py`를 실행합니다.
   ```bash
   python main.py
   ```
   실행이 완료되면 현재 디렉토리에 변환된 Markdown 파일이 생성됩니다.
