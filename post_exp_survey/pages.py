from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    timeout_seconds = 90
    form_model = 'player'
    form_fields = ['test_intro']


class Decision(Page):
    form_model = 'player'
    form_fields = ['choice1', 'explanation', 'choice2']


    def before_next_page(self):
        self.player.set_x1()
        self.player.set_x2()
        self.player.set_x3()
        self.player.set_x4()
        self.player.set_x5()

class Belief(Page):
    form_model = 'player'
    form_fields = ['fair', 'transparent', 'simpler', 'familiar', 'characteristics','previous_performance',
                   'discriminate', 'quickly', 'error','other']





page_sequence = [
    Introduction,
    Decision,
    Belief,

]
