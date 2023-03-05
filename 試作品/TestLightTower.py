import unittest

class TestLightTower(unittest.TestCase):
    def test_apply_buff_no_targets(self):
        lt = LightTower((0, 0), 10, 1, (255, 255, 255, 255))
        self.assertEqual(lt.apply_buff([]), [])

    def test_apply_buff_with_targets(self):
        lt = LightTower((0, 0), 10, 1, (255, 255, 255, 255))
        targets = [(5, 5, 1, (0, 0, 0, 255)), (15, 15, 1, (0, 0, 0, 255))]
        expected = [(5, 5, 1, (255, 255, 255, 255)), (15, 15, 1, (0, 0, 0, 255))]
        self.assertEqual(lt.apply_buff(targets), expected)

    def test_apply_buff_within_range(self):
        lt = LightTower((0, 0), 10, 1, (255, 255, 255, 255))
        targets = [(5, 5, 1, (0, 0, 0, 255)), (15, 15, 1, (0, 0, 0, 255))]
        expected = [(5, 5, 1, (255, 255, 255, 255)), (15, 15, 1, (0, 0, 0, 255))]
        self.assertEqual(lt.apply_buff(targets), expected)

    def test_apply_buff_out_of_range(self):
        lt = LightTower((0, 0), 10, 1, (255, 255, 255, 255))
        targets = [(20, 20,
