# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(692, 460)
        palette = QPalette()
        brush = QBrush(QColor(85, 170, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        icon = QIcon()
        icon.addFile(u"icono_calculadora.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_dos = QPushButton(self.centralwidget)
        self.bt_dos.setObjectName(u"bt_dos")
        self.bt_dos.setGeometry(QRect(90, 330, 81, 51))
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(12)
        self.bt_dos.setFont(font1)
        self.bt_num_entero = QPushButton(self.centralwidget)
        self.bt_num_entero.setObjectName(u"bt_num_entero")
        self.bt_num_entero.setGeometry(QRect(10, 380, 81, 51))
        self.bt_num_entero.setFont(font1)
        self.bt_uno = QPushButton(self.centralwidget)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setGeometry(QRect(10, 330, 81, 51))
        self.bt_uno.setFont(font1)
        self.bt_cero = QPushButton(self.centralwidget)
        self.bt_cero.setObjectName(u"bt_cero")
        self.bt_cero.setGeometry(QRect(90, 380, 81, 51))
        self.bt_cero.setFont(font1)
        self.bt_coma = QPushButton(self.centralwidget)
        self.bt_coma.setObjectName(u"bt_coma")
        self.bt_coma.setGeometry(QRect(170, 380, 81, 51))
        self.bt_coma.setFont(font1)
        self.bt_igual = QPushButton(self.centralwidget)
        self.bt_igual.setObjectName(u"bt_igual")
        self.bt_igual.setGeometry(QRect(250, 380, 81, 51))
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(0, 170, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 135))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.bt_igual.setPalette(palette1)
        self.bt_igual.setFont(font1)
        self.bt_igual.setMouseTracking(True)
        self.bt_igual.setToolTipDuration(0)
        self.bt_igual.setStyleSheet(u"QPushButton#bt_igual {\n"
"    background-color: rgb(0, 170, 255);\n"
"	border-radius: 10px;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"   }\n"
"\n"
"QPushButton#bt_igual:hover {\n"
"    background-color: rgb(82, 186, 255);\n"
" }")
        self.bt_igual.setCheckable(False)
        self.bt_sumar = QPushButton(self.centralwidget)
        self.bt_sumar.setObjectName(u"bt_sumar")
        self.bt_sumar.setGeometry(QRect(250, 330, 81, 51))
        self.bt_sumar.setFont(font1)
        self.bt_tres = QPushButton(self.centralwidget)
        self.bt_tres.setObjectName(u"bt_tres")
        self.bt_tres.setGeometry(QRect(170, 330, 81, 51))
        self.bt_tres.setFont(font1)
        self.bt_nueve = QPushButton(self.centralwidget)
        self.bt_nueve.setObjectName(u"bt_nueve")
        self.bt_nueve.setGeometry(QRect(170, 230, 81, 51))
        self.bt_nueve.setFont(font1)
        self.bt_cuatro = QPushButton(self.centralwidget)
        self.bt_cuatro.setObjectName(u"bt_cuatro")
        self.bt_cuatro.setGeometry(QRect(10, 280, 81, 51))
        self.bt_cuatro.setFont(font1)
        self.bt_cinco = QPushButton(self.centralwidget)
        self.bt_cinco.setObjectName(u"bt_cinco")
        self.bt_cinco.setGeometry(QRect(90, 280, 81, 51))
        self.bt_cinco.setFont(font1)
        self.bt_multiplicar = QPushButton(self.centralwidget)
        self.bt_multiplicar.setObjectName(u"bt_multiplicar")
        self.bt_multiplicar.setGeometry(QRect(250, 230, 81, 51))
        self.bt_multiplicar.setFont(font1)
        self.bt_restar = QPushButton(self.centralwidget)
        self.bt_restar.setObjectName(u"bt_restar")
        self.bt_restar.setGeometry(QRect(250, 280, 81, 51))
        self.bt_restar.setFont(font1)
        self.bt_ocho = QPushButton(self.centralwidget)
        self.bt_ocho.setObjectName(u"bt_ocho")
        self.bt_ocho.setGeometry(QRect(90, 230, 81, 51))
        self.bt_ocho.setFont(font1)
        self.bt_siete = QPushButton(self.centralwidget)
        self.bt_siete.setObjectName(u"bt_siete")
        self.bt_siete.setGeometry(QRect(10, 230, 81, 51))
        self.bt_siete.setFont(font1)
        self.bt_seis = QPushButton(self.centralwidget)
        self.bt_seis.setObjectName(u"bt_seis")
        self.bt_seis.setGeometry(QRect(170, 280, 81, 51))
        self.bt_seis.setFont(font1)
        self.bt_parentesis_der = QPushButton(self.centralwidget)
        self.bt_parentesis_der.setObjectName(u"bt_parentesis_der")
        self.bt_parentesis_der.setGeometry(QRect(90, 80, 81, 51))
        self.bt_parentesis_der.setFont(font1)
        self.bt_parentesis_der.setStyleSheet(u"&radic;")
        self.bt_porcentaje = QPushButton(self.centralwidget)
        self.bt_porcentaje.setObjectName(u"bt_porcentaje")
        self.bt_porcentaje.setGeometry(QRect(170, 180, 81, 51))
        self.bt_porcentaje.setFont(font1)
        self.bt_dividir = QPushButton(self.centralwidget)
        self.bt_dividir.setObjectName(u"bt_dividir")
        self.bt_dividir.setGeometry(QRect(250, 180, 81, 51))
        self.bt_dividir.setFont(font1)
        self.bt_reiniciar = QPushButton(self.centralwidget)
        self.bt_reiniciar.setObjectName(u"bt_reiniciar")
        self.bt_reiniciar.setGeometry(QRect(170, 80, 81, 51))
        self.bt_reiniciar.setFont(font1)
        self.bt_parentesis_izq = QPushButton(self.centralwidget)
        self.bt_parentesis_izq.setObjectName(u"bt_parentesis_izq")
        self.bt_parentesis_izq.setGeometry(QRect(10, 80, 81, 51))
        self.bt_parentesis_izq.setFont(font1)
        self.bt_exponencial = QPushButton(self.centralwidget)
        self.bt_exponencial.setObjectName(u"bt_exponencial")
        self.bt_exponencial.setGeometry(QRect(90, 180, 81, 51))
        self.bt_exponencial.setFont(font1)
        self.bt_borrar = QPushButton(self.centralwidget)
        self.bt_borrar.setObjectName(u"bt_borrar")
        self.bt_borrar.setGeometry(QRect(250, 80, 81, 51))
        self.bt_borrar.setFont(font1)
        self.bt_raiz_cuadrada = QPushButton(self.centralwidget)
        self.bt_raiz_cuadrada.setObjectName(u"bt_raiz_cuadrada")
        self.bt_raiz_cuadrada.setGeometry(QRect(10, 180, 81, 51))
        self.bt_raiz_cuadrada.setFont(font1)
        self.display = QLabel(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(20, 10, 311, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setPointSize(28)
        self.display.setFont(font2)
        self.display.setTextFormat(Qt.TextFormat.AutoText)
        self.display.setScaledContents(False)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.display.setWordWrap(False)
        self.display.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.bt_historial = QPushButton(self.centralwidget)
        self.bt_historial.setObjectName(u"bt_historial")
        self.bt_historial.setGeometry(QRect(490, 390, 51, 31))
        self.bt_historial.setFont(font)
        self.bt_historial.setMouseTracking(True)
        self.bt_historial.setToolTipDuration(0)
        self.bt_historial.setStyleSheet(u"QPushButton#bt_historial {\n"
"            background-color: rgb(255, 0, 0);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    padding: 10px 20px;\n"
"    text-align: center;\n"
"        }\n"
"\n"
"QPushButton#bt_historial:hover {\n"
"            background-color: rgb(170, 0, 0);\n"
" }")
        icon1 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.bt_historial.setIcon(icon1)
        self.bt_historial.setIconSize(QSize(24, 24))
        self.bt_historial.setAutoDefault(False)
        self.TW_table = QTableWidget(self.centralwidget)
        self.TW_table.setObjectName(u"TW_table")
        self.TW_table.setEnabled(False)
        self.TW_table.setGeometry(QRect(350, 10, 331, 371))
        self.TW_table.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TW_table.setFrameShadow(QFrame.Shadow.Plain)
        self.TW_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.TW_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.TW_table.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.TW_table.horizontalHeader().setDefaultSectionSize(152)
        self.bt_coseno = QPushButton(self.centralwidget)
        self.bt_coseno.setObjectName(u"bt_coseno")
        self.bt_coseno.setGeometry(QRect(250, 130, 81, 51))
        self.bt_coseno.setFont(font1)
        self.bt_rand = QPushButton(self.centralwidget)
        self.bt_rand.setObjectName(u"bt_rand")
        self.bt_rand.setGeometry(QRect(10, 130, 81, 51))
        self.bt_rand.setFont(font1)
        self.bt_pi = QPushButton(self.centralwidget)
        self.bt_pi.setObjectName(u"bt_pi")
        self.bt_pi.setGeometry(QRect(90, 130, 81, 51))
        self.bt_pi.setFont(font1)
        self.bt_pi.setStyleSheet(u"")
        self.bt_log = QPushButton(self.centralwidget)
        self.bt_log.setObjectName(u"bt_log")
        self.bt_log.setGeometry(QRect(170, 130, 81, 51))
        self.bt_log.setFont(font1)
        self.bt_log.setStyleSheet(u"&radic;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.bt_dos.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.bt_num_entero.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.bt_uno.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.bt_cero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bt_coma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.bt_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.bt_sumar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.bt_tres.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.bt_nueve.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.bt_cuatro.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.bt_cinco.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.bt_multiplicar.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.bt_restar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.bt_ocho.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.bt_siete.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.bt_seis.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.bt_parentesis_der.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.bt_porcentaje.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.bt_dividir.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.bt_reiniciar.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.bt_parentesis_izq.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.bt_exponencial.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.bt_borrar.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.bt_raiz_cuadrada.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.display.setText("")
        self.bt_historial.setText("")
        self.bt_coseno.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.bt_rand.setText(QCoreApplication.translate("MainWindow", u"rand", None))
        self.bt_pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.bt_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
    # retranslateUi

