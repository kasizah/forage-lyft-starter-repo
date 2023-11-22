import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        self.assertTrue(CapuletEngine(30001, 0).needs_service())

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(CapuletEngine(24000, 12).needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        self.assertTrue(WilloughbyEngine(62000, 0).needs_service())

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(WilloughbyEngine(40000, 0).needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        self.assertTrue(SternmanEngine(True).needs_service())

    def test_engine_should_not_be_serviced(self):
        self.assertFalse(SternmanEngine(False).needs_service())