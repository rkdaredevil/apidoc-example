import random
import uuid

import bottle

app = bottle.app()


@app.hook('after_request')
def enable_cors():
    """
    Set CORS headers.
    You may not want to use the wildcard '*' for Access-Control-Allow-Origin
    in production.
    """
    headers = bottle.response.headers
    headers['Access-Control-Allow-Origin'] = '*'
    headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET'
    headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type'


@app.route('/api/v1/random/', method=['OPTIONS', 'GET'])
def get_random_number():
    """
    @api {GET} /v1/random/ Generate a random number
    @apiName GetRandomNumber
    @apiGroup Random

    @apiDescription Generates a random number in the range `[0.0, 1.0)`.

    @apiSuccess (Success 200) {UUID}   request_id Unique id for the request
    @apiSuccess (Success 200) {Number} results    Random number in `[0.0, 1.0)`

    @apiSampleRequest /v1/random/

    @apiExample cURL example
    $ curl https://apidoc-example.herokuapp.com/api/v1/random/

    @apiSuccessExample {js} Success-Response:
        HTTP/1.0 200 OK
        {
            "request_id": "ad506913-a073-4d23-9f95-388d1c1e2c46",
            "result": 0.3606252123151169
        }
    """
    if bottle.request == 'OPTIONS':
        return {}

    return {
        'request_id': str(uuid.uuid4()),
        'result': random.random(),
    }
