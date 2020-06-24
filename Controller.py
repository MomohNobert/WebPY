import web

urls = (
    '/', 'home'
)

render = web.template.render("Views/Templates", base="MainLayout")


# Classes/Routes
class home:
    def GET(self):
        return render.Home()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
