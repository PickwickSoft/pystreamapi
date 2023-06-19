from datetime import datetime, timedelta, timezone
from unittest import TestCase


class DateTest(TestCase):

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