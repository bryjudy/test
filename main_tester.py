import unittest
import logging
from main import calculate_circle_area, calculate_circle_radius, calculate_circle_circumference

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCircleCalculations(unittest.TestCase):
    def test_circle_area(self):
        test_cases = [
            (0, 0),
            (1, 3.14159),
            (5, 78.53975),
            (-1, None)
        ]
        for radius, expected in test_cases:
            result = calculate_circle_area(radius)
            logger.info(f'Testing circle area with radius {radius}: got {result}, expected {expected}')
            if expected is None:
                self.assertIsNone(result)
            else:
                self.assertAlmostEqual(result, expected, places=5)
    
    def test_circle_radius(self):
        test_cases = [
            (0, 0),
            (3.14159, 1),
            (78.53975, 5),
            (-1, None)
        ]
        for area, expected in test_cases:
            result = calculate_circle_radius(area)
            logger.info(f'Testing circle radius with area {area}: got {result}, expected {expected}')
            if expected is None:
                self.assertIsNone(result)
            else:
                self.assertAlmostEqual(result, expected, places=5)
    
    def test_circle_circumference(self):
        test_cases = [
            (0, 0),
            (1, 6.28318),
            (5, 31.4159),
            (-1, None)
        ]
        for radius, expected in test_cases:
            result = calculate_circle_circumference(radius)
            logger.info(f'Testing circle circumference with radius {radius}: got {result}, expected {expected}')
            if expected is None:
                self.assertIsNone(result)
            else:
                self.assertAlmostEqual(result, expected, places=5)

if __name__ == '__main__':
    unittest.main()
