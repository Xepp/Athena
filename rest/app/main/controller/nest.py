from flask import Blueprint
from flask import request

from app.main.service import ElasticsearchService
from app.main.serializer import ElasticsearchDocCreateSerializer
from app.main.util.decorator import validate_input


nest_blueprint = Blueprint('nest', __name__)


@nest_blueprint.route('/', methods=['POST'])
@validate_input
def create_doc():
    payload = request.get_json()

    elastic_id = payload['id']
    content = payload['content']
    source = payload['source']
    sentiment = payload.get('sentiment', None)

    doc = ElasticsearchService().create_doc(
        index='athena',
        elastic_id=elastic_id,
        content=content,
        source=source,
        sentiment=sentiment
    )

    res = ElasticsearchDocCreateSerializer().serialize(doc)

    return res, 201

