import os
import unittest
import pandas
from src.xganalyzer.season_aggregator import SeasonAggregator, BasicSumMetric, ExpectedGaolsPer90IndexMinutesMetric, \
    AverageMetric, ExpectedGaolsPer90MinutesAverageMetric, ExpectedGaolsPerShotMetric, ExpectedGaolsPer90MinutesMetric


class TestSeasonGameAggregator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dirname = os.path.dirname(__file__)

        aggregated_season = 4922
        games_df = pandas.read_csv(os.path.join(dirname, 'data/games.csv'))
        games_df = games_df[games_df['season_id'] == aggregated_season]

        game_aggregations_df = pandas.read_csv(os.path.join(dirname, 'data/game_aggregations.csv'))

        cls.aggregator = SeasonAggregator(games_df, game_aggregations_df)

    def test_aaa(self):
        result_df = self.aggregator.aggregate({
            'finished_games': BasicSumMetric('games'),
            'duration': BasicSumMetric('duration'),
            'duration_avg': AverageMetric('duration', 3),
            'xg90': ExpectedGaolsPer90MinutesMetric('expected_goals', 'duration', 3),
            'xga90': ExpectedGaolsPer90MinutesMetric('expected_goals_against', 'duration', 3),
            'xgsh': ExpectedGaolsPerShotMetric('expected_goals', 'shots_count', 3),
            'xgash': ExpectedGaolsPerShotMetric('expected_goals_against', 'shots_against_count', 3),
            'xg90index': ExpectedGaolsPer90IndexMinutesMetric('expected_goals', 'duration', 3),
            'xga90index': ExpectedGaolsPer90IndexMinutesMetric('expected_goals_against', 'duration', 3),
            'xg90avg': ExpectedGaolsPer90MinutesAverageMetric('expected_goals', 'duration', 3),
        })
        result_df.to_csv('1.csv')
        key = (85892, 6719)
        self.assertEqual(3, result_df.loc[key]['finished_games'])
        self.assertEqual(286, result_df.loc[key]['duration'])
        self.assertEqual(285.8, result_df.loc[key]['duration_avg'])
        self.assertEqual(1.691, result_df.loc[key]['xg90'])
        self.assertEqual(0.634, result_df.loc[key]['xga90'])
        self.assertEqual(0.141, result_df.loc[key]['xgsh'])
        self.assertEqual(0.058, result_df.loc[key]['xgash'])
        self.assertEqual(1.312, result_df.loc[key]['xg90index'])
        self.assertEqual(0.492, result_df.loc[key]['xga90index'])
        self.assertEqual(1.289, result_df.loc[key]['xg90avg'])


if __name__ == '__main__':
    unittest.main()
