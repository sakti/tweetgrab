import twitter
import os
from urllib2 import URLError
import json
import sys
import argparse


TWITTER_CREDS = os.path.expanduser('~/.tweetgrabgraphcreds')

CONSUMER_KEY = 'xtKjs9wudlHoA21qf0A'
CONSUMER_SECRET = '9GCetczwvsfuyYkYZJofFyPg022d9Ld3aoEu46ABQ'

__version__ = 0.1

parser = argparse.ArgumentParser(
        prog='tweetgrab.py',
        description='Twitter Grabber'
    )
parser.add_argument('-oa', '--oauth',
        action='store_true',
        default=False,
        help='use oauth authentication'
    )
parser.add_argument('-u', '--user',
        action='store',
        help='user screen_name to lookup',
        required=True
    )

parser.add_argument('-c', '--command',
        action='store',
        help='command to run [info, rel]',
        required=True
    )
parser.add_argument('-v', '--version',
        action='version',
        version=__version__
    )


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

    def info(self):
        userinfo = self.tw.users.show(screen_name=self.screen_name)
        return json.dumps(userinfo, indent=4)

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
    args = parser.parse_args()
    
    auth = None

    if args.oauth:
        get_oauth()
        auth = create_oauth()

    if args.command == 'info':
        twt_obj = TweetGrab(args.user, auth=auth)
        print twt_obj.info()
    elif args.command == 'rel':
        twt_obj = TweetGrab(args.user, auth=auth)
        print("fetching followers")
        twt_obj.get_follower()
        print("saving relationship to file")
        twt_obj.save()
        print("Done.")
        print twt_obj