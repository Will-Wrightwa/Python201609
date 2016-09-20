from system.core.controller import *
import random
import string

class rand_word(Controller):
    def __init__(self, action):
        super(rand_word, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        if not count in session:
            session['count'] = 0
        session['count'] += 1
        word = ""
        for n in range(14):
            word += random.choice(string.ascii_lowercase)
        return self.load_view('index.html',word=word)
