
class Middleware:
    def __init__(self, application, surname):
        self.app = application
        self.surname = surname

    def __call__(self, environ, start_response):
        environ = self.add_surname(environ)
        res = self.app(environ, start_response)
        return self.change_data(environ, res)

    def add_surname(self, environ):
        environ['SURNAME'] = self.surname
        return environ

    @staticmethod
    def change_data(environ, res):
        res = res[0].decode('utf-8')
        res = res.lower()
        temp = environ['SURNAME'].lower()
        res = res.replace(temp, temp.capitalize())
        res = f"{res[0].upper()}{res[1:]}"
        return [res.encode('utf-8')]
