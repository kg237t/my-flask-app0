from flask import Flask, send_from_directory, request
import webbrowser
import time
import threading

app = Flask(__name__)

# URLs to open
urls = ['https://www.youtube.com', 'https://www.google.com']

# Interval in seconds
interval = 6

# Control variable to stop the loop
running = False

def open_tabs():
    global running
    while running:
        for url in urls:
            webbrowser.open_new_tab(url)
            time.sleep(interval)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/start', methods=['POST'])
def start():
    global running
    if not running:
        running = True
        thread = threading.Thread(target=open_tabs)
        thread.start()
    return '', 204

@app.route('/stop', methods=['POST'])
def stop():
    global running
    running = False
    return '', 204

if __name__ == '__main__':
    app.run(port=5000, debug=True)
