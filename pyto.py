import pyto_ui as ui
import http.server
import socketserver
import threading
import os

# Define the server port
PORT = 8001

# Set up and start the HTTP server in a separate thread
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)

def start_server():
    print(f"Serving at http://0.0.0.0:{PORT}")
    httpd.serve_forever()

# Start the server in a background thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Initialize WebView and load the URL from the HTTP server
web_view = ui.WebView()
web_view.load_url(f"http://localhost:{PORT}/index.html")

# Display the WebView in fullscreen mode
ui.show_view(web_view, mode=ui.PRESENTATION_MODE_FULLSCREEN)
