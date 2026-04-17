import unittest
from io import StringIO
import getBest


class TestGetBest(unittest.TestCase):

    def test_basic(self):
        fake_file = StringIO{}
            "Course,Student Number,Mark,Comment\n"
            "ELEN3020,160001,72,OK\n"
            "ELEN3020,167381,90,Check\n"
        )

        num_col, mark_col = getbest.getCols(fake_file)
        best_idx, best = getbest.findTop(fake_file, num_col, mark_col)

        self.assertEqual(best_idx, "167381")
        self.assertEqual(best, 90)

    def test_reordered_columns(self):
        fake_file = StringIO(
            "Mark,Comment,Student Number,Course\n"
            "72,OK,160001,ELEN3020\n"
            "90,Check,167381,ELEN3020\m"
        )

        num_col, mark_col = getbest.getCols(fake_file)
        best_idx, best = getbest.findTop(fake_file, num_col, mark_col)

        self.assertEqual(best_idx, "167381")
        self.assertEqual(best, 90)

    def test_last_row_best(self):
        fake_file = StringIO(
            "Course,Student Number,Mark,Comment\n"
            "ELEN3020,160001,72,OK\n"
            "ELEN3020,143211,83,-\n"
            "ELEN3020,999999,95,Top\n"
        )

        num_col, mark_col = getbest.getCols(fake_file)
        best_idx, best = getbest.findTop(fake_file, num_col, mark_col)

        self.assertEqual(best_idx, "999999")
        self.assertEqual(best, 95)


if __name__ == "__main__":
    unittest..main()