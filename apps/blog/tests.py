import datetime as dt

from django.test import TestCase
from django.utils import timezone as tz

from .models import Blog


class BlogTestMethod(TestCase):

    def test_is_published_today_with_future_time(self):
        today = dt.datetime.now() + dt.timedelta(minutes=5)

        date = today.date()
        time = today.time()

        blog_1 = Blog(pub_date=date, pub_time=time, is_pub=True)
        blog_2 = Blog(pub_date=date, pub_time=time, is_pub=False)

        self.assertIs(blog_1.is_published(), False)
        self.assertIs(blog_2.is_published(), False)

    def test_is_published_today_with_past_time(self):
        today = dt.datetime.now() - dt.timedelta(minutes=5)

        date = today.date()
        time = today.time()

        blog_1 = Blog(pub_date=date, pub_time=time, is_pub=True)
        blog_2 = Blog(pub_date=date, pub_time=time, is_pub=False)

        self.assertIs(blog_1.is_published(), True)
        self.assertIs(blog_2.is_published(), False)
