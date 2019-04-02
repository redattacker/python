import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello ithomer")


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    print("look at: http://localhost:8888")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
