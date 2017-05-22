from functools import wraps

from flask import request, jsonify

from app import redis_store


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'code': 0, 'message': '请先登录!'})
            # phone_number = redis_store.get('token:%s' % token)
            # return jsonify({'code': 1, 'message': 'success'})

    return decorated_function
