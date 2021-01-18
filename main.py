"""
(c) ilhamitugral - 2021
All Rights Reserved
Created For Usak University Visual Programming Homework

"""
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout,QVBoxLayout, QPushButton, QLabel, QLineEdit

# User information is here.
_username = "ilhamitugral"
_password = "1234"

# This class is Login Form Window
class LoginWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Login Window specs here.
        self.setWindowTitle("Sign In")
        self.resize(300, 100)

        # Let's create layout
        layout = QGridLayout()

        # Error Label
        self.errorText = QLabel("")
        layout.addWidget(self.errorText, 0, 0)

        # Username Text Label
        self.usernameLabel = QLabel("Username:")
        layout.addWidget(self.usernameLabel, 1, 0)

        # Username Input
        self.usernameInput = QLineEdit()
        layout.addWidget(self.usernameInput, 2, 0, 1, 2)

        # Password Text Label
        self.passwordLabel = QLabel("Password:")
        layout.addWidget(self.passwordLabel, 3, 0)

        # Password Input
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passwordInput, 4, 0, 1, 2)

        # Login Button
        self.loginButton = QPushButton("Sign In")
        self.loginButton.clicked.connect(lambda: self.tryLogin(self.usernameInput.text(), self.passwordInput.text()))
        layout.addWidget(self.loginButton, 5, 0, 1, 1)

        # Register Button
        self.registerButton = QPushButton("Sign Up")
        self.registerButton.clicked.connect(self.tryRegister)
        layout.addWidget(self.registerButton, 5, 1, 1, 1)

        # Lost Password Button
        self.lostPasswordButton = QPushButton("Reset Account")
        self.lostPasswordButton.clicked.connect(self.openLostPassword)
        layout.addWidget(self.lostPasswordButton, 6, 0, 1, 2)

        # Copyright information ;)
        self.copyright = QLabel("<div style=\"text-align: right;\">© ilhamitugral</div>")
        layout.addWidget(self.copyright, 7, 0, 1, 2)

        # Layout is completed. Lets show on window.
        self.setLayout(layout)

    # This method will be open Homepage
    def openHomepage(self):
        self.homepage = HomepageWindow()
        self.close()
        self.homepage.show()

    # This method will be open Register Form
    def openRegister(self):
        self.register = RegisterWindow()
        self.close()
        self.register.show()

    # This method will be open Lost Password Form
    def openLostPassword(self):
        self.lostPassword = ResetPassword()
        self.close()
        self.lostPassword.show()

    # This method will be try login.
    def tryLogin(self, username, password):
        if username == _username and password == _password:
            print("Sign In Success!")
            self.openHomepage()
        else:
            self.errorText.setText("<font color=\"red\">Username or password wrong.</font>")

    # This method will be try register the system.
    def tryRegister(self):
        self.openRegister()

# This is a Register Window class
class RegisterWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Register Window information is here.
        self.setWindowTitle("Sign Up")
        self.resize(300, 100)

        # We're create a layout for Register Window
        layout = QGridLayout()

        # Error Label
        self.errorText = QLabel("")
        layout.addWidget(self.errorText, 0, 0)

        # Username Text Label
        self.usernameLabel = QLabel("Username:")
        layout.addWidget(self.usernameLabel, 1, 0)

        # Username Input
        self.usernameInput = QLineEdit()
        layout.addWidget(self.usernameInput, 2, 0, 1, 2)

        # Password Text Label
        self.passwordLabel = QLabel("Password:")
        layout.addWidget(self.passwordLabel, 3, 0)

        # Password Input
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.passwordInput, 4, 0, 1, 2)

        # Password Text Label
        self.rePasswordLabel = QLabel("Re-Password:")
        layout.addWidget(self.rePasswordLabel, 5, 0)

        # Re-Password Input
        self.rePasswordInput = QLineEdit()
        self.rePasswordInput.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.rePasswordInput, 6, 0, 1, 2)

        # Register Button
        self.registerButton = QPushButton("Sign Up")
        self.registerButton.clicked.connect(lambda: self.tryRegister(self.usernameInput.text(),
                                                                     self.passwordInput.text(),
                                                                     self.rePasswordInput.text()))
        layout.addWidget(self.registerButton, 7, 0)

        # Login Button
        self.loginButton = QPushButton("Sign In")
        self.loginButton.clicked.connect(self.openLogin)
        layout.addWidget(self.loginButton, 7, 1)

        # Copyright information ;)
        self.copyright = QLabel("<div style=\"text-align: right;\">© ilhamitugral</div>")
        layout.addWidget(self.copyright, 8, 0, 1, 2)

        # Let's set layout to window.
        self.setLayout(layout)

    # This method will be open Login Form
    def openLogin(self):
        self.login = LoginWindow()
        self.close()
        self.login.show()

    # This method will be try register to project. (It's virtual example)
    def tryRegister(self, username, password, rePassword):
        if username == _username and password == _password and password == rePassword:
            print("Kayıt başarılı!")
            self.openLogin()
        else:
            self.errorText.setText("<font color=\"red\">Sign Up failed! Please try again later.</font>")

# This class Reset Password screen.
class ResetPassword(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Lets set windows info.
        self.setWindowTitle("Reset Password")
        self.resize(300, 100)

        # We're create a layout here.
        layout = QGridLayout()

        # Error Label
        self.errorText = QLabel("")
        layout.addWidget(self.errorText, 0, 0)

        # Username Text Label
        self.usernameLabel = QLabel("Username:")
        layout.addWidget(self.usernameLabel, 1, 0)

        # Username Input Label
        self.usernameInput = QLineEdit()
        layout.addWidget(self.usernameInput, 2, 0)

        # Lost Password Button
        self.lostPasswordButton = QPushButton("Submit")
        self.lostPasswordButton.clicked.connect(lambda: self.tryReset(self.usernameInput.text()))
        layout.addWidget(self.lostPasswordButton, 3, 0)

        # Copyright information ;)
        self.copyright = QLabel("<div style=\"text-align: right;\">© ilhamitugral</div>")
        layout.addWidget(self.copyright, 4, 0, 1, 1)

        # Layout completed. Let's show layout.
        self.setLayout(layout)

    # This method will try reset the password (Virtual example)
    def tryReset(self, username):
        if username == "":
            self.errorText.setText("<font color=\"red\">Username cannot empty.</font>")
        elif not username == _username:
            self.errorText.setText("<font color=\"red\">Invalid Username</font>")
        else:
            self.openLogin()
            print("Account reset success. You can Sign In now.")

    def openLogin(self):
        self.login = LoginWindow()
        self.close()
        self.login.show()

# This class will be show Homepage window.
class HomepageWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Homepage screen information is here.
        self.setWindowTitle("Homepage")
        self.resize(300, 100)

        # We are set a new layout.
        layout = QVBoxLayout()

        # Welcome Text
        welcomeText = QLabel("Welcome, {}".format(_username))
        layout.addWidget(welcomeText)

        # Close App Button
        closeButton = QPushButton("Close App")
        closeButton.clicked.connect(self.closeApp)
        layout.addWidget(closeButton)

        # Copyright information ;)
        self.copyright = QLabel("<div style=\"text-align: right;\">© ilhamitugral</div>")
        layout.addWidget(self.copyright)

        # And now lets set layout to window.
        self.setLayout(layout)

    # This method will be close app.
    def closeApp(self):
        self.close()

def main():
    import sys

    # Let's try to execute window.
    app = QApplication(sys.argv)
    LoginWindow().show()
    sys.exit(app.exec_())

# Let's run!
if __name__ == '__main__':
    main()