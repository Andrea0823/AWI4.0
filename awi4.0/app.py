import web

urls = (
    '/', 'Index',
    '/bienvenida', 'Bienvenida'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Bienvenida:
    def GET(self):
        return render.bienvenida()

#Formulario
import web

urls = (
    '/', 'Index',

)
app = web.application(urls, globals())
render = web.template.render('templetes')
class Index:
    def GET(self):
        return render.formulario()

    def POST(self):
        form = web.input()
        print(type(form))
        return form["nombre"]


if __name__ == "__main__":
    app.run()