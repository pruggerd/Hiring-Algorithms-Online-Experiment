from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'player'
    form_fields = ['explanation1', 'explanation2']


class End(Page):
    pass


page_sequence = [
    Decision,
    End,

]
