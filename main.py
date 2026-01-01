from libs.engine import Engine
from libs.gemini import GeminiLLM
from libs.tistory_parser import TistoryContentParser

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

import datetime

f = open(f"./{datetime.datetime.now()}.md", "a")
f.write(result.text)
f.close()
