from datetime import datetime
def date_difference_in_seconds(date1, date2):
    difference = abs(date1 - date2)
    difference_in_seconds = difference.total_seconds()
    return difference_in_seconds
if __name__ == "__main__":
    date1 = datetime(2022, 1, 1, 12, 0, 0)
    date2 = datetime(2022, 1, 2, 12, 0, 0)
    difference_seconds = date_difference_in_seconds(date1, date2)
    print("Difference between the two dates in seconds:", difference_seconds)
