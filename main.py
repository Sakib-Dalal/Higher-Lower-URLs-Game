from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Guess a number between 0 to 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

random_number = random.randint(a=0, b=9)

@app.route('/<int:num>')
def random_site(num):
    if num < random_number:
        return '''<h1 style="color: red"> Too low, try again!</h1>
                <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExanFrc2FsODA2bnc5MDY5NDFzMWh4djQ2NWIzcTM3NXA4eXJpeGQzZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xjTIBA4gjvXIQ/giphy.gif">'''

    elif num > random_number:
        return '''<h1 style="color: blue"> Too high, try again! </h1>
                <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDV5OWJkNXBscWlyb3MxamRyZmFqMjlnZmpmdXM3d2wxZGZ4aGI0eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZtaO9BZHcOjmErm/giphy.gif">'''

    else:
        return '''<h1 style="color: green"> You Found Me!</h1>
                <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGg4aDJlODB2OWQyMmRoY25yYzRhMTV0NWd2anJtaGwwYjdiOW4xNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/21GCae4djDWtP5soiY/giphy.gif">'''


if __name__ == '__main__':
    app.run(debug=True)

