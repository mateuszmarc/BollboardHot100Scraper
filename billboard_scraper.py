import datetime
import bs4
import requests
import date_manager
import quote_generator


class BillboardScraper:
    """Class responsible for returning the content of the website based
     on date got from user using DateManager object."""

    def __init__(self, url: str, user_handler: date_manager.DateManager) -> None:
        self.url = url
        self.today = datetime.datetime.now(tz=datetime.timezone.utc).date()
        self.date_manager = user_handler
        self.date = self.date_manager.get_date()
        self.url_to_use = f'{self.url}/{self.date}/'
        self.bytes_data = self.parse_website()

    def parse_website(self) -> bytes:
        """
        Return bytes object returned by request to url.
        """
        response = requests.get(url=self.url_to_use)

        response.raise_for_status()
        data = response.content
        return data

    def scrape_html(self, tag_name: str, class_name: str) -> list:
        """
        Return list of objects specified by tag_name and class_name.

        :param tag_name: Tag name that we want to look for
        :param class_name: Tag class that we want to narrow search.
        """
        soup = bs4.BeautifulSoup(self.bytes_data, 'html.parser')
        item_list = [item.text.strip() for item in
                     soup.find_all(name=tag_name, class_=class_name)]
        return item_list


if __name__ == '__main__':
    tracklist_creator = BillboardScraper(url='https://www.billboard.com/charts/hot-100/')
    track_list = tracklist_creator.scrape_html(tag_name='h3', class_name='a-no-trucate')
    artist_list = tracklist_creator.scrape_html(tag_name='span', class_name='a-no-trucate')
    artist_song_list = [{'artist': artist, 'song_title': track_list[index]} for index, artist in enumerate(artist_list)]
    quote_generator = quote_generator.QuoteGenerator(artist_song_list)
    quotes = quote_generator.generate_quotes()

    for quote in quotes:
        print(quote)
