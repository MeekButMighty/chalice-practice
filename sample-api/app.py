from chalice import Chalice

app = Chalice(app_name='sample-api')


@app.route('/')
def index():
    return {'hello': 'Oliver'}


@app.route('/hello/{name}')
def hello_name(name):
#    '/hello/james' -> {"hello": "james"}
    return {'hello': name}
