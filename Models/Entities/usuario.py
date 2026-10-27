class Usuario:
    def __init__(self, identificacion , activo):
        self.__dni = identificacion
        self._es_activo = activo

    @property
    def identificacion(self) -> str:
        return self.__dni
    @property
    def activo(self) -> bool:
        return self._es_activo
