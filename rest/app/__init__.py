import os
from flask import json
from werkzeug.exceptions import HTTPException
from elasticsearch.exceptions import TransportError

from app.main import create_app
from app.main.controller.sentiment import sentiment_blueprint
from app.main.serializer import ElasticsearchTransparentErrorSerializer


env = 'prod' if os.getenv('FLASK_ENV') == 'production' else 'dev'
app = create_app(env)


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description
    })
    response.content_type = 'application/json'

    return response


@app.errorhandler(TransportError)
def handle_transport_error(e):
    return ElasticsearchTransparentErrorSerializer().serialize(e)

app.register_blueprint(sentiment_blueprint, url_prefix='/api/sentiment')

