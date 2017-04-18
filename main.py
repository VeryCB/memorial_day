# coding: utf-8

from datetime import date

from twitter import Twitter, OAuth

from local_config import token, token_secret, consumer_key, consumer_secret


acquaintance_day = date(2010, 8, 11)
love_day = date(2011, 12, 9)
wedding_day = date(2014, 8, 15)
daughter_birthday = date(2017, 2, 6)

today = date.today()

acquaintanced = (today - acquaintance_day).days
loved = (today - love_day).days
married = (today - wedding_day).days
daughter_age = (today - daughter_birthday).days

status_tmpl = '今天是我们相识的第%s天，相爱的第%s天，喜结连理的第%s天，也是我们的女儿出生的第%s天。'  # noqa
status = status_tmpl % (acquaintanced, loved, married, daughter_age)

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
t.statuses.update(status=status)
