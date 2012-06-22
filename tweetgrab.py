import twitter
import os
from urllib2 import URLError

TWITTER_CREDS = os.path.expanduser('~/.tweetgrabgraphcreds')

CONSUMER_KEY = 'xtKjs9wudlHoA21qf0A'
CONSUMER_SECRET = '9GCetczwvsfuyYkYZJofFyPg022d9Ld3aoEu46ABQ'


def get_oauth():
    if not os.path.exists(TWITTER_CREDS):
        twitter.oauth_dance('TweetGrabGraph', CONSUMER_KEY, CONSUMER_SECRET,
                TWITTER_CREDS)
    oauth_token, oauth_secret = twitter.read_token_file(TWITTER_CREDS)
    return (oauth_token, oauth_secret)


def create_oauth():
    oauth_token, oauth_secret = get_oauth()
    return twitter.OAuth(oauth_token, oauth_secret,
            CONSUMER_KEY, CONSUMER_SECRET)


class TweetGrab(object):
    def __init__(self, screen_name, auth=None):
        if auth:
            self.tw = twitter.Twitter(auth=auth)
        else:
            self.tw = twitter.Twitter()
        self.screen_name = screen_name
        self.follower = []
        # default starting cursor is -1
        self._cursor = -1
        self.id = self.tw.users.lookup(screen_name=screen_name)[0]['id']

    def __repr__(self):
        return "TweetGrab for %s" % self.screen_name

    def __str__(self):
        limit = self.get_limit()['remaining_hits']
        return "%s, remaining limit %s" % (self.__repr__(), limit)

    def save(self, filename=None):
        if not filename:
            filename = "%s_rel.csv" % self.screen_name

        import csv
        writer = csv.writer(open(filename, 'a'))
        for follower in self.follower:
            writer.writerow((follower, self.id))

    def reset(self):
        "reset this obj status, in case of failure"
        self.follower = []
        self._cursor = -1

    def get_limit(self):
        return self.tw.account.rate_limit_status()

    def get_follower(self):
        while True:
            try:
                result = self.tw.followers.ids(
                        screen_name=self.screen_name,
                        cursor=self._cursor)
            except URLError as e:
                print e
                break

            # update follower attribute
            self.follower.extend(result['ids'])

            self._cursor = result['next_cursor']

            if self._cursor == 0:
                break

            print("continue iteration, number followers now: %s" %
                    self.get_number_follower())

    def get_number_follower(self):
        return len(self.follower)


if __name__ == '__main__':
    using_oauth = False
    while True:
        answer = raw_input('Use OAuth (y/n)? ')
        if answer == 'y':
            using_oauth = True
            break
        elif answer == 'n':
            break

    auth = None
    if using_oauth:
        get_oauth()
        auth = create_oauth()

    screen_name = raw_input('Target user screen name : ')
    twt_obj = TweetGrab(screen_name, auth=auth)
    print("fetching followers")
    twt_obj.get_follower()
    print("saving relationship to file")
    twt_obj.save()
    print("Done.")
    print twt_obj
