import billboard_scraper
import date_manager
import quote_generator
from spotipy import SpotifyOAuth, Spotify
from environs import Env
import os
import spotify_manager

#
env = Env()
env.read_env('.env.txt')

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
SCOPE = 'playlist-modify-private'
URL_TO_SCRAPE = os.getenv('URL_TO_SCRAPE')

# scrape the website to get track titles and artist names.
user_handler = date_manager.DateManager()
billboard_scraper = billboard_scraper.BillboardScraper(URL_TO_SCRAPE,
                                                       user_handler)
# get the name and the description of the playlist being created
playlist_data = user_handler.get_playlist_details()

track_list = billboard_scraper.scrape_html(tag_name='h3',
                                           class_name='a-no-trucate')
artist_list = billboard_scraper.scrape_html(tag_name='span',
                                            class_name='a-no-trucate')

artist_song_list = [{'artist': artist, 'song_title': track_list[index]}
                    for index, artist in enumerate(artist_list)]

# generate quotes which will be used as quotes for spotify search api
# to get uri of particular track
quote_generator = quote_generator.QuoteGenerator(artist_song_list)
quotes = quote_generator.generate_quotes()

# create Spotify object responsible for handling spotify api requests
sp_handler = Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path='tokens.txt'))

spotify_manager = spotify_manager.SpotifyManager(spotify_handler=sp_handler)

user_id = sp_handler.current_user()['id']

new_playlist = spotify_manager.create_playlist(name=playlist_data[0],
                                               public=False,
                                               description=playlist_data[1])

track_uri_list = spotify_manager.get_song_uri(quotes)

spotify_manager.add_tracks(playlist_id=new_playlist, track_list=track_uri_list)