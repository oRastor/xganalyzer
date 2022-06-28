import os
import unittest
import pandas

from src.xganalyzer.events_aggregator import GamesEventsAggregator, CalculateContext, CalculateType, CalculateLocation


class TestGameStatisticsAggregator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dirname = os.path.dirname(__file__)

        games_df = pandas.read_csv(os.path.join(dirname, 'data/games.csv'))
        events_df = pandas.read_csv(os.path.join(dirname, 'data/events.csv'))

        cls.aggregator = GamesEventsAggregator(games_df, events_df)

    def test_get_team_ids(self):
        self.assertEqual(14861, self.aggregator.get_home_team_id(85804))
        self.assertEqual(6719, self.aggregator.get_away_team_id(85804))

    def test_get_events(self):
        events_df = self.aggregator.get_events(85804)
        self.assertEqual(30, len(events_df))

    def test_calculate_games_count(self):
        events_df = self.aggregator.get_events(85804)
        home_team_id = self.aggregator.get_home_team_id(85804)
        away_team_id = self.aggregator.get_away_team_id(85804)

        context = CalculateContext(calculate_type=CalculateType.GAMES_COUNT)
        self.assertEqual(1, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(1, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.GAMES_COUNT, calculate_location=CalculateLocation.HOME)
        self.assertEqual(1, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.GAMES_COUNT, calculate_location=CalculateLocation.AWAY)
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(1, self.aggregator.calculate(events_df, 85804, away_team_id, context))

    def test_calculate_duration(self):
        events_df = self.aggregator.get_events(85804)
        home_team_id = self.aggregator.get_home_team_id(85804)
        away_team_id = self.aggregator.get_away_team_id(85804)

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(97, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(97, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.HOME)
        self.assertEqual(97, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.AWAY)
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(97, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   second_half=False)
        self.assertEqual(47, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(47, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.HOME,
                                   second_half=False)
        self.assertEqual(47, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.AWAY,
                                   second_half=False)
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(47, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   first_half=False)
        self.assertEqual(50, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(50, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.HOME,
                                   first_half=False)
        self.assertEqual(50, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.AWAY,
                                   first_half=False)
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(50, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   difference_from=0, difference_to=0)
        self.assertEqual(56, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(56, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.HOME,
                                   difference_from=0, difference_to=0)
        self.assertEqual(56, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.AWAY,
                                   difference_from=0, difference_to=0)
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(56, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   difference_from=0, difference_to=0, home_team_goals=0)
        self.assertEqual(46, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(46, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   minute_to=15)
        self.assertEqual(15, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(15, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   minute_from=75)
        self.assertEqual(20, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(20, self.aggregator.calculate(events_df, 85804, away_team_id, context))

    def test_calculate_duration_with_red_card_in_second_half(self):
        events_df = self.aggregator.get_events(85801)
        home_team_id = self.aggregator.get_home_team_id(85801)
        away_team_id = self.aggregator.get_away_team_id(85801)

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(95, self.aggregator.calculate(events_df, 85801, home_team_id, context))
        self.assertEqual(95, self.aggregator.calculate(events_df, 85801, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   finish_on_red_card=True)
        self.assertEqual(78, self.aggregator.calculate(events_df, 85801, home_team_id, context))
        self.assertEqual(78, self.aggregator.calculate(events_df, 85801, away_team_id, context))

    def test_calculate_duration_with_red_card_in_first_half(self):
        events_df = self.aggregator.get_events(86510)
        home_team_id = self.aggregator.get_home_team_id(86510)
        away_team_id = self.aggregator.get_away_team_id(86510)

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(95, self.aggregator.calculate(events_df, 86510, home_team_id, context))
        self.assertEqual(95, self.aggregator.calculate(events_df, 86510, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   finish_on_red_card=True)
        self.assertEqual(32, self.aggregator.calculate(events_df, 86510, home_team_id, context))
        self.assertEqual(32, self.aggregator.calculate(events_df, 86510, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.DURATION, calculate_location=CalculateLocation.TOTAL,
                                   finish_on_red_card=True, minute_from=0, minute_to=35)
        self.assertEqual(32, self.aggregator.calculate(events_df, 86510, home_team_id, context))
        self.assertEqual(32, self.aggregator.calculate(events_df, 86510, away_team_id, context))

    def test_calculate_goals(self):
        events_df = self.aggregator.get_events(85804)
        home_team_id = self.aggregator.get_home_team_id(85804)
        away_team_id = self.aggregator.get_away_team_id(85804)

        context = CalculateContext(calculate_type=CalculateType.GOALS, calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(2, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(1, self.aggregator.calculate(events_df, 85804, away_team_id, context))

    def test_calculate_goals_with_own_goals(self):
        events_df = self.aggregator.get_events(85895)
        home_team_id = self.aggregator.get_home_team_id(85895)
        away_team_id = self.aggregator.get_away_team_id(85895)

        context = CalculateContext(calculate_type=CalculateType.GOALS, calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(2, self.aggregator.calculate(events_df, 85895, home_team_id, context))
        self.assertEqual(1, self.aggregator.calculate(events_df, 85895, away_team_id, context))

    def test_calculate_xg(self):
        events_df = self.aggregator.get_events(85804)
        home_team_id = self.aggregator.get_home_team_id(85804)
        away_team_id = self.aggregator.get_away_team_id(85804)

        context = CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                   calculate_location=CalculateLocation.TOTAL, precision=3)
        self.assertEqual(0.871, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(2.407, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                   calculate_location=CalculateLocation.TOTAL, own_shots=False, precision=3)
        self.assertEqual(2.407, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(0.871, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                   calculate_location=CalculateLocation.TOTAL, max_value=0.3, precision=3)
        self.assertEqual(0.871, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(1.731, self.aggregator.calculate(events_df, 85804, away_team_id, context))

    def test_calculate_xg_with_red_cards(self):
        events_df = self.aggregator.get_events(85801)
        home_team_id = self.aggregator.get_home_team_id(85801)
        away_team_id = self.aggregator.get_away_team_id(85801)

        context = CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                   calculate_location=CalculateLocation.TOTAL, precision=3)
        self.assertEqual(1.498, self.aggregator.calculate(events_df, 85801, home_team_id, context))
        self.assertEqual(0.621, self.aggregator.calculate(events_df, 85801, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                   calculate_location=CalculateLocation.TOTAL, finish_on_red_card=True, precision=3)
        self.assertEqual(1.051, self.aggregator.calculate(events_df, 85801, home_team_id, context))
        self.assertEqual(0.621, self.aggregator.calculate(events_df, 85801, away_team_id, context))

    def test_calculate_xg_with_own_goals(self):
        events_df = self.aggregator.get_events(85895)
        home_team_id = self.aggregator.get_home_team_id(85895)
        away_team_id = self.aggregator.get_away_team_id(85895)

        context = CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                   calculate_location=CalculateLocation.TOTAL, precision=3)
        self.assertEqual(2.142, self.aggregator.calculate(events_df, 85895, home_team_id, context))
        self.assertEqual(1.779, self.aggregator.calculate(events_df, 85895, away_team_id, context))

    def test_calculate_shots_count(self):
        events_df = self.aggregator.get_events(85804)
        home_team_id = self.aggregator.get_home_team_id(85804)
        away_team_id = self.aggregator.get_away_team_id(85804)

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(12, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(18, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL, skip_penalties=True)
        self.assertEqual(12, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(17, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL, minute_from=0, minute_to=15)
        self.assertEqual(1, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(2, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL, minute_from=70)
        self.assertEqual(3, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(5, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL, difference_from=0, difference_to=0)
        self.assertEqual(7, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(10, self.aggregator.calculate(events_df, 85804, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL, difference_from=0, difference_to=0,
                                   home_team_goals=1)
        self.assertEqual(1, self.aggregator.calculate(events_df, 85804, home_team_id, context))
        self.assertEqual(0, self.aggregator.calculate(events_df, 85804, away_team_id, context))

    def test_calculate_shots_count_with_own_goals(self):
        events_df = self.aggregator.get_events(85895)
        home_team_id = self.aggregator.get_home_team_id(85895)
        away_team_id = self.aggregator.get_away_team_id(85895)

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT, calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(16, self.aggregator.calculate(events_df, 85895, home_team_id, context))
        self.assertEqual(11, self.aggregator.calculate(events_df, 85895, away_team_id, context))

    def test_calculate_shots_count_for_game_with_red_card(self):
        events_df = self.aggregator.get_events(86510)
        home_team_id = self.aggregator.get_home_team_id(86510)
        away_team_id = self.aggregator.get_away_team_id(86510)

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL)
        self.assertEqual(16, self.aggregator.calculate(events_df, 86510, home_team_id, context))
        self.assertEqual(9, self.aggregator.calculate(events_df, 86510, away_team_id, context))

        context = CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                   calculate_location=CalculateLocation.TOTAL, finish_on_red_card=True)
        self.assertEqual(0, self.aggregator.calculate(events_df, 86510, home_team_id, context))
        self.assertEqual(2, self.aggregator.calculate(events_df, 86510, away_team_id, context))

    def test_aggregate_team_statistics(self):
        events_df = self.aggregator.get_events(85804)
        home_team_id = self.aggregator.get_home_team_id(85804)
        away_team_id = self.aggregator.get_away_team_id(85804)

        home_aggregations = self.aggregator.aggregate_team_statistics(events_df, 85804, home_team_id, {
            'duration': CalculateContext(calculate_type=CalculateType.DURATION),
            'shots_count': CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                            calculate_location=CalculateLocation.HOME),
        })

        self.assertEqual(85804, home_aggregations['game_id'])
        self.assertEqual(home_team_id, home_aggregations['team_id'])
        self.assertEqual(97, home_aggregations['duration'])
        self.assertEqual(12, home_aggregations['shots_count'])

        away_aggregations = self.aggregator.aggregate_team_statistics(events_df, 85804, away_team_id, {
            'duration_home': CalculateContext(calculate_type=CalculateType.DURATION,
                                              calculate_location=CalculateLocation.HOME),
            'duration_away': CalculateContext(calculate_type=CalculateType.DURATION,
                                              calculate_location=CalculateLocation.AWAY),
            'expected_goals_home': CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                                    calculate_location=CalculateLocation.HOME, precision=3),
            'expected_goals_away': CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS,
                                                    calculate_location=CalculateLocation.AWAY, precision=3),
            'shots_count_home': CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                                 calculate_location=CalculateLocation.HOME),
            'shots_count_away': CalculateContext(calculate_type=CalculateType.SHOTS_COUNT,
                                                 calculate_location=CalculateLocation.AWAY),
        })

        self.assertEqual(85804, away_aggregations['game_id'])
        self.assertEqual(away_team_id, away_aggregations['team_id'])
        self.assertEqual(0, away_aggregations['duration_home'])
        self.assertEqual(97, away_aggregations['duration_away'])
        self.assertEqual(0, away_aggregations['expected_goals_home'])
        self.assertEqual(2.407, away_aggregations['expected_goals_away'])
        self.assertEqual(0, away_aggregations['shots_count_home'])
        self.assertEqual(18, away_aggregations['shots_count_away'])

    def test_processor(self):
        metrics_definition = {
            'expected_goals': CalculateContext(calculate_type=CalculateType.EXPECTED_GOALS, precision=3),
        }

        result_df = self.aggregator.aggregate(metrics_definition, False)

        self.assertEqual(result_df['expected_goals'][85804][14861], 0.871)
        self.assertEqual(result_df['expected_goals'][85895][6727], 1.779)


if __name__ == '__main__':
    unittest.main()
