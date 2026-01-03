# from libs.llm.gemini import GeminiLLM
from libs.tistory_checker import TistoryRSSChecker
from storage.dao import FileDao

# from libs.export.template import MarkDownExportTemplate

# engine = Engine.initialize(url)

# Tistory Parser
# content = TistoryContentParser(engine)
c = TistoryRSSChecker()
file_dao = FileDao()


# file_created_at = content.get_created_at()
# file_content = content.get_content_source()

# # content make
# llm = GeminiLLM()
# result = llm.execute('\n\n'.join(file_content))
#
# # Markdown Export
# exporter = MarkDownExportTemplate(
#     file_name=content.get_title(),
#     file_content=result.text
# )
# exporter.execute()
