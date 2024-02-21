from datetime import datetime, timedelta

def subtract_five_days_from_current_date():
    current_date = datetime.now()
    five_days_ago = current_date - timedelta(days=5)

    return five_days_ago

if __name__ == "__main__":
    result = subtract_five_days_from_current_date()
    print("Current date:", datetime.now().strftime("%Y-%m-%d"))
    print("Date five days ago:", result.strftime("%Y-%m-%d"))
