from datetime import datetime

import feedparser


class TistoryRSSChecker:

    def __init__(self):
        self.rss_url = "https://jakpentest.tistory.com/rss"

    def get_laste_post_index(self) -> int:
        result = self.parse_rss()
        return int(result[:1][0].get("guid").split("/")[-1])

    def parse_rss(self, depth=1) -> list[dict]:
        feed = feedparser.parse(self.rss_url)

        if feed.bozo:
            raise ValueError(f"RSS 파싱 실패: {feed.bozo_exception}")

        results = []

        for entry in feed.entries[:depth]:
            item = {
                "title": entry.get("title"),
                "link": entry.get("link"),
                "summary": entry.get("summary"),
                "published": (datetime(*entry.published_parsed[:6]) if entry.get("published_parsed") else None),
                "author": entry.get("author"),
                "guid": entry.get("guid"),
            }
            results.append(item)

        return results
