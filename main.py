import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Optional: integrate Jarvis logic later
# from jarvis import JarvisAssistant  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jarvis with 3D Robot")
        self.setGeometry(200, 100, 1000, 700)

        # Central widget
        widget = QWidget()
        layout = QVBoxLayout()

        # WebEngine View
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile(
            "YOUR_PATH/Jarvis3D/robot_viewer.html"
        ))

        layout.addWidget(self.browser)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # TODO: Launch JARVIS assistant in background thread

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
