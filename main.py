import web

web_urls = (
    '/', 'index'
)


class index:
    def GET(self):
        return("How are you today?")


if __name__ == "__main__":
    app = web.application(web_urls, globals())
    app.run()
