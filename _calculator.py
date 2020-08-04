def get_quotient_and_rem(a, b):
    quotient = a // b
    remainder = a % b

    return remainder, quotient


def time_format(current):
    if current == "PM":
        return "AM"
    if current == "AM":
        return "PM"


def greater_than_twelve(hour, period, minute, tod):
    extra_period, number_of_days = get_quotient_and_rem(period, 2)
    # returned_time = ""
    if hour == 0:
        hour = 12

    if extra_period != 0:
        number_of_days += 1
        if number_of_days == 1:
            if tod == "PM":
              addition = "(next day)"
              return hour, minute, time_format(tod), addition
                # returned_time += f'{hour}:{minute:02d} {time_format(tod)} (next day)'
            else:
              return hour, minute, time_format(tod), addition
                # returned_time += f'{hour}:{minute:02d} {time_format(tod)}'
        else:
          addition = f"{number_of_days} days later)"
          return hour, minute, time_format(tod), number_of_days, addition
            # returned_time += f'{hour}:{minute:02d} {time_format(tod)} ({number_of_days} days later)'
    else:
        if number_of_days == 1:
          addition = '(next day)'
          return hour, minute, tod, addition
            # returned_time += f'{hour}:{minute:02d} {tod} (next day)'
        else:
            number_of_days += 1
            addition = f"({number_of_days} days later)"
            return hour, minute, tod, number_of_days, addition
            # returned_time += f'{hour}:{minute:02d} {tod} ({number_of_days} days later)'

    # return returned_time


def get_day(current_day, days_added):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    new_day = 0
    returned_day = ""
    for item in days_of_week:
        if current_day == item[1]:
            new_day = item[0]
            if days_added != 0:
                new_day += days_added
    if new_day > 7:
        new_day = new_day % 7

    returned_day = days_of_week[new_day]

    return returned_day


def add_time(start, duration, day="Today"):
    print(start)
    print(duration)
    new_time = ""
    # added_day = ""

    time, time_of_day = start.split(' ')
    time_hour, time_min = time.split(':')
    duration_hour, duration_min = duration.split(':')

    total_min = int(time_min) + int(duration_min)
    total_hour = int(time_hour) + int(duration_hour)
    print(total_hour)
    print(total_min)
    if total_min <= 60:
        if total_hour < 12:
            new_time += f'{total_hour}:{total_min:02d} {time_of_day} '
        elif total_hour == 12:
            new_time += f'{total_hour}:{total_min:02d} {time_format(time_of_day)}'
        else:
            hour_result, hour_extra = get_quotient_and_rem(total_hour, 12)
            #2,2
            new_time += greater_than_twelve(hour_result, hour_extra, total_min,
                                            time_of_day)

    else:
        min_result, min_extra = get_quotient_and_rem(total_min, 60)
        total_hour += min_extra
        if total_hour < 12:
            new_time += f'{total_hour}:{min_result:02d} {time_of_day}'
        elif total_hour == 12:
            if time_of_day == "PM":
                new_time += f'{total_hour}:{min_result:02d} {time_format(time_of_day)} (next day)'
            else:
                new_time += f'{total_hour}:{min_result:02d} {time_format(time_of_day)}'
        else:
            hour_result, hour_extra = get_quotient_and_rem(total_hour, 12)
            new_time += greater_than_twelve(hour_result, hour_extra,
                                            min_result, time_of_day)

    return new_time
