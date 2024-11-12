import pyto_ui as ui
import pathlib
import http.server
import socketserver
import threading
import os

# Set up the directory where the HTML and CSS files are located
os.chdir(pathlib.Path.joinpath(os.getcwd(), "/jb"))

# Define server port
PORT = 8000

# Set up and start the HTTP server in a separate thread
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

def start_server():
    httpd.serve_forever()

# Start server in a background thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Initialize WebView and load the URL from the HTTP server
web_view = ui.WebView()
web_view.load_url(f"http://localhost:{PORT}/index.html")

# Display the WebView in fullscreen mode
ui.show_view(web_view, mode=ui.PRESENTATION_MODE_FULLSCREEN)