from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from ConexionDb.ConexionDb import ConexionDb
from PyQt6.QtWidgets import QTableWidgetItem
class MenuPrincipalView(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        uic.loadUi("View/UI/frm_Menu_Principal.ui", self)
        self.usuario = usuario
        self.btn_inicio.clicked.connect(self.mostrar_inicio)
        self.btn_ventas.clicked.connect(self.mostrar_ventas)
        self.btn_productos.clicked.connect(self.mostrar_productos)
        self.btn_clientes.clicked.connect(self.mostrar_clientes)
        self.btn_proveedores.clicked.connect(self.mostrar_proveedores)
        self.btn_compras.clicked.connect(self.mostrar_compras)
        self.btn_reportes.clicked.connect(self.mostrar_reportes)
        self.btn_usuarios.clicked.connect(self.mostrar_usuarios)
        self.Paginas.setCurrentWidget(self.Pagina_Inicio)
        self.btn_CerrarSesion.clicked.connect(self.cerrar_sesion)
        self.Paginas.setCurrentWidget(self.Pagina_Inicio)
#Dentro del panel Usuarios
        self.btn_Buscar.clicked.connect(self.buscar)

        self.lbl_bienvenido.setText(
            f"¡Hola!, {usuario.nombre_completo}!"
        )
    def mostrar_inicio(self):
        self.Paginas.setCurrentWidget(self.Pagina_Inicio)

    def mostrar_ventas(self):
        self.Paginas.setCurrentWidget(self.Pagina_Ventas)
    
    def mostrar_productos(self):
        self.Paginas.setCurrentWidget(self.Pagina_Productos)

    def mostrar_clientes(self):
        self.Paginas.setCurrentWidget(self.Pagina_Clientes)

    def mostrar_proveedores(self):
        self.Paginas.setCurrentWidget(self.Pagina_Proveedores)

    def mostrar_compras(self):
        self.Paginas.setCurrentWidget(self.Pagina_Compras)

    def mostrar_reportes(self):
        self.Paginas.setCurrentWidget(self.Pagina_Reportes)

    def mostrar_usuarios(self):
        self.Paginas.setCurrentWidget(self.Pagina_Usuarios)

    def cerrar_sesion(self):
        from View.Login_View import LoginView
        self.login = LoginView()
        self.login.show()
        self.close()

    def buscar(self):
        buscado = self.Line_Buscar.text().strip()
        resultados = ConexionDb.ejecutar_sp_resultado('Buscar_Empleado',(buscado,))
        self.tb_empleados.setRowCount(0)
        for empleado in resultados:
            fila = self.tb_empleados.rowCount()
            self.tb_empleados.insertRow(fila)
            self.tb_empleados.setItem(
                fila, 0, QTableWidgetItem(str(empleado["dni"])))
            self.tb_empleados.setItem(
                fila, 1, QTableWidgetItem(str(empleado["nombres"])))
            self.tb_empleados.setItem(
                fila, 2, QTableWidgetItem(str(empleado["apellidos"])))
            self.tb_empleados.setItem(
                fila, 3, QTableWidgetItem(str(empleado["telefono"])))
            self.tb_empleados.setItem(
                fila, 4, QTableWidgetItem(str(empleado["correo"])))
            self.tb_empleados.setItem(
                fila, 5, QTableWidgetItem(str(empleado["rol"])))
            self.tb_empleados.setItem(
                fila, 6, QTableWidgetItem(str(empleado["es_activo"])))