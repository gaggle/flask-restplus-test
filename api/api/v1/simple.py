from flask_restplus import Namespace, Resource

api = Namespace('simple', description='Simple example operations')


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/goodbye')
class GoodbyeWorld(Resource):
    def get(self):
        return {'goodbye': 'world'}
