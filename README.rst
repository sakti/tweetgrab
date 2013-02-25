tweetgrab
=========

Grabbing Twitter Information


Requirements
------------

- python ``twitter`` module
  ::

      pip install twitter



Usage
-----

Get user relationship list (csv format)

::

    $ python tweetgrab.py
    Use OAuth (y/n)? y
    Target user screen name : saktidc
    fetching followers
    saving relationship to file
    Done.
    TweetGrab for saktidc, remaining limit 346

    $ view saktidc_rel.csv

Fetch user info (json format)

::

    $ python tweetgrab.py saktidc
    Use OAuth (y/n)? y
    {
    "follow_request_sent": false, 
    "profile_use_background_image": true, 
    "time_zone": "Jakarta", 
    "id": 20506172, 
    "description": "Pythonistas", 
    "verified": false, 
    "profile_image_url_https": "https://si0.twimg.com/profile_images/925827134/60565d77c757412d4d0d4ea36363fb7b_normal.jpeg", 
    "profile_sidebar_fill_color": "EFEFEF", 
    "is_translator": false, 
    "geo_enabled": true, 
    "profile_text_color": "333333", 
    "followers_count": 174, 
    "protected": false, 
    "id_str": "20506172", 
    "default_profile_image": false, 
    "listed_count": 8, 
    "status": {
        "favorited": false, 
        "contributors": null, 
        "truncated": false, 
        "text": "Cobra tweet", 
        "created_at": "Mon Feb 25 03:54:04 +0000 2013", 
        "retweeted": false, 
        "in_reply_to_status_id_str": null, 
        "coordinates": {
            "type": "Point", 
            "coordinates": [
                106.8014642, 
                -6.2028552
            ]
        }, 
        "in_reply_to_user_id_str": null, 
        "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", 
        "in_reply_to_status_id": null, 
        "in_reply_to_screen_name": null, 
        "id_str": "305888365134348288", 
        "place": {
            "full_name": "Kebayoran Lama, Jakarta Selatan", 
            "url": "http://api.twitter.com/1/geo/id/d74066a958870db1.json", 
            "country": "Indonesia", 
            "place_type": "city", 
            "bounding_box": {
                "type": "Polygon", 
                "coordinates": [
                    [
                        [
                            106.770437, 
                            -6.297602
                        ], 
                        [
                            106.805699, 
                            -6.297602
                        ], 
                        [
                            106.805699, 
                            -6.202102
                        ], 
                        [
                            106.770437, 
                            -6.202102
                        ]
                    ]
                ]
            }, 
            "country_code": "ID", 
            "attributes": {}, 
            "id": "d74066a958870db1", 
            "name": "Kebayoran Lama"
        }, 
        "retweet_count": 0, 
        "geo": {
            "type": "Point", 
            "coordinates": [
                -6.2028552, 
                106.8014642
            ]
        }, 
        "id": 305888365134348288, 
        "in_reply_to_user_id": null
    }, 
    "utc_offset": 25200, 
    "statuses_count": 636, 
    "profile_background_color": "131516", 
    "friends_count": 320, 
    "profile_link_color": "009999", 
    "profile_image_url": "http://a0.twimg.com/profile_images/925827134/60565d77c757412d4d0d4ea36363fb7b_normal.jpeg", 
    "notifications": false, 
    "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme14/bg.gif", 
    "profile_background_image_url": "http://a0.twimg.com/images/themes/theme14/bg.gif", 
    "screen_name": "saktidc", 
    "lang": "en", 
    "profile_background_tile": true, 
    "favourites_count": 11, 
    "name": "Sakti Dwi Cahyono", 
    "url": "http://saktidwicahyono.name", 
    "created_at": "Tue Feb 10 10:57:29 +0000 2009", 
    "contributors_enabled": false, 
    "location": "Bandung, Indonesia", 
    "profile_sidebar_border_color": "EEEEEE", 
    "default_profile": false, 
    "following": false


Next Milestones
---------------

- Add all basic information for twitter account not only followers
- Task can be distributed into multiple host (using zerorpc)
- Using a database system
