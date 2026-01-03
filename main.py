# from libs.engine import Engine
# from libs.tistory_checker import TistoryRSSChecker
# from libs.tistory_parser import TistoryContentParser
# from storage.dao import FileDao

# from libs.export.template import MarkDownExportTemplate

# Tistory Parser
# c = TistoryRSSChecker()
#
# file_dao = FileDao()
# r = file_dao.get_accessable_post(depth=3)

# contents = [
#     TistoryContentParser(
#         Engine.initialize(
#             f"https://jakpentest.tistory.com/{post.get('id')}"
#         )
#     )
#     for post in r
# ]


# file_created_at = content.get_created_at()
# file_content = content.get_content_source()

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
