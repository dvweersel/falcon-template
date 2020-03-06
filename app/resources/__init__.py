from .APIStatus import APIStatus


def register_routes(api):
    api.add_route('/health', APIStatus())