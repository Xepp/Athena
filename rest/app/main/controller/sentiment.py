from flask import Blueprint
from flask import request

from app.main.service import ElasticsearchService
from app.main.serializer import ElasticsearchDocGetSerializer
from app.main.serializer import ElasticsearchDocUpdateSerializer
from app.main.util.decorator import validate_input


sentiment_blueprint = Blueprint('sentiment', __name__)


@sentiment_blueprint.route('/random', methods=['GET'])
def get_random_doc():
    doc = ElasticsearchService().get_random_sentiment_doc(
        index='athena'
    )

    res = ElasticsearchDocGetSerializer().serialize(doc)

    return res, 200


@sentiment_blueprint.route('/', methods=['PATCH'])
@validate_input
def update_doc():
    payload = request.get_json()

    elastic_id = payload['id']
    sentiment = payload['sentiment']

    doc = ElasticsearchService().update_sentiment_doc(
        index='athena',
        elastic_id=elastic_id,
        sentiment=sentiment
    )

    res = ElasticsearchDocUpdateSerializer().serialize(doc)

    return res, 200

