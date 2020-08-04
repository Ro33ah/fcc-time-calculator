#returns remainder and quotient values
def get_quotient_and_rem(a, b):
    quotient = a // b
    remainder = a % b

    return remainder, quotient

def time_format(current):
    if current == "PM":
        return "AM"
    if current == "AM":
        return "PM"

#computes and returns day of the week when supplied 
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
  for item in days_of_week.items():
      if current_day.lower() == item[1].lower():
        new_day = item[0]
        if days_added != 0:
          new_day += days_added
              
  if new_day == 0:
    return returned_day
  if new_day > 7:
    new_day = new_day % 7

  returned_day = days_of_week[new_day]

  return returned_day

#called when total hours greater than 12
def greater_than_twelve(hour, period, minute, tod):
    extra_period, number_of_days = get_quotient_and_rem(period, 2)
    addition = ""
    if hour == 0:
        hour = 12

    if extra_period != 0:
        number_of_days += 1
        if number_of_days == 1:
            if tod == "PM":
              addition = " (next day)"
              return hour, minute, time_format(tod), number_of_days, addition
            else:
              return hour, minute, time_format(tod), number_of_days, addition
        else:
          addition = f" ({number_of_days} days later)"
          return hour, minute, time_format(tod), number_of_days, addition
    else:
        if number_of_days == 1:
          addition = ' (next day)'
          return hour, minute, tod, number_of_days, addition
        else:
            number_of_days += 1
            addition = f" ({number_of_days} days later)"

            return hour, minute, tod, number_of_days, addition

#put the result string together
def get_string_result(f_hour, f_min, f_tod, f_nod=0, f_day="", strng =""):
  f_result = ""
  if f_nod != 0:
    if f_day != "":
      f_day = get_day(f_day, f_nod)
      if f_day:
        f_day = f', {f_day}'
    else:
      f_result = f'{f_hour}:{f_min:02d} {f_tod}{strng}'

    f_result = f'{f_hour}:{f_min:02d} {f_tod}{f_day}{strng}'

  if f_nod == 0:
    if f_day == "":
      f_result = f'{f_hour}:{f_min:02d} {f_tod}{strng}'
    else:
      f_day = f', {f_day}'
      f_result = f'{f_hour}:{f_min:02d} {f_tod}{f_day}{strng}'

  return f_result

def add_time(start, duration, day=""):
    new_time = ""
    days = 0
    time, time_of_day = start.split(' ')
    time_hour, time_min = time.split(':')
    duration_hour, duration_min = duration.split(':')

    total_min = int(time_min) + int(duration_min)
    total_hour = int(time_hour) + int(duration_hour)
  
    if total_min <= 60:
        if total_hour < 12:
          new_time = get_string_result(total_hour, total_min, time_of_day, days, day)
        elif total_hour == 12:
          new_time = get_string_result(total_hour, total_min, time_format(time_of_day))
        else:
            hour_result, hour_extra = get_quotient_and_rem(total_hour, 12)
            hour_result, total_min, time_of_day, days, extra_string = greater_than_twelve(hour_result, hour_extra, total_min, time_of_day)
            new_time = get_string_result(hour_result, total_min, time_of_day, days, day, extra_string)
    #if total minutes above 60
    else:
        min_result, min_extra = get_quotient_and_rem(total_min, 60)
        total_hour += min_extra
        if total_hour < 12:
            new_time = get_string_result(total_hour, min_result, time_of_day)
        elif total_hour == 12:
            if time_of_day == "PM":
              extra_string = ' (next day)'
              new_time = get_string_result(total_hour, min_result, time_format(time_of_day), extra_string)
            else:
                new_time = get_string_result(total_hour, min_result, time_format(time_of_day))
        else:
            hour_result, hour_extra = get_quotient_and_rem(total_hour, 12)

            hour_result, total_min, time_of_day, days, extra_string = greater_than_twelve(hour_result, hour_extra, min_result, time_of_day)
            new_time = get_string_result(hour_result, total_min, time_of_day, days, day, extra_string)

    return new_time