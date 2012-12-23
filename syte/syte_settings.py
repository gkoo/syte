# -*- coding: utf-8 -*-

DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.1'

BLOG_PLATFORM = 'wordpress'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'superkerplunk.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'uVOEfuZcwxkp6Mls4wP78t5DVicSTxtE5c50nLWHJZWHGAKk2P'

#Blog Integration: Wordpress
WORDPRESS_BLOG_URL = 'gordonkoo.wordpress.com'
WORDPRESS_API_URL = 'https://public-api.wordpress.com/rest/v1/sites/{0}'.format(WORDPRESS_BLOG_URL)

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = False
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = 'OGnbxQEGrpQaUCAXlPJ7YQ'
TWITTER_CONSUMER_SECRET = 'XF8ERdmtmSOaep0QnHDkfSLgVtJCaVMjqZzPL2sxh0'
TWITTER_USER_KEY = '167215657-CyjyfVoLL0ZmUODJtME97kaTBCjNz9WiJ8vLI9k7'
TWITTER_USER_SECRET = 'ZgbgAonhT3jPNJYxL5gkc34zYg4ePPYMjAfPiKdqA'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = 'dc10b34d0222eb486194a35c4d9e8d74c6747fa0'

GITHUB_OAUTH_ENABLED = False
GITHUB_CLIENT_ID = 'e901c0b9ead3012b1172'
GITHUB_CLIENT_SECRET = '85b867f06ba6448e17ef8a23c6bce0b54bc17f54'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '9229265.4cb4b52.940114e9947242f28edb9f8a6183d0df'
INSTAGRAM_USER_ID = 'superkerplunk'

INSTAGRAM_OAUTH_ENABLED = True
INSTAGRAM_CLIENT_ID = '4cb4b52500d847b0a05238ab87d1de5d'
INSTAGRAM_CLIENT_SECRET = '78834d05da614dbfba4ececb55a4fab1'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = False
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = '[ENTER FOURSQUARE ACCESS TOKEN HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = True
FOURSQUARE_CLIENT_ID = '[ENTER FOURSQUARE CLIENT_ID HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_CLIENT_SECRET = '[ENTER FOURSQUARE CLIENT_SECRET HERE, SEE FOURSQUARE SETUP INSTRUCTIONS]'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#Woopra
WOOPRA_TRACKING_DOMAIN = ''
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False



#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = ''


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = False
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '[ENTER LASTFM API_KEY HERE, SEE LASTFM SETUP INSTRUCTIONS]'

#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = False
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = '[ENTER SOUNDCLOUD APPLICATION CLIENT_ID HERE]'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = False
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False

#Tent.io Integration
TENT_INTEGRATION_ENABLED = False
TENT_ENTITY_URI = '[ENTER YOUR ENTITY URI HERE] ex. https://yourname.tent.is'
TENT_FEED_URL = '[ENTER A URL TO YOUR FEED] ex. https://yourname.tent.is'




if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://sleepy-plains-7049.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
