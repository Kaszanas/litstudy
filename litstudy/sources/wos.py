from litstudy.types import Document, DocumentSet, DocumentIdentifier, Author


class WoSAuthor:
    def __init__(self, entry):
        self.entry = entry


class WoSDocument(Document):
    def __init__(self) -> None:
        pass


def search_wos() -> DocumentSet:
    pass
