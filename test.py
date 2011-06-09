#!/usr/bin/env python

"""Unit tests for the USA Today Census API."""

import unittest

from mock import Mock

from usa_today import usa_today
from usa_today import Census


def set_up_method_tests():
    """Cut down on boilerplate setup testing code."""
    usa_today.API_KEY = 'my_fake_api_key'
    usa_today.urlopen = Mock()
    usa_today.json = Mock()


def called_url():
    """Test what URL was called through the mocked urlopen."""
    url = usa_today.urlopen.call_args[0][0]
    return url


class TestCensusInitialization(unittest.TestCase):

    def setUp(self):
        usa_today.API_KEY = 'my_fake_api_key'

    def test_Census_intialized_with_api_key(self):
        census = Census('my_api_key')
        self.assertEquals(census.api_key, 'my_api_key')

    def test_Census_initialized_without_api_key(self):
        census = Census()
        self.assertEquals(census.api_key, 'my_fake_api_key')


class TestApiMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_api_method_fails(self):
        self.assertRaises(TypeError, Census().api)

    def test_api_method_with_locations_arg(self):
        Census().api('locations')
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'locations?api_key=my_fake_api_key')
        self.assertEquals(url, expected_url)

    def test_api_method_with_multiple_args(self):
        Census().api('testing', hello='world')
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'testing?api_key=my_fake_api_key&hello=world')
        self.assertEquals(url, expected_url)

    def test_api_method_with_new_api_key(self):
        Census('new_api_key').api('testing', hello='world')
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'testing?api_key=new_api_key&hello=world')
        self.assertEquals(url, expected_url)


class TestLocationMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_locations_method_url(self):
        Census().locations()
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'locations?api_key=my_fake_api_key')
        self.assertEquals(url, expected_url)

    def test_locations_method_with_kwargs(self):
        Census().locations(hello='world')
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'locations?api_key=my_fake_api_key&hello=world')
        self.assertEquals(url, expected_url)


class TestEthnicityMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_ethnicity_method_url(self):
        Census().ethnicity()
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'ethnicity?api_key=my_fake_api_key')
        self.assertEquals(url, expected_url)


class TestHousingMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_housing_method_url(self):
        Census().housing()
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'ethnicity?api_key=my_fake_api_key')
        self.assertEquals(url, expected_url)


class TestPopulationMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_housing_method_url(self):
        Census().population()
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'population?api_key=my_fake_api_key')
        self.assertEquals(url, expected_url)


class TestRaceMethod(unittest.TestCase):

    def setUp(self):
        set_up_method_tests()

    def test_empty_housing_method_url(self):
        Census().race()
        url = called_url()
        expected_url = ('http://api.usatoday.com/open/census/'
                        'race?api_key=my_fake_api_key')
        self.assertEquals(url, expected_url)


if __name__ == '__main__':
    unittest.main()