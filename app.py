from flask import Flask
import redis
import os

app = Flask(__name__)

# WHY: Connect to Redis using environment variable
# Not hardcoded — container name is used as hostname in Docker network
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=6379,
    decode_responses=True
)

@app.route('/')
def home():
    # WHY: Increment visit counter every time page loads
    visits = redis_client.incr('visits')
    return f'''
    <h1>Hello from Docker!</h1>
    <p>This app is running inside a container.</p>
    <p>Built by Rishitha — DevOps Engineer in training.</p>
    <p><strong>This page has been visited {visits} times.</strong></p>
    '''

@app.route('/status')
def status():
    visits = redis_client.get('visits') or 0
    return {
        'status': 'running',
        'engineer': 'Rishitha',
        'total_visits': visits
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
