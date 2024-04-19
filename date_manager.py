import datetime


class DateManager:
    """
    Class responsible for getting  the data from the user in specified
    format.

    Class responsible for getting the date from the user in correct format.
    Class responsible also for getting the title and the description of
    the new created playlist.
    """
    def __init__(self):
        """
        Initialize data attributes of DateManager class.
        """
        self.today = datetime.datetime.now(tz=datetime.timezone.utc).date()

    def get_date(self) -> str:
        """
        Return date provided by the user in YYYY-MM-DD format.

        Get the date from the user and set its value to the
        class attribute date.
        """

        while True:
            print("Which year do you want to travel to? "
                  "Type the date in this format YYYY-MM_DD:")
            date = input()
            # you have to also check if the user did not type letters
            # in correct format. It will crash the program later.
            if len(date) != 10 or date[4] != '-' or date[-3] != '-':
                print("Wrong format. Type date again.")
            elif self.check_date(date):
                return date
            else:
                print("Invalid date.")

    def check_date(self, date: str) -> bool:
        """
        Return True if passed `date` components meet requirements.
        Return False otherwise.

        Parse 'date' to get elements of the date and convert them
        into integers.
        YYYY component cannot be greater that present year.
        If YYYY component is the same as present year then MM
        component cannot be greater than present month.
        If MM component is the same as present month then DD component
        cannot be greater than current date.
        If above requirements met then return True. Return False
        otherwise.
        If year component from `date` argument is the leap year then
        if the month component is equal to 2 then day component cannot
        be greater than 29. If not leap year but month is chosen to 2
        then day component cannot be greater than 28.
        :param date: string representing date in YYYY-MM-DD format.
        """

        date_elements = [int(element) for element in date.split('-')]
        year = date_elements[0]
        month = date_elements[1]
        day = date_elements[2]

        if year % 4 == 0:
            if year % 100 != 0:
                leap_year = True
            else:
                if year % 400 == 0:
                    leap_year = True
                else:
                    leap_year = False
        else:
            leap_year = False

        if 1950 <= year < self.today.year:
            if month != 2:
                if month % 2 != 0:
                    if 1 <= day <= 31:
                        return True
                    else:
                        return False
                else:
                    if 1 <= day <= 30:
                        return True
                    else:
                        return False
            else:
                if leap_year:
                    if 1 <= day <= 29:
                        return True
                    else:
                        return False
                else:
                    if 1 <= day <= 28:
                        return True
                    else:
                        return False
        elif year == self.today.year:
            if month <= self.today.month:
                if day <= self.today.day:
                    return True
                else:
                    return False
            else:
                return False

    def get_playlist_details(self):
        """
        Get the name on the created playlist and short description from
        the user.

        Return tuple containing playlist title and short description of
        the playlist.
        """
        playlist_name = input("Please enter playlist name:\n")
        playlist_description = input("Please enter short description "
                                     "of the playlist being created:\n")
        return playlist_name, playlist_description

