# pylint: disable=wildcard-import,too-many-instance-attributes,unused-wildcard-import
from _conditions.date_test import DateTest
from pystreamapi.conditions import equal_to, not_equal_to, between, not_between
from pystreamapi.conditions.date import *


class TestDateConditions(DateTest):

    def test_before(self):
        self.assertTrue(before(self.tomorrow)(self.now))
        self.assertFalse(before(self.yesterday)(self.now))
        self.assertFalse(before(self.now)(self.now))

    def test_after(self):
        self.assertTrue(after(self.yesterday)(self.now))
        self.assertFalse(after(self.tomorrow)(self.now))
        self.assertFalse(after(self.now)(self.now))

    def test_before_or_equal(self):
        self.assertTrue(before_or_equal(self.tomorrow)(self.now))
        self.assertFalse(before_or_equal(self.yesterday)(self.now))
        self.assertTrue(before_or_equal(self.now)(self.now))

    def test_after_or_equal(self):
        self.assertTrue(after_or_equal(self.yesterday)(self.now))
        self.assertFalse(after_or_equal(self.tomorrow)(self.now))
        self.assertTrue(after_or_equal(self.now)(self.now))

    def test_equal_to(self):
        self.assertTrue(equal_to(self.now)(self.now))
        self.assertFalse(equal_to(self.now)(self.yesterday))

    def test_not_equal_to(self):
        self.assertTrue(not_equal_to(self.now)(self.yesterday))
        self.assertFalse(not_equal_to(self.now)(self.now))

    def test_between(self):
        between_func = between(self.yesterday, self.tomorrow)
        self.assertTrue(between_func(self.now))
        self.assertFalse(between_func(self.last_week))
        self.assertFalse(between_func(self.next_week))

    def test_not_between(self):
        not_between_func = not_between(self.yesterday, self.tomorrow)
        self.assertFalse(not_between_func(self.now))
        self.assertTrue(not_between_func(self.last_week))
        self.assertTrue(not_between_func(self.next_week))

    def test_between_or_equal(self):
        between_or_equal_func = between_or_equal(self.now, self.tomorrow)
        self.assertTrue(between_or_equal_func(self.now))
        self.assertTrue(between_or_equal_func(self.tomorrow))
        self.assertFalse(between_or_equal_func(self.yesterday))

    def test_not_between_or_equal(self):
        not_between_or_equal_func = not_between_or_equal(self.now, self.tomorrow)
        self.assertFalse(not_between_or_equal_func(self.now))
        self.assertFalse(not_between_or_equal_func(self.tomorrow))
        self.assertTrue(not_between_or_equal_func(self.yesterday))

    def test_today(self):
        self.assertTrue(today()(self.now))
        self.assertFalse(today()(self.yesterday))
        self.assertFalse(today()(self.tomorrow))

    def test_today_utc(self):
        self.assertTrue(today_utc()(self.now_utc))
        self.assertFalse(today_utc()(self.yesterday_utc))
        self.assertFalse(today_utc()(self.tomorrow_utc))

    def test_yesterday(self):
        self.assertTrue(yesterday()(self.yesterday))
        self.assertFalse(yesterday()(self.now))
        self.assertFalse(yesterday()(self.tomorrow))

    def test_yesterday_utc(self):
        self.assertTrue(yesterday_utc()(self.yesterday_utc))
        self.assertFalse(yesterday_utc()(self.now_utc))
        self.assertFalse(yesterday_utc()(self.tomorrow_utc))

    def test_tomorrow(self):
        self.assertTrue(tomorrow()(self.tomorrow))
        self.assertFalse(tomorrow()(self.now))
        self.assertFalse(tomorrow()(self.yesterday))

    def test_tomorrow_utc(self):
        self.assertTrue(tomorrow_utc()(self.tomorrow_utc))
        self.assertFalse(tomorrow_utc()(self.now_utc))
        self.assertFalse(tomorrow_utc()(self.yesterday_utc))

    def test_this_week(self):
        self.assertTrue(this_week()(self.now))
        self.assertFalse(this_week()(self.last_week))
        self.assertFalse(this_week()(self.next_week))

    def test_this_week_utc(self):
        self.assertTrue(this_week_utc()(self.now_utc))
        self.assertFalse(this_week_utc()(self.last_week_utc))
        self.assertFalse(this_week_utc()(self.next_week_utc))

    def test_last_week(self):
        self.assertTrue(last_week()(self.last_week))
        self.assertFalse(last_week()(self.now))
        self.assertFalse(last_week()(self.next_week))

    def test_last_week_utc(self):
        self.assertTrue(last_week_utc()(self.last_week_utc))
        self.assertFalse(last_week_utc()(self.now_utc))
        self.assertFalse(last_week_utc()(self.next_week_utc))

    def test_next_week(self):
        self.assertTrue(next_week()(self.next_week))
        self.assertFalse(next_week()(self.now))
        self.assertFalse(next_week()(self.last_week))

    def test_next_week_utc(self):
        self.assertTrue(next_week_utc()(self.next_week_utc))
        self.assertFalse(next_week_utc()(self.now_utc))
        self.assertFalse(next_week_utc()(self.last_week_utc))

    def test_this_month(self):
        self.assertTrue(this_month()(self.now))
        self.assertFalse(this_month()(self.last_month))
        self.assertFalse(this_month()(self.next_month))

    def test_this_month_utc(self):
        self.assertTrue(this_month_utc()(self.now_utc))
        self.assertFalse(this_month_utc()(self.last_month_utc))
        self.assertFalse(this_month_utc()(self.next_month_utc))

    def test_last_month(self):
        self.assertTrue(last_month()(self.last_month))
        self.assertFalse(last_month()(self.now))
        self.assertFalse(last_month()(self.next_month))

    def test_last_month_utc(self):
        self.assertTrue(last_month_utc()(self.last_month_utc))
        self.assertFalse(last_month_utc()(self.now_utc))
        self.assertFalse(last_month_utc()(self.next_month_utc))

    def test_next_month(self):
        self.assertTrue(next_month()(self.next_month))
        self.assertFalse(next_month()(self.now))
        self.assertFalse(next_month()(self.last_month))

    def test_next_month_utc(self):
        self.assertTrue(next_month_utc()(self.next_month_utc))
        self.assertFalse(next_month_utc()(self.now_utc))
        self.assertFalse(next_month_utc()(self.last_month_utc))

    def test_this_year(self):
        self.assertTrue(this_year()(self.now))
        self.assertFalse(this_year()(self.last_year))
        self.assertFalse(this_year()(self.next_year))

    def test_this_year_utc(self):
        self.assertTrue(this_year_utc()(self.now_utc))
        self.assertFalse(this_year_utc()(self.last_year_utc))
        self.assertFalse(this_year_utc()(self.next_year_utc))

    def test_last_year(self):
        self.assertTrue(last_year()(self.last_year))
        self.assertFalse(last_year()(self.now))
        self.assertFalse(last_year()(self.next_year))

    def test_last_year_utc(self):
        self.assertTrue(last_year_utc()(self.last_year_utc))
        self.assertFalse(last_year_utc()(self.now_utc))
        self.assertFalse(last_year_utc()(self.next_year_utc))

    def test_next_year(self):
        self.assertTrue(next_year()(self.next_year))
        self.assertFalse(next_year()(self.now))
        self.assertFalse(next_year()(self.last_year))

    def test_next_year_utc(self):
        self.assertTrue(next_year_utc()(self.next_year_utc))
        self.assertFalse(next_year_utc()(self.now_utc))
        self.assertFalse(next_year_utc()(self.last_year_utc))
