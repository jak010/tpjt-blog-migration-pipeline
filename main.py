from libs.engine import Engine
from libs.llm.gemini import GeminiLLM
from libs.tistory_parser import TistoryContentParser
from libs.export.template import MarkDownExportTemplate

x = 482
url = f"https://jakpentest.tistory.com/{x}"
print(url)

engine = Engine.initialize(url)

# Tistory Parser
content = TistoryContentParser(engine)
file_created_at = content.get_created_at()
file_content = content.get_content_source()


# content make
llm = GeminiLLM()
result = llm.execute('\n\n'.join(file_content))

# Markdown Export
exporter = MarkDownExportTemplate(
    file_name=content.get_title(),
    file_content=result.text
)
exporter.execute()
