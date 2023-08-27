import random
from PyQt5.QtWidgets import QApplication, QLineEdit, QSlider, QLabel
from PyQt5.QtWidgets import *
from PyQt5 import uic

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()

        uic.loadUi("password.ui", self)

        self.password_label = self.findChild(QLabel,"password_label")
        self.pass_slider= self.findChild(QSlider,"horizontalSlider")
        self.pass_length=self.findChild(QLabel,"label")
        self.passwordEdit = self.findChild(QLineEdit,"passwordEdit")
        self.refreshbutton = self.findChild(QPushButton, "refreshbutton")
        self.AZbutton1  = self.findChild(QPushButton,"AZbutton_1")
        self.AZbutton2 = self.findChild(QPushButton, "AZbutton_2")
        self.Symbolbutton = self.findChild(QPushButton, "Symbolbutton")
        self.Numberbutton = self.findChild(QPushButton, "Numberbutton")
        self.generateButton = self.findChild(QPushButton, "generateButton")
        self.copybutton = self.findChild(QPushButton, "copybutton")

        self.pass_length.setText(str(self.pass_slider.value()))
        self.pass_slider.valueChanged.connect(self.updatelabel)

        self.refreshbutton.clicked.connect(self.generate_password)
        self.generateButton.clicked.connect(self.generate_password)

        self.copybutton.clicked.connect(self.copy_to_clipboard)

        self.show()


    def updatelabel(self):
        self.pass_length.setText(str(self.pass_slider.value()))


    def generate_password(self):
        # Define the characters to use in the password
        characters = ''
        if self.Uppercase_checkBox.isChecked():
            characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self.Lowercase_checkBox.isChecked():
            characters += 'abcdefghijklmnopqrstuvwxyz'
        if self.Numbers_checkBox.isChecked():
            characters += '0123456789'
        if self.Symbols_checkBox.isChecked():
            characters += '!@#$%^&*()_+'

        if not characters :
            QMessageBox.warning(self,'Message' ,'password can not be null, please select checkbox of desired characters')
            return

        slider_value = self.pass_slider.value()
        # Generate a password of length slider
        password = ''.join(random.choice(characters) for i in range(slider_value))
        self.passwordEdit.setText(password)


    def copy_to_clipboard(self):
            text = self.passwordEdit.text()
            clipboard = QApplication.clipboard()
            clipboard.setText(text)
            QMessageBox.information(self, 'Copied to Clipboard', f'"{text}" has been copied to the clipboard.')


if __name__ == '__main__':
    app = QApplication([])
    UIWindow = PasswordGenerator()
    app.exec_()






