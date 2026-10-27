from ConexionDb.ConexionDb import ConexionDb
from Models.Entities.Empleado import Empleado


class UsuarioModel:

    @staticmethod
    def autenticar(dni: str, clave: str) -> Empleado | None:

        resultados = ConexionDb.ejecutar_sp_resultado(
            "sp_autenticar_usuario",
            [dni, clave]
        )

        if not resultados:
            return None

        fila = resultados[0]

        nombre_rol = str(fila.get("rol") or "").strip().upper()

        if nombre_rol in ("ADMINISTRADOR", "CAJERO"):
            empleado = Empleado(
                identificacion=fila["dni"],
                nombres=fila["nombres"],
                apellidos=fila["apellidos"],
                telefono=fila.get("telefono"),
                correo=fila.get("correo"),
                rol=nombre_rol,
                activo=bool(fila["es_activo"])
            )

            return empleado

        return None