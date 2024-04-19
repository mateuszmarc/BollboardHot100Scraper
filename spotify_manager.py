import spotipy
import requests


class SpotifyManager:
    """
    Class responsible for handling Spotify Api requests.
    """

    def __init__(self, spotify_handler: spotipy.Spotify) -> None:
        """
        Initialize data attributes of SpotifyManager class.
        :param spotify_handler: Instance of spotipy.Spotify class which
            will be responsible for handling api requests.
        """

        self.token = None
        self.spotify_handler = spotify_handler
        self.user_id = self.spotify_handler.current_user()['id']
        self.get_spotify_token('tokens.txt')
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
        }

    def get_song_uri(self, quotes: list) -> list:
        """
        Return list of unique Spotify URIs of the songs.
        :param quotes: List of  formatted string used for making get
            request from Spotify search api.
            Check spotify search api documentation for more details.
        Example value: "remaster%20track:Doxy%20artist:Miles%20Davis"
        """
        uri_list = []
        for item in quotes:
            title = item[1].replace('%20', ' ')
            data = self.spotify_handler.search(q=item, limit=50)
            for data_item in data['tracks']['items']:
                if data_item['name'] == title:
                    uri = data_item['uri']
                    uri_list.append(uri)
                    break
            else:
                print(f"No song uri found for {title}")
        return uri_list

    def get_spotify_token(self, token_file) -> None:
        """
        Extract spotify token from text`token_file`.
        :param token_file: Text file containing spotify authorization
            token.
        """
        with open(token_file, 'r', encoding='utf-8', newline='') as file:
            data = file.read()
        token = (data.split(',')[0]).rstrip('"').lstrip('{"access_token": "')
        self.token = token

    def create_playlist(self, name: str,
                        description: str,
                        public: bool) -> str:
        """
        Create spotify playlist with given `name`, `description`, and
        `public` parameter. Return ID of created playlist.

        :param name: Name of the playlist.
        :param description: Description of the playlist.
        :param public: Defaults to true. If true the playlist will be
            public, if false it will be private. To be able to create
            private playlists, the user must have granted the
            playlist-modify-private scope.
        """
        url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'
        response = requests.post(url=url,
                                 headers=self.headers,
                                 json={
                                     'name': name,
                                     'description': description,
                                     'public': public
                                 })
        response.raise_for_status()
        return response.json()['id']

    def add_tracks(self, playlist_id: str, track_list: list):
        """
        Add tracks to spotify playlist.

        Use spotify api to add tracks to the playlist of given
        `playlist_id`. Tracks are represented by its URIs.
         Note that used spotify scope is set to
        'playlist-modify-private'.
        :param playlist_id: Spotify ID of a playlist.
        :param track_list: List of spotify URIs to add.
        """
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        response = requests.post(url=url,
                                 headers=self.headers,
                                 json={
                                     'uris': track_list
                                 })

        try:
            response.raise_for_status()
        except:
            print("Operation failed")
            pass
        else:
            print("Operation successful")


