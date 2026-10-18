"""Serve dist under the exact GitHub Pages project path. Python 3.10+."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit
import os
os.chdir(Path(__file__).resolve().parent/'dist')
class Handler(SimpleHTTPRequestHandler):
 def do_GET(self):
  if self.path=='/':
   self.send_response(302);self.send_header('Location','/zero.github.io/');self.end_headers();return
  if self.path.startswith('/zero.github.io/'):
   self.path=self.path[len('/zero.github.io'):];return super().do_GET()
  self.send_error(404)
print('Preview: http://127.0.0.1:8000/zero.github.io/',flush=True)
ThreadingHTTPServer(('127.0.0.1',8000),Handler).serve_forever()
