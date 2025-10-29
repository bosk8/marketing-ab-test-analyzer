"""
Unit tests for A/B test statistical functions.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from abtest import ztest_two_prop, power, load_aggregated_data, load_row_level_data
import numpy as np


class TestZTestTwoProp(unittest.TestCase):
    
    def test_basic_ztest(self):
        """Test basic z-test calculation."""
        result = ztest_two_prop(123, 5000, 155, 5000)
        
        self.assertIn('z', result)
        self.assertIn('p', result)
        self.assertIn('lift', result)
        self.assertIn('ci', result)
        
        self.assertIsInstance(result['z'], float)
        self.assertIsInstance(result['p'], float)
        self.assertIsInstance(result['lift'], float)
        self.assertIsInstance(result['ci'], tuple)
        self.assertEqual(len(result['ci']), 2)
        
        # Check lift is positive when B has higher conversion
        self.assertGreater(result['lift'], 0)
        # Check CI is a tuple of two floats
        self.assertIsInstance(result['ci'][0], float)
        self.assertIsInstance(result['ci'][1], float)
    
    def test_custom_alpha(self):
        """Test z-test with custom alpha."""
        result_05 = ztest_two_prop(100, 1000, 120, 1000, alpha=0.05)
        result_01 = ztest_two_prop(100, 1000, 120, 1000, alpha=0.01)
        
        # With smaller alpha, CI should be wider
        ci_width_05 = result_05['ci'][1] - result_05['ci'][0]
        ci_width_01 = result_01['ci'][1] - result_01['ci'][0]
        self.assertGreater(ci_width_01, ci_width_05)
    
    def test_invalid_inputs(self):
        """Test error handling for invalid inputs."""
        with self.assertRaises(ValueError):
            ztest_two_prop(-1, 100, 50, 100)
        
        with self.assertRaises(ValueError):
            ztest_two_prop(100, 0, 50, 100)
        
        with self.assertRaises(ValueError):
            ztest_two_prop(150, 100, 50, 100)  # success > total
    
    def test_equal_proportions(self):
        """Test when proportions are equal."""
        result = ztest_two_prop(100, 1000, 100, 1000)
        self.assertAlmostEqual(result['lift'], 0.0, places=10)
        self.assertGreater(result['p'], 0.05)  # Should not be significant


class TestPower(unittest.TestCase):
    
    def test_basic_power(self):
        """Test basic power calculation."""
        power_val = power(5000, 5000, 0.0246, min_detectable_diff=0.02)
        
        self.assertIsInstance(power_val, float)
        self.assertGreaterEqual(power_val, 0)
        self.assertLessEqual(power_val, 1)
    
    def test_power_with_different_mde(self):
        """Test power changes with MDE."""
        power_small = power(1000, 1000, 0.05, min_detectable_diff=0.01)
        power_large = power(1000, 1000, 0.05, min_detectable_diff=0.05)
        
        # Larger MDE should be easier to detect (higher power)
        self.assertGreater(power_large, power_small)
    
    def test_invalid_inputs(self):
        """Test error handling for invalid inputs."""
        with self.assertRaises(ValueError):
            power(0, 1000, 0.05)
        
        with self.assertRaises(ValueError):
            power(1000, 1000, 1.5)  # p_control > 1


class TestDataLoading(unittest.TestCase):
    
    def test_load_aggregated_data(self):
        """Test loading aggregated data."""
        # Create temporary CSV file
        import tempfile
        import pandas as pd
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("group,success,total\n")
            f.write("A,123,5000\n")
            f.write("B,155,5000\n")
            temp_path = f.name
        
        try:
            success_a, total_a, success_b, total_b = load_aggregated_data(temp_path)
            
            self.assertEqual(success_a, 123)
            self.assertEqual(total_a, 5000)
            self.assertEqual(success_b, 155)
            self.assertEqual(total_b, 5000)
        finally:
            os.unlink(temp_path)
    
    def test_load_row_level_data(self):
        """Test loading and aggregating row-level data."""
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("user_id,group,converted\n")
            f.write("u1,A,0\n")
            f.write("u2,A,1\n")
            f.write("u3,B,1\n")
            f.write("u4,B,1\n")
            temp_path = f.name
        
        try:
            success_a, total_a, success_b, total_b = load_row_level_data(temp_path)
            
            self.assertEqual(success_a, 1)  # 1 conversion out of 2
            self.assertEqual(total_a, 2)
            self.assertEqual(success_b, 2)  # 2 conversions out of 2
            self.assertEqual(total_b, 2)
        finally:
            os.unlink(temp_path)
    
    def test_load_missing_file(self):
        """Test error handling for missing file."""
        with self.assertRaises(FileNotFoundError):
            load_aggregated_data("nonexistent_file.csv")


if __name__ == '__main__':
    unittest.main()

