import billboard_scraper
import date_manager
import quote_generator
from spotipy import SpotifyOAuth, Spotify
from environs import Env
import os
import spotify_manager

env = Env()
env.read_env('.env.txt')

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
SCOPE = 'playlist-modify-private'
URL_TO_SCRAPE = os.getenv('URL_TO_SCRAPE')


date_man = date_manager.DateManager()

scraper = billboard_scraper.BillboardScraper(url='https://www.billboard.com/charts/hot-100/',
                                             user_handler=date_man
                                             )
track_list = scraper.scrape_html(tag_name='h3',
                                 class_name='a-no-trucate')
artist_list = scraper.scrape_html(tag_name='span',
                                  class_name='a-no-trucate')

artist_song_list = [{'artist': artist, 'song_title': track_list[index]}
                    for index, artist in enumerate(artist_list)]

# for item in artist_song_list:
#     print(item)


quote_generator = quote_generator.QuoteGenerator(artist_song_list)
quotes = quote_generator.generate_quotes()
sp_handler = Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path='tokens.txt'))

spotify_manager = spotify_manager.SpotifyManager(spotify_handler=sp_handler)

user_id = sp_handler.current_user()['id']

for item in quotes:
    quote = item[0]
    title = item[1].replace('%20', ' ')
    artist = item[0].replace('%20', " ")
    uri = sp_handler.search(q=quote, limit=50, type='track')
    for item in uri['tracks']['items']:
        if title in item['name']:
            print(f'Name : {item["name"]}')
            break
    else:
        print(f"No song for {title}")






