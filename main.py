import http.server
import socketserver
import threading
import os

# Define the directory where the HTML and CSS files are located
current_directory = os.getcwd()
target_directory = os.path.join(current_directory, "jb")

# Change to the target directory if it exists
if os.path.isdir(target_directory):
    print(f"Serving files from: {target_directory}")
else:
    print(f"Directory '{target_directory}' does not exist. Please check the path.")
    exit(1)

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

# Keep the main thread alive to keep the server running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nShutting down server.")
    httpd.shutdown()