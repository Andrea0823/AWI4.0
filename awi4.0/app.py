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

#Numeros
import web

urls = (
    '/', 'Index',

)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.numeritos()

    def POST(self):
        form = web.input()
        a = form ["num1"]
        b = form["num2"]

        if(len(a)!=0 and len(b)!=0):
            if(a.isnumeric() and b.isnumeric()):
                opcion = form["sumita"]
                if(opcion=="sumar"):
                    sumita= int(a) + int(b)
                    opcion= sumita

                elif(opcion=="Restar"):
                    resta= int(a) - int(b)
                    opcion= resta

                elif(opcion=="Multiplicar"):
                    multiplicacion= int(a) * int(b)
                    opcion= multiplicacion

                elif(opcion=="Dividir"):
                    dividir= int(a) / int(b)
                    opcion= dividir
            else:
                opcion = "Inserta un numero"
        else:
            opcion ="No permite valores vacios"
        return opcion

if __name__ == "__main__":
    app.run()