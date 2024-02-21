from datetime import datetime, timedelta

def print_yesterday_today_tomorrow():
    current_date = datetime.now()

    yesterday = current_date - timedelta(days=1)
    tomorrow = current_date + timedelta(days=1)

    print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
    print("Today:", current_date.strftime("%Y-%m-%d"))
    print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
if __name__ == "__main__":
    print_yesterday_today_tomorrow()
