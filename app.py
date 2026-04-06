from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hello from Docker!</h1>
    <p>This app is running inside a container.</p>
    <p>Built by Rishitha — DevOps Engineer in training.</p>
    '''

@app.route('/status')
def status():
    return {'status': 'running', 'engineer': 'Rishitha'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
