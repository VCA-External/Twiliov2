from app import app
# from flask_compress import Compress
from gevent.pywsgi import WSGIServer
from gevent import monkey
# COMPRESS_MIMETYPES = ['application/json']
# COMPRESS_LEVEL = 7
# Compress(app)
# monkey.patch_all()
if __name__ == "__main__":
    # app.run(debug=True, threaded=True)
    http = WSGIServer(('', 5000), app.wsgi_app)  # for production
    http.serve_forever()
    # http.serve()  # for production
