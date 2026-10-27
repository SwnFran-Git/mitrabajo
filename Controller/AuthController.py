from Exceptions.Exepciones import (
    CredencialesIncorrectas,
    DniInvalidoError,
    UsuarioInactivo
)

from Controller.ValidacionCampos import texto_obligatorio
from Models.models import UsuarioModel
from Models.Entities.Empleado import Empleado


class AuthController:

    def IniciarSesion(self, dni: str, clave: str) -> Empleado:

        # 1. Validar campos obligatorios
        dni = texto_obligatorio(dni, "DNI")
        texto_obligatorio(clave, "Contraseña")

        # 2. Validar formato del DNI
        if len(dni) != 8 or not dni.isdigit():
            raise DniInvalidoError(
                "El DNI debe contener exactamente 8 dígitos numéricos"
            )

        # 3. Autenticar usuario
        empleado: Empleado | None = UsuarioModel.autenticar(dni, clave)

        # 4. Verificar credenciales
        if empleado is None:
            raise CredencialesIncorrectas(
                "Credenciales incorrectas. Verifique su acceso"
            )

        # 5. Verificar estado
        if not empleado.activo:
            raise UsuarioInactivo(
                "Cuenta desactivada. Contacte con el administrador"
            )

        # 6. Devolver empleado autenticado
        return empleado