"""_Module_"""


class Cat:
    """This is the cat class"""

    nr_of_paws = 4

    def __init__(self, name, eye_color, lives_left=-1):
        self.name = name
        self.eye_color = eye_color
        self._lives_left = lives_left  # if lives_left is not None else -1

    def description(self):
        """abc"""
        # vad är line too long viktigt för?
        string1 = (f"My cat's name is {self.name}, ha" +
                   f"s {self.eye_color} eyes and {self._lives_left } lives left to live.")
        return string1

    def get_lives_left(self):
        """returns lives left"""
        return self._lives_left

    def set_lives_left(self, new_lives_left):
        """sets the new number of lives left for the cat"""
        self._lives_left = new_lives_left

class Duration:
    """This is duration class"""

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        """_summary_

        Returns:
            _string_: _hh-mm-ss as string_
        """
        hours = self.hours
        minutes = self.minutes
        seconds = self.seconds
        temp_list = [
            hours,
            minutes,
            seconds
        ]
        for i in range(3):
            if temp_list[i] > 10:
                temp_list[i] = temp_list[i]
            else:
                temp_list[i] = "0" + str(temp_list[i])
        display_string = str(temp_list[0]) + "-" + \
            str(temp_list[1]) + "-" + str(temp_list[2])
        return display_string

    @staticmethod
    def duration_to_sec(time):
        """takes string hh-mm-ss format and converts to int seconds"""
        h, m, s = time.split("-")
        h = int(h) * 3600
        m = int(m) * 60
        total_time = h + m + int(s)
        return total_time

    def __add__(self, other):
        return Duration.duration_to_sec(self.display()) + Duration.duration_to_sec(other.display())

    def __iadd__(self, other):
        """_summary_
        Args:
            other (_type_): _description_
        Returns:
            _type_: _description_
        """
        dur1 = Duration.display(self)
        dur2 = Duration.display(other)
        h1, m1, s1 = dur1.split("-")
        h2, m2, s2 = dur2.split("-")
        total_s = int(s1) + int(s2)
        total_m = int(m1) + int(m2)
        total_h = int(h1) + int(h2)
        if total_s/60 >= 1:
            total_s -= 60
            total_m += 1

        if total_m/60 >= 1:
            total_m -= 60
            total_h += 1

        return str(total_h) + "-" + str(total_m) + "-" + str(total_s)
