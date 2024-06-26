import sys
from PySide6.QtWidgets import QApplication
from models.model import Model
from controllers.controller import Controller
from views.view import View


class Main(QApplication):
    def __init__(self, argv):
        super(Main, self).__init__(argv)
        self._model = Model()
        self._controller = Controller(self._model)
        self._view = View(self._model, self._controller)
        self._view.show()
