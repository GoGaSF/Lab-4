from datetime import datetime
def drop_microseconds(dt):
    return dt.replace(microsecond=0)
if __name__ == "__main__":
    current_datetime = datetime.now()
    print("Current datetime with microseconds:", current_datetime)

    datetime_without_microseconds = drop_microseconds(current_datetime)
    print("Datetime without microseconds:", datetime_without_microseconds)
