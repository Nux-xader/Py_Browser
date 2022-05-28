from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

APP_NAME = "Py Browser"

class Browser(QMainWindow):
    def __init__(self) -> None:
        # super(Browser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle(APP_NAME)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(25)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(25)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()
    
    def navigate(self, url:str):
        self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication([])
    window = Browser()
    app.exec_()