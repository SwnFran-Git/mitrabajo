import sys
from PyQt6.QtWidgets import QApplication
from View.Login_View import LoginView

app = QApplication(sys.argv)

ventana = LoginView()
ventana.show()

sys.exit(app.exec())