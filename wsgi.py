from flask import Flask, render_template

app = Flask(__name__)


def get_films():
    return [
        {
            'id': 1,
            'name': 'Harry Potter and the Philosopher\'s Stone',
            'relise_date': '2001-11-16'
        },
        {
            'id': 2,
            'name': 'Harry Potter and the Chamber of Secrets',
            'relise_date': '2002-11-16'
        }
    ]

    @app.route('/')
    def index():
        def get_films():
            return [
                {
                    'id': 1,
                    'name': 'Harry Potter and the Philosopher\'s Stone',
                    'relise_date': '2001-11-16'
                },
                {
                    'id': 2,
                    'name': 'Harry Potter and the Chamber of Secrets',
                    'relise_date': '2002-11-16'
                }
            ]

        return render_template('index.html', films=get_films())

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/<string:name>')
    def greating(name):
        return f'<h1>Hello, {name.capitalize()}</h1>'

    if __name__ == '__main__':
        app.run()
