from MainWindow import *



app = QApplication(sys.argv)

window = MainWindow()
window.show()

exit_code = app.exec()
sys.exit(exit_code)