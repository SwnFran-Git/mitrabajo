from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from View.Menu_Principal_View import MenuPrincipalView
from Controller.AuthController import AuthController
from Exceptions.Exepciones import TiendaException


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("View/UI/frm_login.ui", self)

        self._auth_controller = AuthController()
        self.Btn_Login.clicked.connect(self._on_btn_ingresar_click)
    def _on_btn_ingresar_click(self):
        dni = self.txtdni.text()
        clave = self.txtclave.text()
        
        try:
            # 1. Autenticación exitosa
            usuario = self._auth_controller.IniciarSesion(dni, clave)
            # 2. Mensaje de bienvenida
            self.menu_principal = MenuPrincipalView(usuario)
            self.menu_principal.show()
            self.close()
        except TiendaException as ex:
            QMessageBox.warning(self, "Validación de Acceso", str(ex))
        except Exception as ex:
            # Captura de errores no previstos en Python
            QMessageBox.critical(self, "Error de Sistema", f"Ocurrió un error en la aplicación: {ex}")




        self.txtdni.clear()
        self.txtclave.clear()