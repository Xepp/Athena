import os
from datetime import datetime
from elasticsearch import Elasticsearch

from app.main.vo import ElasticsearchDocVO


class ElasticsearchAdapter:

    def __init__(self):
        self.es = Elasticsearch(
            [os.getenv('ELASTICSEARCH_NODE')]
        )

    def get_doc(self, index, query, size):
        body = {
            'query': query,
            'size': size
        }

        return self.es.search(
            index=index,
            body=body
        )

    def update_doc(self, index, elastic_id, doc):
        now = datetime.now()
        doc.update({
            ElasticsearchDocVO.UPDATED_AT: now
        })
        body = {
            'doc': doc
        }

        return self.es.update(
            index=index,
            id=elastic_id,
            body=body
        )

