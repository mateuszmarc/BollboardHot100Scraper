import spotipy
from spotipy import SpotifyOAuth
import requests


CLIENT_ID = 'fd432a3d5f694aafbaae38fe47a67663'
CLIENT_SECRET = 'bab6f27ce7ce4539b99fe8b766769a53'
REDIRECT_URL = 'http://example.com'
# USER_ID : 31wcyclerx2go3ts7jc3qwasivf4'
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               show_dialog=True,
                                               cache_path='tokens.txt'))
# playlists = sp.current_user_playlists()
# for item in playlists.items():
#     print(item)
quote = 'remaster%20track:Incomplete%20Sisqo'



uri = sp.search(q=quote, limit=50)
for item in uri['tracks']['items']:
    if item['name'] == 'Incomplete':
        print(f'Name : {item["name"]}')
        break
    print()



















# data = sp.search(q='remaster%20track:Players%20Coi%20Leray', limit=1)

# for item in data['item']:
# print(data['tracks']['items'][0]['artists'][0]['name'])


# print(data['tracks']['items'][0]['uri'])

# user_id = sp.current_user()['id']
# #
# response = requests.post(url=f'https://api.spotify.com/v1/users/{user_id}/playlists',
#                          headers={
#                              'Authorization': 'Bearer BQC3nkl3IAfdKnXiDxHw_JS0xvxtmKIxll-I5FJKGYuZi7KM9DSW_2OwQ39O1WjoKL1CHvko5gKZxU4NlodzuY7-LDhqJIbLkwTa6OTkH8uvgmq_LEl4KN-Bkkg7Fw3_oSl5MAWtQdqn1MyQW5OACZJpPmIZxY5-NAW3E2rCh1c0OpU9z7pVhNZQsiLIL--gW_KmFrmE0o949vVEdUluRBqwnaJRDqgoHKM5zaAhpFtBlKaZ0VxAOqg3Jp5N',
#                              'Content-Type': 'application/json'
#                          },
#                          json={
#                              'name': "Test new Playlist",
#                              'description': 'Checking the code',
#                              'public': 'false'
#                          })
# response.raise_for_status()
# playlist_id = response.json()['id']
#
# new_response = requests.post(url=f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks',
#                              headers={
#                                  'Authorization': 'Bearer BQC3nkl3IAfdKnXiDxHw_JS0xvxtmKIxll-I5FJKGYuZi7KM9DSW_2OwQ39O1WjoKL1CHvko5gKZxU4NlodzuY7-LDhqJIbLkwTa6OTkH8uvgmq_LEl4KN-Bkkg7Fw3_oSl5MAWtQdqn1MyQW5OACZJpPmIZxY5-NAW3E2rCh1c0OpU9z7pVhNZQsiLIL--gW_KmFrmE0o949vVEdUluRBqwnaJRDqgoHKM5zaAhpFtBlKaZ0VxAOqg3Jp5N',
#                                  'Content-Type': 'application/json'
#                              },
#                              json={
#                                  'uris': ['spotify:track:3OHfY25tqY28d16oZczHc8']
#                              }
#                              )


# tracks -> items -> ['id'], ['name'], ['uri']