# pylint: disable=wildcard-import,too-many-instance-attributes,unused-wildcard-import

from datetime import datetime, timedelta, timezone
from unittest import TestCase

from pystreamapi.conditions import equal_to, not_equal_to, between, not_between
from pystreamapi.conditions.date import *


class TestDateConditionsUsingTypeDate(TestCase):

    def setUp(self):
        self.now = datetime.now()
        self.yesterday = self.now - timedelta(days=1)
        self.tomorrow = self.now + timedelta(days=1)
        self.last_week = self.now - timedelta(weeks=1)
        self.next_week = self.now + timedelta(weeks=1)
        self.last_month = (self.now.replace(day=1) - timedelta(days=1))
        self.next_month = (self.now.replace(day=25) + timedelta(days=15))
        self.last_year = self.now.replace(year=self.now.year - 1)
        self.next_year = self.now.replace(year=self.now.year + 1)
        self.now_utc = datetime.now(timezone.utc)
        self.yesterday_utc = self.now_utc - timedelta(days=1)
        self.tomorrow_utc = self.now_utc + timedelta(days=1)
        self.last_week_utc = self.now_utc - timedelta(weeks=1)
        self.next_week_utc = self.now_utc + timedelta(weeks=1)
        self.last_month_utc = (self.now_utc.replace(day=1) - timedelta(days=1))
        self.next_month_utc = (self.now_utc.replace(day=25) + timedelta(days=15))
        self.last_year_utc = self.now_utc.replace(year=self.now_utc.year - 1)
        self.next_year_utc = self.now_utc.replace(year=self.now_utc.year + 1)

    def test_before(self):
        self.assertTrue(before(self.tomorrow.date())(self.now.date()))
        self.assertFalse(before(self.yesterday.date())(self.now.date()))
        self.assertFalse(before(self.now.date())(self.now.date()))

    def test_after(self):
        self.assertTrue(after(self.yesterday.date())(self.now.date()))
        self.assertFalse(after(self.tomorrow.date())(self.now.date()))
        self.assertFalse(after(self.now.date())(self.now.date()))

    def test_before_or_equal(self):
        self.assertTrue(before_or_equal(self.tomorrow.date())(self.now.date()))
        self.assertFalse(before_or_equal(self.yesterday.date())(self.now.date()))
        self.assertTrue(before_or_equal(self.now.date())(self.now.date()))

    def test_after_or_equal(self):
        self.assertTrue(after_or_equal(self.yesterday.date())(self.now.date()))
        self.assertFalse(after_or_equal(self.tomorrow.date())(self.now.date()))
        self.assertTrue(after_or_equal(self.now.date())(self.now.date()))

    def test_equal_to(self):
        self.assertTrue(equal_to(self.now.date())(self.now.date()))
        self.assertFalse(equal_to(self.now.date())(self.yesterday.date()))

    def test_not_equal_to(self):
        self.assertTrue(not_equal_to(self.now.date())(self.yesterday.date()))
        self.assertFalse(not_equal_to(self.now.date())(self.now.date()))

    def test_between(self):
        between_func = between(self.yesterday.date(), self.tomorrow.date())
        self.assertTrue(between_func(self.now.date()))
        self.assertFalse(between_func(self.last_week.date()))
        self.assertFalse(between_func(self.next_week.date()))

    def test_not_between(self):
        not_between_func = not_between(self.yesterday.date(), self.tomorrow.date())
        self.assertFalse(not_between_func(self.now.date()))
        self.assertTrue(not_between_func(self.last_week.date()))
        self.assertTrue(not_between_func(self.next_week.date()))

    def test_between_or_equal(self):
        between_or_equal_func = between_or_equal(self.now.date(), self.tomorrow.date())
        self.assertTrue(between_or_equal_func(self.now.date()))
        self.assertTrue(between_or_equal_func(self.tomorrow.date()))
        self.assertFalse(between_or_equal_func(self.yesterday.date()))

    def test_not_between_or_equal(self):
        not_between_or_equal_func = not_between_or_equal(self.now.date(), self.tomorrow.date())
        self.assertFalse(not_between_or_equal_func(self.now.date()))
        self.assertFalse(not_between_or_equal_func(self.tomorrow.date()))
        self.assertTrue(not_between_or_equal_func(self.yesterday.date()))

    def test_today(self):
        self.assertTrue(today()(self.now.date()))
        self.assertFalse(today()(self.yesterday.date()))
        self.assertFalse(today()(self.tomorrow.date()))

    def test_today_utc(self):
        self.assertTrue(today_utc()(self.now_utc.date()))
        self.assertFalse(today_utc()(self.yesterday_utc.date()))
        self.assertFalse(today_utc()(self.tomorrow_utc.date()))

    def test_yesterday(self):
        self.assertTrue(yesterday()(self.yesterday.date()))
        self.assertFalse(yesterday()(self.now.date()))
        self.assertFalse(yesterday()(self.tomorrow.date()))

    def test_yesterday_utc(self):
        self.assertTrue(yesterday_utc()(self.yesterday_utc.date()))
        self.assertFalse(yesterday_utc()(self.now_utc.date()))
        self.assertFalse(yesterday_utc()(self.tomorrow_utc.date()))

    def test_tomorrow(self):
        self.assertTrue(tomorrow()(self.tomorrow.date()))
        self.assertFalse(tomorrow()(self.now.date()))
        self.assertFalse(tomorrow()(self.yesterday.date()))

    def test_tomorrow_utc(self):
        self.assertTrue(tomorrow_utc()(self.tomorrow_utc.date()))
        self.assertFalse(tomorrow_utc()(self.now_utc.date()))
        self.assertFalse(tomorrow_utc()(self.yesterday_utc.date()))

    def test_this_week(self):
        self.assertTrue(this_week()(self.now.date()))
        self.assertFalse(this_week()(self.last_week.date()))
        self.assertFalse(this_week()(self.next_week.date()))

    def test_this_week_utc(self):
        self.assertTrue(this_week_utc()(self.now_utc.date()))
        self.assertFalse(this_week_utc()(self.last_week_utc.date()))
        self.assertFalse(this_week_utc()(self.next_week_utc.date()))

    def test_last_week(self):
        self.assertTrue(last_week()(self.last_week.date()))
        self.assertFalse(last_week()(self.now.date()))
        self.assertFalse(last_week()(self.next_week.date()))

    def test_last_week_utc(self):
        self.assertTrue(last_week_utc()(self.last_week_utc.date()))
        self.assertFalse(last_week_utc()(self.now_utc.date()))
        self.assertFalse(last_week_utc()(self.next_week_utc.date()))

    def test_next_week(self):
        self.assertTrue(next_week()(self.next_week.date()))
        self.assertFalse(next_week()(self.now.date()))
        self.assertFalse(next_week()(self.last_week.date()))

    def test_next_week_utc(self):
        self.assertTrue(next_week_utc()(self.next_week_utc.date()))
        self.assertFalse(next_week_utc()(self.now_utc.date()))
        self.assertFalse(next_week_utc()(self.last_week_utc.date()))

    def test_this_month(self):
        self.assertTrue(this_month()(self.now.date()))
        self.assertFalse(this_month()(self.last_month.date()))
        self.assertFalse(this_month()(self.next_month.date()))

    def test_this_month_utc(self):
        self.assertTrue(this_month_utc()(self.now_utc.date()))
        self.assertFalse(this_month_utc()(self.last_month_utc.date()))
        self.assertFalse(this_month_utc()(self.next_month_utc.date()))

    def test_last_month(self):
        self.assertTrue(last_month()(self.last_month.date()))
        self.assertFalse(last_month()(self.now.date()))
        self.assertFalse(last_month()(self.next_month.date()))

    def test_last_month_utc(self):
        self.assertTrue(last_month_utc()(self.last_month_utc.date()))
        self.assertFalse(last_month_utc()(self.now_utc.date()))
        self.assertFalse(last_month_utc()(self.next_month_utc.date()))

    def test_next_month(self):
        self.assertTrue(next_month()(self.next_month.date()))
        self.assertFalse(next_month()(self.now.date()))
        self.assertFalse(next_month()(self.last_month.date()))

    def test_next_month_utc(self):
        self.assertTrue(next_month_utc()(self.next_month_utc.date()))
        self.assertFalse(next_month_utc()(self.now_utc.date()))
        self.assertFalse(next_month_utc()(self.last_month_utc.date()))

    def test_this_year(self):
        self.assertTrue(this_year()(self.now.date()))
        self.assertFalse(this_year()(self.last_year.date()))
        self.assertFalse(this_year()(self.next_year.date()))

    def test_this_year_utc(self):
        self.assertTrue(this_year_utc()(self.now_utc.date()))
        self.assertFalse(this_year_utc()(self.last_year_utc.date()))
        self.assertFalse(this_year_utc()(self.next_year_utc.date()))

    def test_last_year(self):
        self.assertTrue(last_year()(self.last_year.date()))
        self.assertFalse(last_year()(self.now.date()))
        self.assertFalse(last_year()(self.next_year.date()))

    def test_last_year_utc(self):
        self.assertTrue(last_year_utc()(self.last_year_utc.date()))
        self.assertFalse(last_year_utc()(self.now_utc.date()))
        self.assertFalse(last_year_utc()(self.next_year_utc.date()))

    def test_next_year(self):
        self.assertTrue(next_year()(self.next_year.date()))
        self.assertFalse(next_year()(self.now.date()))
        self.assertFalse(next_year()(self.last_year.date()))

    def test_next_year_utc(self):
        self.assertTrue(next_year_utc()(self.next_year_utc.date()))
        self.assertFalse(next_year_utc()(self.now_utc.date()))
        self.assertFalse(next_year_utc()(self.last_year_utc.date()))
