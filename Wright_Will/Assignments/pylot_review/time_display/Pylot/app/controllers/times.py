from system.core.controller import *
from time import strftime
class times(Controller):
    def __init__(self, action):
        super(times, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):

        return self.load_view('index.html')
