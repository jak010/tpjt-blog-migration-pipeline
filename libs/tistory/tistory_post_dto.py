from dataclasses import dataclass


@dataclass()
class TistoryPostDTO:
    title: str
    created_at: str
    content: str
    post_number: int
