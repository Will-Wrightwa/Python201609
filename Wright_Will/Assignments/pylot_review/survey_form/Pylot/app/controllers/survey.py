from system.core.controller import *



class survey(Controller):
    def __init__(self, action):
        super(survey, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        cities = ["Dallas","San Fansisco","Seattle","San Diego", "New York"]
        languages = ["Python","jacasript"]
        return self.load_view('index.html',cities=cities,languages=languages)

    def process(self):

        session['user'] = {
            "name":request.form["name"],
            "location":request.form["location"],
            "language":request.form["language"],
            "comment":request.form["comment"]
        }
        if not "count" in session['user']:
            session['user']['count'] = 0
        session['user']['count'] += 1

        return redirect("/survey/success")
    def success(self):
        return self.load_view('results.html')
