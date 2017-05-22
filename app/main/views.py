from app import redis_store
from . import main


@main.route('/')
def index():
    return redis_store.__getitem__("a")
    # return "hello worlds!"
