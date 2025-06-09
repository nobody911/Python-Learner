import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI window")
        self.setGeometry(80, 50, 800, 500)
        self.setWindowIcon(QIcon("wet-cat.jpeg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Courier", 80))
        label.setGeometry(80, 50, 800, 500)
        label.setStyleSheet("color: #d3d6d2;"
                            "background-color: #222e25;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP ALIGN
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM ALIGN
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER ALIGN

        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT ALIGN
        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT ALIGN
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER ALIGN

        # label.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # LEFT & TOP
        # label.setAlignment(Qt.AlignRight | Qt.AlignBottom)  # RIGHT & BOTTOM
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # CENTER & CENTER
        label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER (same as above)

        # there are many more combinations but im lazy soo DIY......

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()