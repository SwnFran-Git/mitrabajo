class TiendaException (Exception):
    pass

class CredencialesIncorrectas(TiendaException):
    def __init__(
            self, mensaje: str = "Correo o contraseña de acceso incorrectos."):
        super().__init__(mensaje)

class UsuarioInactivo(TiendaException):
    def __init__(
        self , mensaje:str = ("Su cuenta esta Desactivada Contacte Con el administrador"
        )):
        super().__init__(mensaje)


class DniInvalidoError(TiendaException):
    def __init__(
        self , mensaje:str = ("Dni Debe tener 8 Caracteres Numericos"
        )):
        super().__init__(mensaje)

class PasswordError(TiendaException):
        def __init__(
        self , mensaje:str = ("La Contraseña Debe tener una logitud de 12 Caracteres entre letras numeros y caracteres especiales"
        )):
            super().__init__(mensaje)

class FormatoError(TiendaException):

    pass