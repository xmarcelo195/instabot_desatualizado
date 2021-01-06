# import random
from instapy import InstaPy
from instapy import smart_run
# from test import likar

# login credentials
insta_username = 'gordice.gourmet'
insta_password = ''

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

# likar = likar()

users_like_me = ['tudogostosooficial']

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True, max_followers=5000)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)
    session.set_user_interact(amount=2,
                              percentage=70,
                              randomize=True,
                              media='Photo')

    # activity
    session.foll
