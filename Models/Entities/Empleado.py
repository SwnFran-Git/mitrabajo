from Models.Entities.usuario import Usuario


class Empleado(Usuario):
    def __init__(self, identificacion: str, nombres: str, apellidos: str,
                 telefono: str | None, correo: str | None, rol: str,
                 activo: bool = True):
        super().__init__(identificacion, activo)
        self._nombres = nombres
        self._apellidos = apellidos
        self._telefono = telefono
        self._correo = correo
        self._rol = rol

    @property
    def nombre_completo(self) -> str:
        return f"{self._nombres} {self._apellidos}"

    @property
    def apellidos(self) -> str:
        return self._apellidos

    @property
    def telefono(self) -> str | None:
        return self._telefono

    @property
    def correo(self) -> str | None:
        return self._correo

    @property
    def rol(self) -> str:
        return self._rol

    @property
    def activo(self) -> bool:
        return self._es_activo