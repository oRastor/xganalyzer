import os
import unittest
import pandas

from src.xganalyzer.final_aggregator import FinalAggregator
from src.xganalyzer.season_aggregator import SeasonAggregator, BasicSumMetric, ExpectedGaolsPer90IndexMinutesMetric, \
    AverageMetric, ExpectedGaolsPer90MinutesAverageMetric, ExpectedGaolsPerShotMetric, ExpectedGaolsPer90MinutesMetric


class TestSeasonGameAggregator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dirname = os.path.dirname(__file__)

        aggregated_season = 4922
        games_df = pandas.read_csv(os.path.join(dirname, 'data/games.csv'))
        games_df = games_df[games_df['season_id'] == aggregated_season]

        metrics_aggregations_df = pandas.read_csv(os.path.join(dirname, 'data/metrics_aggregations.csv'))

        cls.aggregator = FinalAggregator(games_df, metrics_aggregations_df)

    def test_aaa(self):
        result_df = self.aggregator.aggregate()

        key = 85892
        self.assertEqual(286, result_df.loc[key]['home_team_duration'])
        self.assertEqual(286, result_df.loc[key]['away_team_duration'])
        self.assertEqual(1.509, result_df.loc[key]['home_team_xg90'])
        self.assertEqual(1.691, result_df.loc[key]['away_team_xg90'])
        self.assertEqual(0.888, result_df.loc[key]['home_team_xga90'])
        self.assertEqual(0.634, result_df.loc[key]['away_team_xga90'])
        self.assertEqual(1.171, result_df.loc[key]['home_team_xg90index'])
        self.assertEqual(1.312, result_df.loc[key]['away_team_xg90index'])


if __name__ == '__main__':
    unittest.main()
