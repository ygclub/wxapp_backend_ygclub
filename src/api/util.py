# -*- coding: utf-8 -*-

import json
import flask

from functools import wraps

def api(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
        except BaseException as e:
            value = {
                "status": "failed",
                "error": "Unkonwn error!"
            }
            flask.current_app.logger.error("Unkonwn error: %s" % str(e))
            flask.current_app.logger.exception(e)

        status = 200
        mimetype = 'application/json'
        content = json.dumps(value)
        callback = flask.request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + content + ')'
            mimetype = 'application/javascript'

        return flask.current_app.response_class(content, status=status, mimetype=mimetype)
    return decorated_function
