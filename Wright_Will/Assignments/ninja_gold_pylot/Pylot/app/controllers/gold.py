from system.core.controller import *
from random import randint
from time import strftime
locations = {"Farm":[10,20],"Cave":[5,10],"House":[2,5],"Casino":[-50,50]}
class gold(Controller):
    def __init__(self, action):
        super(gold, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        if not "gold" in session:
            session['gold'] = 0
        if not 'log' in session:
            session['log'] = []
        for key in locations:
            print key
        return self.load_view('index.html',locations=locations,gold=session['gold'],log=session['log'])

    def process(self):
        location = request.form['location']
        earnings = randint(locations[location][0],locations[location][1])
        session['gold'] += earnings
        color = "red"
        log_str = "<h6 class='"
        if earnings < 0:
            log_str +="red'> OH NO... You lost " + str(earnings) +" gold at " + location + strftime("(%Y/%m/%d %I:%M)") + "</h6>"
        else:
            log_str += "green'> Earned " + str(earnings) +" gold from " + location + strftime("(%Y/%m/%d %I:%M)") + "</h6>"
        session['log'].append(log_str)
        return redirect("/")
