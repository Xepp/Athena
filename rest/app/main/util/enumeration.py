from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class SentimentType(BaseEnum):

    POS = 'pos'
    NEU = 'neu'
    NEG = 'neg'
    UNK = 'unk'

