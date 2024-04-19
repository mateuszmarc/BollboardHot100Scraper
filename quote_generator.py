class QuoteGenerator:
    """
    Class responsible for generating the quote for Spotify Api fom given
    data object.
    """

    def __init__(self, data_to_parse: list) -> None:
        """
        Initialize data attribute for QuoteGenerator class.
        :param data_to_parse: List of dictionaries. Each dictionary
            contains two items, first artist_name and its value, second
            song_name and its value.
        """
        self.data_to_parse = data_to_parse


    def generate_quotes(self) -> list:
        """
        Return list of formatted quotes parsed from object
        `data_to_parse` data attribute.

        Return quote in specific format for Spotify Search Api.
        Required format: "remaster%20track:Doxy%20artist:Miles%20Davis"
        where track is a title of the song, artist is a name of the
        artist. If song title or artist is made of multiple words api
        requests to use %20 as a separator.

        :return: List of formatted quotes for api get request use.
        """
        quotes = []
        for item in self.data_to_parse:
            artist = item['artist']
            if ' ' in artist:
                artist = artist.replace(' ', '%20')
            artist_quote = f"artist:{artist}"
            title = item['song_title']
            if ' ' in title:
                title = title.replace(' ', '%20')
            title_quote = f'track:{title}'
            full_quote = f"remaster%20{title_quote}%20{artist_quote}"
            quotes.append((full_quote, title))
        return quotes


