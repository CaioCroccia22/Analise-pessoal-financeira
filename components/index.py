from app import app
from components.sidebar import layout

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)