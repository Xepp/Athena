from app.main.adapter import ElasticsearchAdapter
from app.main.vo import ElasticsearchDocVO
from app.main.util.enumeration import SentimentType


class ElasticsearchService:

    def __init__(self):
        self.adapter = ElasticsearchAdapter()

    def get_random_sentiment_doc(self, index):
        query = {
            'function_score': {
                'query': {
                    'term': {
                        ElasticsearchDocVO.SENTIMENT: {
                            'value': SentimentType.UNK.value
                        }
                    }
                },
                'functions': [
                    {
                        'random_score': {
                            'field': '_seq_no'
                        }
                    }
                ]
            }
        }

        return self.adapter.get_doc(
            index=index,
            query=query,
            size=1
        )

    def update_sentiment_doc(self, index, elastic_id, sentiment):
        doc = {
            ElasticsearchDocVO.SENTIMENT: sentiment
        }

        return self.adapter.update_doc(
            index=index,
            elastic_id=elastic_id,
            doc=doc
        )

