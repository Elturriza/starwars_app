import os
from app import create_app

port = int(os.environ['PORT'])

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=port)