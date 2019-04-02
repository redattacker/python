import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello babyq!')


if __name__=='__main__':
    print("look at: http://localhost:8000")
    app=tornado.web.Application([
        (r'/',IndexHandler),
    ])

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(8000)
    http_server.start(0)
    tornado.ioloop.IOLoop.current().start()