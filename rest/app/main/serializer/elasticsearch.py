from flask import jsonify
from werkzeug.exceptions import NotFound

from app.main.vo import ElasticsearchDocVO


class ElasticsearchDocGetSerializer:

    @staticmethod
    def serialize(doc):
        try:
            item = doc['hits']['hits'][0]
        except IndexError:
            raise NotFound()

        res = {
            'id': item['_id'],
            'content': item['_source'][ElasticsearchDocVO.CONTENT]
        }

        return jsonify(res)


class ElasticsearchDocUpdateSerializer:

    @staticmethod
    def serialize(doc):
        res = {
            'id': doc['_id'],
            'result': doc['result']
        }

        return jsonify(res)


class ElasticsearchTransparentErrorSerializer:

    @staticmethod
    def serialize(e):
        res = {
            'code': e.status_code,
            'name': e.error,
            'description': e.info
        }

        return jsonify(res), e.status_code

