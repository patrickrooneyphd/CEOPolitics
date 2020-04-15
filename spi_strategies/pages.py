from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class ProlificID(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

    def is_displayed(self):
        return self.round_number == 1
    pass


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def is_displayed(self):
        return self.round_number == 1


'''
class OpeningSurvey1(Page):
    form_model = 'player'
    form_fields = ['eligible_survey_1', 'eligible_survey_2', 'eligible_survey_3', 'eligible_survey_4',
                   'eligible_survey_5', 'eligible_survey_6', 'eligible_survey_7', 'eligible_survey_8',
                   'eligible_survey_9', 'eligible_survey_10']

    def is_displayed(self):
        return self.round_number == 1 and self.player.survey_key == 1

    def before_next_page(self):
        self.player.set_eligibility()


class OpeningSurvey2(Page):
    form_model = 'player'
    form_fields = ['eligible_survey_1', 'eligible_survey_2', 'eligible_survey_3', 'eligible_survey_4',
                   'eligible_survey_5', 'eligible_survey_6', 'eligible_survey_7', 'eligible_survey_8',
                   'eligible_survey_9', 'eligible_survey_10']

    def is_displayed(self):
        return self.round_number == 1 and self.player.survey_key == 2

    def before_next_page(self):
        self.player.set_eligibility()


class OpeningSurvey3(Page):
    form_model = 'player'
    form_fields = ['eligible_survey_1', 'eligible_survey_2', 'eligible_survey_3', 'eligible_survey_4',
                   'eligible_survey_5', 'eligible_survey_6', 'eligible_survey_7', 'eligible_survey_8',
                   'eligible_survey_9', 'eligible_survey_10']

    def is_displayed(self):
        return self.round_number == 1 and self.player.survey_key == 3

    def before_next_page(self):
        self.player.set_eligibility()
'''


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1  # and self.participant.vars['eligible'] == 1

    def before_next_page(self):
        self.player.start_time = time.time()

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
            'cause_statement': self.participant.vars['cause_statement'],
            'orig_value_s': Constants.orig_value,
        }
    pass


class ManagerAdvice(Page):
    def is_displayed(self):
        return self.round_number == 1   # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'orig_value_s': Constants.orig_value,
        }
    pass


class IntroductionBoard(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['condition'] == 'Board' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
            'orig_value_s': Constants.orig_value,
            'min_value_s': Constants.min_value,
        }
    pass


class IntroductionReputation(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['condition'] == 'Reputation' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }
    pass


class ConfirmNRA(Page):
    form_model = 'player'
    form_fields = ['confirm_cause_nra', 'confirm_money']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['cause'] == 'the National Rifle Association (NRA)' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
            'cause_statement': self.participant.vars['cause_statement']
        }
    pass


class ConfirmETFGS(Page):
    form_model = 'player'
    form_fields = ['confirm_cause_etfgs', 'confirm_money']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['cause'] == 'Everytown for Gun Safety' \
               # and self.participant.vars['eligible'] == 1
    
    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
            'cause_statement': self.participant.vars['cause_statement'],
        }
    pass


class ConfirmRC(Page):
    form_model = 'player'
    form_fields = ['confirm_cause_rc', 'confirm_money']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['cause'] == 'The American Red Cross' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
            'cause_statement': self.participant.vars['cause_statement']
        }
    pass


class MktResearchInstructions(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds / 2 + 1  # and self.participant.vars['eligible'] == 1
    pass


class MktResearchPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds / 2 + 1  # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }
    pass


class FirstPeriod(Page):
    form_model = 'player'
    form_fields = ['type1', 'cotton1', 'price1', 'social_action1']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['condition'] != 'Board' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }

    def before_next_page(self):
        self.player.first_period_to_vars()
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.reputation_adjust()
        self.player.donation_calculate()
        self.player.string_convert()
        self.player.set_payoffs()
    pass


class FirstPeriodBoard(Page):
    form_model = 'player'
    form_fields = ['type1', 'cotton1', 'price1', 'social_action1']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['condition'] == 'Board' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }

    def before_next_page(self):
        self.player.first_period_to_vars_board()
        self.player.initialize_board_calcs()
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.set_pre_decision_earnings()
        self.player.board_decision()
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.board_adjust()
        self.player.donation_calculate()
        self.player.string_convert()
        self.player.set_payoffs()
    pass


class PeriodFirstHalf(Page):
    form_model = 'player'
    form_fields = ['type', 'cotton', 'price', 'social_action']

    def is_displayed(self):
        return self.round_number < 6 and self.participant.vars['condition'] != 'Board' and self.round_number != 1 \
               # and self.participant.vars['eligible'] == 1

    def before_next_page(self):
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.reputation_adjust()
        self.player.donation_calculate()
        self.player.string_convert()
        self.player.set_payoffs()

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'cause': self.participant.vars['cause']
        }
    pass


class PeriodBoardFirstHalf(Page):
    form_model = 'player'
    form_fields = ['type_b', 'cotton_b', 'price_b', 'social_action_b']

    def is_displayed(self):
        return self.round_number < 6 and self.participant.vars['condition'] == 'Board' and self.round_number != 1 \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'cause': self.participant.vars['cause']
        }

    def before_next_page(self):
        self.player.initialize_board_calcs()
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.set_pre_decision_earnings()
        self.player.board_decision()
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.board_adjust()
        self.player.donation_calculate()
        self.player.string_convert()
        self.player.set_payoffs()

    pass


class PeriodSecondHalf(Page):
    form_model = 'player'
    form_fields = ['type', 'cotton', 'price', 'social_action']

    def is_displayed(self):
        return self.round_number > 5 and self.participant.vars['condition'] != 'Board' \
               # and self.participant.vars['eligible'] == 1

    def before_next_page(self):
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.reputation_adjust()
        self.player.donation_calculate()
        self.player.string_convert()
        self.player.set_payoffs()

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'cause': self.participant.vars['cause']
        }
    pass


class PeriodBoardSecondHalf(Page):
    form_model = 'player'
    form_fields = ['type_b', 'cotton_b', 'price_b', 'social_action_b']

    def is_displayed(self):
        return self.round_number > 5 and self.participant.vars['condition'] == 'Board' \
             # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'player_in_previous_rounds': self.player.in_previous_rounds(),
            'cause': self.participant.vars['cause']
        }

    def before_next_page(self):
        self.player.initialize_board_calcs()
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.set_pre_decision_earnings()
        self.player.board_decision()
        self.player.determine_type_match()
        self.player.determine_round_earnings()
        self.player.board_adjust()
        self.player.donation_calculate()
        self.player.string_convert()
        self.player.set_payoffs()
    pass


class Results(Page):
    form_model = 'player'
    form_fields = ['round_earnings_n', 'type_n', 'cotton_n', 'price_n', 'social_action_n']

    def is_displayed(self):
        return self.participant.vars['condition'] != 'Board'  # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }
    pass


class ResultsBoard(Page):
    form_model = 'player'
    form_fields = ['round_earnings_n', 'type_n', 'cotton_n', 'price_n', 'social_action_n', 'board_block_n']

    def is_displayed(self):
        return self.participant.vars['condition'] == 'Board'  # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }
    pass


class AttentionCheck(Page):
    form_model = 'player'
    form_fields = ['attention_check']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds  # and self.participant.vars['eligible'] == 1
    pass


class ManipulationChecks(Page):
    form_model = 'player'
    form_fields = ['manip_1', 'manip_2', 'manip_3', 'manip_4']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.participant.vars['condition'] == 'Control' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }
    pass


class ManipulationChecksBoard(Page):
    form_model = 'player'
    form_fields = ['manip_1', 'manip_2', 'manip_3', 'manip_4', 'manip_b1', 'manip_b2']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.participant.vars['condition'] == 'Board' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }
    pass


class ManipulationChecksReputation(Page):
    form_model = 'player'
    form_fields = ['manip_1', 'manip_2', 'manip_3', 'manip_4', 'manip_r1', 'manip_r2']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.participant.vars['condition'] == 'Reputation' \
               # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        return {
            'cause': self.participant.vars['cause'],
        }
    pass


class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'race', 'volunteer', 'donated', 'politics', 'stance_opinion', 'csr_opinion',
                   'trolley']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds  # and self.participant.vars['eligible'] == 1
    pass


class AversionPage(Page):
    form_model = 'player'
    form_fields = ['risk1', 'risk2', 'risk3', 'risk4', 'risk5', 'amb1', 'amb2', 'amb3', 'amb4', 'amb5', 'amb6', 'amb7']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds  # and self.participant.vars['eligible'] == 1

    def before_next_page(self):
        self.player.extra_payments()
    pass


class OpenComments(Page):
    form_model = 'player'
    form_fields = ['open_comments']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds  # and self.participant.vars['eligible'] == 1

    def before_next_page(self):
        self.player.end_time = time.time()
    pass


class FinalPayment(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds  # and self.participant.vars['eligible'] == 1

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()
        list_donations = [p.donation for p in player_in_all_rounds]
        donations = sum(list_donations)
        self.player.donation = donations
        self.player.donation_str = '{:,.2f}'.format(self.player.donation)
        self.participant.vars['donation'] = self.player.donation_str

        return {
            'paying_round_a': self.participant.vars['paying_round_a'],
            'payoff_a': self.participant.vars['payoff_a'],
            'paying_round_b': self.participant.vars['paying_round_b'],
            'payoff_b': self.participant.vars['payoff_b'],
            'risk_payoff': self.participant.vars['risk_payoff'],
            'amb_payoff': self.participant.vars['amb_payoff'],
            'payoff': self.participant.payoff_plus_participation_fee(),
            'cause': self.participant.vars['cause'],
            'donation': self.participant.vars['donation']
        }
    pass


# class Ineligible(Page):
#     def is_displayed(self):
#         return self.participant.vars['eligible'] == 0


page_sequence = [
    ProlificID,
    Consent,
    # OpeningSurvey1,
    # OpeningSurvey2,
    # OpeningSurvey3,
    Introduction,
    ManagerAdvice,
    IntroductionBoard,
    IntroductionReputation,
    ConfirmNRA,
    ConfirmETFGS,
    ConfirmRC,
    MktResearchInstructions,
    MktResearchPage,
    FirstPeriod,
    FirstPeriodBoard,
    PeriodFirstHalf,
    PeriodBoardFirstHalf,
    PeriodSecondHalf,
    PeriodBoardSecondHalf,
    Results,
    ResultsBoard,
    AttentionCheck,
    Questionnaire,
    AversionPage,
    ManipulationChecks,
    ManipulationChecksBoard,
    ManipulationChecksReputation,
    OpenComments,
    FinalPayment,
    # Ineligible,
]
