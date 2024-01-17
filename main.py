from flask import Flask, request, jsonify
from pydantic import ValidationError

from logger_creator import LoggerCreator
from sample_request import SampleRequest

app = Flask(__name__)

logger = LoggerCreator().create()


@app.get('/ping')
def ping():
    logger.info('Ping received')
    return jsonify("Pong")


@app.route('/sample-route')
def get_sample_route():
    parameter1 = request.args.get('parameter1')

    try:
        sample_request = SampleRequest(parameter1=parameter1)
    except ValidationError as e:
        error_message = '; '.join(f'{e["loc"][0]}: {e["msg"]}' for e in e.errors())
        logger.info(error_message)

        return jsonify({"error": error_message}), 400

    logger.info(f"Do something with ...")

    return jsonify("Sample Response")


if __name__ == "__main__":
    app.run(port=6000, debug=True)
