from flask_restplus import Namespace, Resource

api = Namespace('simple', description='Simple example operations')


@api.route('/hello')
class HelloWorld2(Resource):
    def get(self):
        return {'hello': 'world 2.0'}


@api.route('/welcome')
class WelcomeWorld(Resource):
    def get(self):
        return {'welcome': 'world'}
