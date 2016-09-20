from system.core.controller import *

cities = [ne]

class gold(Controller):
    def __init__(self, action):
        super(gold, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        cites = ["Dallas","San Fansisco","Seattle","San Diego", "New York"]
        languages = ["Python","jacasript"]
        return self.load_view('index.html',cities=cities,languages=languages)

    def process(self):
        if not "count" in session['user']:
            session['user']['count'] = 0
        session['user']['count'] += 1

        session['user'] = {
            "name":request.form("name"),
            "location":request.form("location"),
            "language":request.form("language")
        }

        return redirect("/success")
    def success(self):
        return self.load_view('success.html')
