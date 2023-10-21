import logging

from flask import Flask
from flask import request
import flask

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger("app")

app = Flask(__name__)


@app.route("/consumeTerraWebhook", methods=["POST"])
def consume_terra_webhook() -> flask.Response:
  # Note that you may wish to do signature verification here
  # however that is not covered by this recipe. See the
  # webhook signature verification recipe for more on that.
  body = request.get_json()
  _LOGGER.info(
    "Received webhook for user %s of type %s", 
    body.get("user", {}).get("user_id"),
    body["type"]
  )
  
  return flask.Response(status=200)


if __name__ == "__main__":
  app.run(host="localhost", port=8080)