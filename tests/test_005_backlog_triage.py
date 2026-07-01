import unittest

from portfolio_drawdown_sentinel.models import Record
from portfolio_drawdown_sentinel.scoring import score_record


class DepthCheck5(unittest.TestCase):
    def test_005_backlog_triage(self):
        record = Record(id="position-005", exposure=93827, signal=0.857, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
