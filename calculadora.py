import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import math
import os

class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()

        uic.loadUi("calculadora_ui.ui",self)
        self.setWindowTitle("Calculadora")

        os.path.join(os.path.dirname(__file__), "calculadora_ui.ui")
        os.path.join(os.path.dirname(__file__), "icono_calculadora.png")
        
        self.operacion = []
        self.resultado_calculado = False

        self.configurar()
        self.listadatos = []

        self.bt_cero.clicked.connect(lambda: self.insertar_num("0"))
        self.bt_uno.clicked.connect(lambda: self.insertar_num("1"))
        self.bt_dos.clicked.connect(lambda: self.insertar_num("2"))
        self.bt_tres.clicked.connect(lambda: self.insertar_num("3"))
        self.bt_cuatro.clicked.connect(lambda: self.insertar_num("4"))
        self.bt_cinco.clicked.connect(lambda: self.insertar_num("5"))
        self.bt_seis.clicked.connect(lambda: self.insertar_num("6"))
        self.bt_siete.clicked.connect(lambda: self.insertar_num("7"))
        self.bt_ocho.clicked.connect(lambda: self.insertar_num("8"))
        self.bt_nueve.clicked.connect(lambda: self.insertar_num("9"))

        self.bt_num_entero.clicked.connect(self.cambiar_entero)
        self.bt_coma.clicked.connect(self.insertar_coma)
        self.bt_parentesis_izq.clicked.connect(self.parentesis_izq)
        self.bt_parentesis_der.clicked.connect(self.parentesis_der)

        self.bt_sumar.clicked.connect(lambda: self.insertar_operador("+"))
        self.bt_restar.clicked.connect(lambda: self.insertar_operador("-"))
        self.bt_multiplicar.clicked.connect(lambda: self.insertar_operador("*"))
        self.bt_dividir.clicked.connect(lambda: self.insertar_operador("/"))

        self.bt_pi.clicked.connect(self.num_pi)
        self.bt_rand.clicked.connect(self.radianes)
        self.bt_log.clicked.connect(self.log_base10)
        self.bt_coseno.clicked.connect(self.coseno)
        self.bt_porcentaje.clicked.connect(self.porcentaje)
        self.bt_exponencial.clicked.connect(self.exponencial)
        self.bt_raiz_cuadrada.clicked.connect(self.raiz_cuadrada)

        self.bt_igual.clicked.connect(self.resultado)

        self.bt_borrar.clicked.connect(self.borrar)
        self.bt_reiniciar.clicked.connect(self.reiniciar)

        self.bt_historial.clicked.connect(self.borrar_historial)

        # Inicializar display con "0"
        self.display.setText("0")

    def insertar_num(self, num: str):
        if self.resultado_calculado:
            self.operacion = [num]  # Reiniciar la operación con "0"
            self.resultado_calculado = False
        else:
            if self.display.text() == "0":
                self.operacion.append(num)
            else:
                self.operacion.append(num)
        self.actualizar_display()

    def insertar_coma(self):
        if self.operacion[-1].count(".") < 1:
            self.resultado_calculado = False
            self.operacion[-1] += "."
            self.actualizar_display()

    def parentesis_izq(self):
        if self.resultado_calculado:
            self.operacion = ["("]
            self.resultado_calculado = False
        else:
            if self.display.text() == "0":
                self.operacion.append("(")
            else:
                self.operacion.append("(")
        self.actualizar_display()

    def parentesis_der(self):
        if self.resultado_calculado:
            self.operacion = [")"]
            self.resultado_calculado = False
        else:
            if self.display.text() == "0":
                self.operacion.append(")")
            else:
                self.operacion.append(")")
        self.actualizar_display()

    def insertar_operador(self, operador: str):
        self.resultado_calculado = False
        self.operacion.append(operador)
        self.actualizar_display()

    def porcentaje(self):
        if self.operacion:
            operacion_str = "".join(self.operacion)
            resultado = str(float(operacion_str) * 0.01)
            self.operacion =[resultado]
            self.listadatos.append((f"{operacion_str}*1%", resultado))
            self.agregar_datos()
            self.actualizar_display()

    def exponencial(self):
        if self.operacion:
            operacion_str = "".join(self.operacion)
            self.operacion.append("*" + operacion_str)
            self.agregar_datos()
            self.resultado()

    def raiz_cuadrada(self):
        if self.operacion:
            # Convertimos la operación en un número
            numero = float("".join(self.operacion))
            
            # La raíz cuadrada solo se calcula para números no negativos
            if numero < 0:
                self.operacion = ["Error"]
            else:
                resultado = str(math.sqrt(numero))  # Calculamos la raíz cuadrada
                self.operacion = [resultado]  # Reemplazamos la operación con el resultado
                self.listadatos.append((f"√{numero}", resultado))
                self.agregar_datos()
            self.resultado_calculado = True
            self.actualizar_display()

    def num_pi(self):
        if self.resultado_calculado:
            self.operacion = ["3.14159"]  # Reiniciar la operación con pi
            self.resultado_calculado = False
        else:
            if self.display.text() == "0":
                self.operacion.append("3.14159")
            else:
                self.operacion.append("3.14159")
        self.actualizar_display()

    def radianes(self):
        if self.operacion:
            # Convertimos la operación en un número
            numero = float("".join(self.operacion))
            
            resultado = math.radians(numero)  # Calculamos lso radianes de los grados introducidos
            formateado = "{:.5f}".format(resultado)  # Limitamos los decimales a 5
            
            self.operacion = [str(formateado)]
            self.listadatos.append((f"{numero}°", f"{formateado} rad"))
            self.agregar_datos()
        self.resultado_calculado = True
        self.actualizar_display()

    def coseno(self):
        if self.operacion:
            # Convertimos la operación en un número
            numero = float("".join(self.operacion))
            
            radianes = math.radians(numero) # Pasamos los grados introducidos a radianes
            coseno = math.cos(radianes)  # Con los radianes calculamos el coseno

            formateado = "{:.5f}".format(coseno)
            self.operacion = [str(formateado)]
            self.listadatos.append((f"{numero}°", f"{formateado}"))
            self.agregar_datos()
        self.resultado_calculado = True
        self.actualizar_display()

    def log_base10(self):
        if self.operacion:
            # Convertimos la operación en un número
            numero = float("".join(self.operacion))
            
            resultado = math.log10(numero)  # Calcula el logarítmo en base 10
            formateado = "{:.5f}".format(resultado)
            self.operacion = [str(formateado)]
            self.listadatos.append((f"log_10({numero})", f"{formateado}"))
            self.agregar_datos()
        self.resultado_calculado = True
        self.actualizar_display()

    def reiniciar(self):
        self.operacion.clear()
        self.display.setText("0")

    def borrar(self):
        if self.operacion:  # Si hay algo en la lista
            self.operacion.pop() # Elimina el último elemento
            self.actualizar_display()  
        if not self.operacion:  # Si la lista está vacía después de borrar
            self.display.setText("0")  # Vuelve a poner "0" como valor predeterminado

    def cambiar_entero(self):
        if self.operacion: 
            self.operacion[-1] = str(-int(self.operacion[-1]))
            self.actualizar_display()
        
    def actualizar_display(self):
        self.display.setText("".join(self.operacion))  # Actualizar la caja de texto con la operación actual

    def resultado(self):
        try:
            # Unir todos los elementos de la lista y evaluar la operación
            operacion_str = "".join(self.operacion)
            resultado = eval(operacion_str)  # Evaluar la operación matemática
            self.operacion = [str(resultado)] # Mostrar solo el resultado en la operación
            self.resultado_calculado = True
            self.listadatos.append((operacion_str, str(resultado)))
            self.agregar_datos()
        except Exception as e:
            self.operacion = ["Error"]  # Si hay error en la operación, mostrar "Error"
            self.resultado_calculado = True
        self.actualizar_display()

    
    def configurar(self):
        self.TW_table.setColumnCount(2)
        self.TW_table.setHorizontalHeaderLabels(('Operación', 'Resultado'))
        

    def agregar_datos(self):
        self.TW_table.setRowCount(0)
        fila = 0
        row = 1
        for tupla in self.listadatos:
            self.TW_table.setRowCount(row)
            columna = 0 
            for valor in tupla: 
                item = QTableWidgetItem(valor) 
                self.TW_table.setItem(fila, columna, item)
                columna += 1 
            row += 1
            fila += 1

    def borrar_historial(self):
        self.listadatos.clear()
        self.TW_table.setRowCount(0)
        
def main():
    # se crea la instancia de la aplicación
    app = QApplication(sys.argv)
        # se crea la instancia de la ventana
    window = Ventana()
        # se muestra la ventana 
    window.show()
        # se entrega el control al sistema operativo
    app.exec() 

if __name__ == '__main__':
    main() 