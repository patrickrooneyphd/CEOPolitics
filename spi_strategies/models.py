from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

#import itertools
import random
import numpy as np
from django.core.validators import MaxValueValidator, MinValueValidator

author = 'Patrick Rooney'

doc = """
Antecedents to CEOs' Strategic Political Stances
"""


class Constants(BaseConstants):
    name_in_url = 'spi_strategies'
    players_per_group = None
    num_rounds = 20
    max_pi = np.array([7.0, 10.0, 18.0])
    opt_values = np.array([[90, 60, 10], [9, 49, 99]])
    penalty = np.array([[0.25, 5, 6], [0.25, 2, 3], [0.25, 2, 3]])
    donation_pct = 0.10
    orig_value = 5.75
    reputation_penalty = 1.00
    min_value = 1.00
    board_deny_threshold = 50


class Subsession(BaseSubsession):

    def creating_session(self):
        # == Randomize Conditions == #
        if self.round_number == 1:
            for p in self.get_players():
                # condition = random.choice(['Board', 'Reputation', 'Control']) # Hidden for pilot testing.
                condition = random.choice(['Board', 'Reputation'])
                cause = random.choice(['Planned Parenthood', 'The National Right to Life Committee',
                                      'The American Red Cross'])
                if condition != 'Control':
                    cause = 'Planned Parenthood'
                else:
                    cause = cause

                if cause == 'Planned Parenthood':
                    cause_statement = "which is the largest organization in the United States dedicated to women's \
                    reproductive health services. It is also the largest provider of abortions in the country"
                elif cause == 'The National Right to Life Committee':
                    cause_statement = "which is the largest organization in the United States dedicated to lobbying for \
                    pro-life causes. It principally advocates against abortion, as well as euthanasia and assisted suicide"
                else:
                    cause_statement = "which is an American humanitarian organization that provides emergency assistance, \
                    disaster relief and preparedness programs. It is part of the largest humanitarian network in the world"

                p.condition = condition
                p.cause = cause
                p.participant.vars['condition'] = condition
                p.participant.vars['cause'] = cause
                p.participant.vars['cause_statement'] = cause_statement
                p.participant.vars['donation_num'] = 0
                p.participant.vars['social_action_count'] = 0
            else:
                self.group_like_round(1)

        # == Choose Paid Rounds == #
        if self.round_number == 1:
            paying_round_a = random.randint(1, Constants.num_rounds/2)
            paying_round_b = random.randint(Constants.num_rounds/2 + 1,  Constants.num_rounds)
            for p in self.get_players():
                #paying_round_a = random.randint(1, Constants.num_rounds/2)
                #paying_round_b = random.randint(Constants.num_rounds/2 + 1,  Constants.num_rounds)
                p.paying_round_a = paying_round_a
                p.paying_round_b = paying_round_b
                p.participant.vars['paying_round_a'] = paying_round_a
                p.participant.vars['paying_round_b'] = paying_round_b
                p.donation_sum = 0.00
        else:
            pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    ## == OBJECTS == ##
    # == Base Objects == #
    prolific_id = models.StringField()
    start_time = models.FloatField()
    end_time = models.FloatField()
    round_earnings = models.FloatField()
    round_earnings_str = models.StringField()
    round_earnings_init = models.FloatField()
    condition = models.StringField()
    cause = models.StringField()
    consent = models.StringField(label='', choices=['I consent'], widget=widgets.TextInput)
    confirm_cause_pp = models.StringField(label='',
                                          choices=['Any donations I make in this experiment will '
                                                   'go to Planned Parenthood.'],
                                          widget=widgets.TextInput)
    confirm_cause_nrtlc = models.StringField(label='',
                                             choices=['Any donations I make in this experiment will go to The '
                                                      'National Right to Life Committee.'],
                                             widget=widgets.TextInput)
    confirm_cause_rc = models.StringField(label='',
                                          choices=['Any donations I make in this experiment '
                                                   'will go to The American Red Cross.'],
                                          widget=widgets.TextInput)
    confirm_money = models.StringField(label='', choices=['My personal earnings in this experiment will be paid '
                                                          'to me in real money.'],
                                       widget=widgets.TextInput)
    donation = models.FloatField()
    donation_sum = models.FloatField()
    round_donation_str = models.StringField()
    donation_str = models.StringField()
    payoff_a = models.FloatField()
    payoff_a_str = models.StringField()
    payoff_b = models.FloatField()
    payoff_b_str = models.StringField()
    paying_round_a = models.IntegerField()
    paying_round_b = models.IntegerField()
    rand_num = models.IntegerField()
    social_action_count = models.IntegerField()

    # == Create Production Objects == #
    type = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Sweater Vest', 'Cardigan', 'Turtleneck'],
        blank=False
    )
    cotton = models.PositiveIntegerField(label='',
                                         blank=False,
                                         validators=[MinValueValidator(0), MaxValueValidator(100)])
    price = models.PositiveIntegerField(label='',
                                        blank=False,
                                        validators=[MinValueValidator(9), MaxValueValidator(109)])
    social_action = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['No Action', 'Donate 10% of Period Earnings'],
        blank=False
    )
    type1 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Sweater Vest', 'Cardigan', 'Turtleneck'],
        blank=False,
        initial='Sweater Vest'
    )
    cotton1 = models.PositiveIntegerField(label='', validators=[MinValueValidator(0), MaxValueValidator(100)],
                                          blank=False, initial=80)
    price1 = models.PositiveIntegerField(label='', validators=[MinValueValidator(9), MaxValueValidator(109)],
                                         blank=False, initial=49)
    social_action1 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['No Action', 'Donate 10% of Period Earnings'],
        blank=False,
        initial='No Action'
    )
    t_match1 = models.BooleanField()
    t_match2 = models.BooleanField()
    t_match3 = models.BooleanField()
    d_match1 = models.BooleanField()
    d_match2 = models.BooleanField()
    d_match3 = models.BooleanField()
    match1 = models.BooleanField()
    match2 = models.BooleanField()
    match3 = models.BooleanField()

    # == Notes Variables on Results Page == #
    round_earnings_n = models.DecimalField(label='', decimal_places=2, max_digits=4, blank=True)
    type_n = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Sweater Vest', 'Cardigan', 'Turtleneck'],
        blank=True
    )
    cotton_n = models.IntegerField(label='', blank=True)
    price_n = models.IntegerField(label='', blank=True)
    social_action_n = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['No Action', 'Donate 10% of Period Earnings'],
        blank=True
    )
    board_block_n = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Blocked', 'Did Not Block'],
        blank=True
    )

    # == Board Condition Variables == #
    type_b = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Sweater Vest', 'Cardigan', 'Turtleneck'],
        blank=False
    )
    cotton_b = models.IntegerField(label='', blank=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    price_b = models.IntegerField(label='', blank=False, validators=[MinValueValidator(9), MaxValueValidator(109)])
    social_action_b = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['No Action', 'Donate 10% of Period Earnings'],
        blank=False
    )
    board_block = models.StringField()
    board_penalty = models.StringField()

    # == Attention and Manipulation Check Objects == #

    attention_check = models.StringField(label='', blank=True)

    manip_1 = models.StringField(label='', widget=widgets.Textarea)
    manip_2 = models.StringField(label='', widget=widgets.Textarea)
    manip_3 = models.StringField(label='', widget=widgets.Textarea)
    manip_4 = models.StringField(label='', widget=widgets.Textarea)

    manip_b1 = models.StringField(label='', widget=widgets.Textarea)
    manip_b2 = models.StringField(label='', widget=widgets.Textarea)

    manip_r1 = models.StringField(label='', widget=widgets.Textarea)
    manip_r2 = models.StringField(label='', widget=widgets.Textarea)


    # == Questionnaire and Risk/Amb Aversion Objects == #
    age = models.IntegerField(label='', min=0, max=100, blank=True)
    gender = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Male', 'Female', 'Non-Binary', 'Prefer not to Disclose'],
        blank=True
    )
    race = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['White', 'Black', 'East Asian', 'South Asian', 'Middle Eastern', 'Hispanic', 'Multi-racial',
                 'Other'],
        blank=True
    )
    volunteer = models.StringField(label='', widget=widgets.RadioSelect, choices=['Yes', 'No'], blank=True)
    donated = models.StringField(label='', widget=widgets.RadioSelect, choices=['Yes', 'No'], blank=True)
    politics = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Very Conservative', 'Moderately Conservative', 'Lean Conservative', 'Lean Liberal',
                 'Moderately Liberal', 'Very Liberal'],
        blank=True
    )
    stance_opinion = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Very Inappropriate', 'Moderately Inappropriate', 'Slightly Inappropriate', 'Slightly Appropriate',
                 'Moderately Appropriate', 'Very Appropriate'],
        blank=True
    )
    csr_opinion = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Very Inappropriate', 'Moderately Inappropriate', 'Slightly Inappropriate', 'Slightly Appropriate',
                 'Moderately Appropriate', 'Very Appropriate'],
        blank=True
    )
    trolley = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Do Nothing; Kill Five People', 'Jerk to the Right; Kill One Person'],
        blank=True
    )
    risk1 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$7 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    risk2 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$6 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    risk3 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$5 for certain', '$10 with probability, $2 with probability 50%'],
        blank=True
    )
    risk4 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$4 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    risk5 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['$3 for certain', '$10 with probability 50%, $2 with probability 50%'],
        blank=True
    )
    amb1 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 16 red balls and 4 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb2 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 14 red balls and 6 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb3 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 12 red balls and 8 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb4 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 10 red balls and 10 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb5 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 8 red balls and 12 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb6 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 6 red balls and 14 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    amb7 = models.StringField(
        label='',
        widget=widgets.RadioSelect,
        choices=['Bag 1 (containing 4 red balls and 16 black balls)', 'Bag 2 (containing 20 balls)'],
        blank=True
    )
    risk_payoff = models.FloatField()
    risk_payoff_str = models.StringField()
    amb_payoff = models.FloatField()
    amb_payoff_str = models.StringField()
    open_comments = models.StringField(
        label='',
        widget=widgets.Textarea,
        blank=True
    )

    # == FUNCTIONS == #
    # == Assign first period choices to choice variables == #
    def first_period_to_vars(self):
        self.type = self.type1
        self.cotton = self.cotton1
        self.price = self.price1
        self.social_action = self.social_action1

    def first_period_to_vars_board(self):
        self.type_b = self.type1
        self.cotton_b = self.cotton1
        self.price_b = self.price1
        self.social_action_b = self.social_action1

    # == Set random numbers for functions that follow== #
    def set_rand_num(self):
        self.rand_num = random.randint(0, 100)

    # == Adjust payoff for board condition == #
    def board_interference(self):
        if self.social_action_b == 'No Action' or self.rand_num > Constants.board_deny_threshold:
            self.board_block = "Did Not Block"
            self.board_penalty = "No penalty"
            self.type = self.type_b
            self.cotton = self.cotton_b
            self.price = self.price_b
            self.social_action = self.social_action_b
        else:
            self.board_block = "Blocked"
            self.board_penalty = "A $1.00 penalty"
            self.type = 'Sweater Vest'
            self.cotton = 80
            self.price = 49
            self.social_action = 'No Action'

    # == Determine if participant chose optimal type given spi action == #
    def determine_type_match(self):
        self.t_match1 = (self.type == "Sweater Vest")
        self.t_match2 = (self.type == "Turtleneck")
        self.t_match3 = (self.type == "Cardigan")
        self.d_match1 = (self.social_action == 'No Action')
        self.d_match2 = (self.social_action == 'Donate 10% of Period Earnings')
        self.match1 = (self.t_match1 == self.d_match1)
        self.match2 = (self.t_match2 == self.d_match2)
        self.match3 = (self.t_match3 == self.d_match3)

    # == Determine payoffs by category == #
    def determine_round_earnings(self):
        if self.social_action == 'No Action' and self.type == 'Sweater Vest':
            self.round_earnings = round(max(Constants.max_pi[0] - \
                          abs(Constants.opt_values[0, 0] - self.cotton) / 10.0 * Constants.penalty[1, 0] - \
                          abs(Constants.opt_values[1, 0] - self.price) / 10.0 * Constants.penalty[2, 0],
                                            Constants.min_value), 2)

        elif self.social_action == 'No Action' and self.type != 'Sweater Vest':
            self.round_earnings = round(max(Constants.max_pi[0] - Constants.penalty[0, 0] - \
                          abs(Constants.opt_values[0, 0] - self.cotton) / 10.0 * Constants.penalty[1, 0] - \
                          abs(Constants.opt_values[1, 0] - self.price) / 10.0 * Constants.penalty[2, 0],
                                            Constants.min_value), 2)

        elif self.social_action == 'Donate 10% of Period Earnings' and self.type == 'Sweater Vest':
            self.round_earnings = round(max(Constants.max_pi[0] - Constants.penalty[0, 2] - \
                          abs(Constants.opt_values[0, 0] - self.cotton) / 10.0 * Constants.penalty[1, 0] - \
                          abs(Constants.opt_values[1, 0] - self.price) / 10.0 * Constants.penalty[2, 0],
                                            Constants.min_value), 2)

        elif self.social_action == 'Donate 10% of Period Earnings' and self.type == 'Turtleneck':
            self.round_earnings = round(max(Constants.max_pi[1] - \
                          abs(Constants.opt_values[0, 1] - self.cotton) / 10.0 * Constants.penalty[1, 1] - \
                          abs(Constants.opt_values[1, 1] - self.price) / 10.0 * Constants.penalty[2, 1],
                                            Constants.min_value), 2)

        elif self.social_action == "Donate 10% of Period Earnings" and self.type == 'Cardigan':
            self.round_earnings = round(max(Constants.max_pi[2] - \
                          abs(Constants.opt_values[0, 2] - self.cotton) / 10.0 * Constants.penalty[1, 2] - \
                          abs(Constants.opt_values[1, 2] - self.price) / 10.0 * Constants.penalty[2, 2],
                                            Constants.min_value), 2)

        self.round_earnings_init = round(self.round_earnings, 2)

    # == Adjust payoff for board interference and reputation == #
    def board_adjust(self):
        if self.board_block == 'Blocked':
            self.round_earnings = Constants.orig_value - Constants.min_value
        else:
            self.round_earnings = self.round_earnings

    def reputation_adjust(self):
        if self.participant.vars['condition'] == 'Reputation':
            if self.social_action != 'No Action':
                self.participant.vars['social_action_count'] += 1
            else:
                self.participant.vars['social_action_count'] = self.participant.vars['social_action_count']
        else:
            self.round_earnings = self.round_earnings

        if self.social_action == 'No Action':
            self.round_earnings = max((self.round_earnings - (Constants.reputation_penalty *
                                                              self.participant.vars['social_action_count']), 0.00))
        else:
            self.round_earnings = self.round_earnings

    # == Calculate donation == #
    def donation_calculate(self):
        if self.social_action == 'Donate 10% of Period Earnings':
            self.donation = round((self.round_earnings * Constants.donation_pct), 2)
            self.round_earnings = self.round_earnings - self.donation
        else:
            self.donation = 0.00

    # == Create String Variables for Currencies on Results Pages == #
    def string_convert(self):
        self.round_earnings_str = '{:,.2f}'.format(self.round_earnings)
        self.round_donation_str = '{:,.2f}'.format(self.donation)

    # == Calculate payoffs and create strings for final display== #
    def set_payoffs(self):
        if self.subsession.round_number == self.participant.vars['paying_round_a']:
            self.payoff_a = round(self.round_earnings / 2, 2)
            self.payoff = self.payoff_a
            self.payoff_a_str = '{:,.2f}'.format(self.payoff_a)
            self.participant.vars['payoff_a'] = self.payoff_a_str
            self.donation = round(self.donation / 2, 2)
        else:
            pass

        if self.subsession.round_number == self.participant.vars['paying_round_b']:
            self.payoff_b = round(self.round_earnings / 2, 2)
            self.payoff = self.payoff + self.payoff_b
            self.payoff_b_str = '{:,.2f}'.format(self.payoff_b)
            self.participant.vars['payoff_b'] = self.payoff_b_str
            self.donation = round(self.donation / 2, 2)
        else:
            pass

        if self.subsession.round_number == self.participant.vars['paying_round_a'] \
                or self.subsession.round_number == self.participant.vars['paying_round_b']:
            self.donation = self.donation
        else:
            self.donation = 0

    def extra_payments(self):
        risk = random.choice([self.risk1, self.risk2, self.risk3, self.risk4, self.risk5])
        risk_dict = {self.risk1: 0.70, self.risk2: 0.60, self.risk3: 0.50, self.risk4: 0.40, self.risk5: 0.30}
        amb = random.choice([self.amb1, self.amb2, self.amb3, self.amb4, self.amb5, self.amb6, self.amb7])
        amb_dict = {self.amb1: 80, self.amb2: 70, self.amb3: 60, self.amb4: 50, self.amb5: 40,
                    self.amb6: 30, self.amb7: 20}
        rand1 = random.randint(0, 100)
        rand2 = random.randint(0, 100)

        #== Risk Aversion Payoffs ==#
        if risk == '$10 with probability 50%, $2 with probability 50%':
            if rand1 > 50:
                self.payoff = self.payoff + 1.00
                self.risk_payoff = 1.00
            else:
                self.risk_payoff = 0.20
                self.payoff = self.payoff + 0.20
        else:
            self.risk_payoff = risk_dict[risk]
            self.payoff = self.payoff + self.risk_payoff

        # == Ambiguity Aversion Payoffs ==#
        if amb == 'Bag 2 (containing 20 balls)':
            if rand1 > rand2:
                self.payoff = self.payoff + 1.00
                self.amb_payoff = 1.00
            else:
                self.payoff = self.payoff + 0.20
                self.amb_payoff = 0.20
        else:
            amb_val = amb_dict[amb]
            if amb_val > rand2:
                self.payoff = self.payoff + 1.00
                self.amb_payoff = 1.00
            else:
                self.payoff = self.payoff + 0.20
                self.amb_payoff = 0.20

        self.risk_payoff_str = '{:,.2f}'.format(self.risk_payoff)
        self.participant.vars['risk_payoff'] = self.risk_payoff_str
        self.amb_payoff_str = '{:,.2f}'.format(self.amb_payoff)
        self.participant.vars['amb_payoff'] = self.amb_payoff_str




