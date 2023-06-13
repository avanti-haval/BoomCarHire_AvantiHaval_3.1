from datetime import datetime,timedelta

issue_date = input("Enter date in dd-mm-yyyy format")
issue_date = issue_date.split("-")
issue_date = datetime(int(issue_date[2]),int(issue_date[1]),int(issue_date[0]))
print(issue_date)


submit_date = input("Enter date in dd-mm-yyyy format")
submit_date = submit_date.split("-")
submit_date = datetime(int(submit_date[2]),int(submit_date[1]),int(submit_date[0]))
print(submit_date)

days = (submit_date-issue_date).days
print(days)