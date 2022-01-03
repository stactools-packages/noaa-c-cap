import unittest

import stactools.noaa_c_cap


class TestModule(unittest.TestCase):

    def test_version(self):
        self.assertIsNotNone(stactools.noaa_c_cap.__version__)
