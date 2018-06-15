from flask import *
import bs4 as bs
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return get_page()

@app.route('/<string:data>')
def query(data):
    data = request.query_string
    if str(data)[2:4] == 'ie':
        return get_query(data)
    elif str(data)[2:3]:
        return get_site(data)

def get_page():
    content = requests.get('https://www.google.com')
    return content.text

def get_query(data):
    url = 'https://www.google.com/search?' + str(data)[2:len(str(data)) - 1]
    data = requests.get(url)
    return data.text

def get_site(data):
    data = str(data)[4:].split('&sa')[0]
    return redirect(data)

if __name__ == '__main__':
    app.run(debug=True)