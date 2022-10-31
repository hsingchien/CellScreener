from qtpy import QtCore, QtGui
from qtpy.QtCore import Qt, QEvent

from qtpy.QtWidgets import QApplication, QMainWindow, QWidget, QDockWidget
from qtpy.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox
from qtpy.QtWidgets import QLabel, QPushButton, QComboBox
from qtpy.QtWidgets import QMessageBox

from typing import Callable, List, Optional, Tuple

class MainWindow(QMainWindow):
    def __init__(self, parent: typing.Optional[QWidget] = ..., flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = ...) -> None:
        super().__init__(parent, flags):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setAcceptDrops(True)

        self.neurons = Nuron()


