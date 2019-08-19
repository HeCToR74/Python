from celery import Celery
from celery.task import periodic_task

app = Celery('celery_balance', broker='redis://localhost:6379/0')

@periodic_task(ignore_result=True, run_every=60)
def periodic_balance():
    import urllib.request, json
    with urllib.request.urlopen("http://127.0.0.1:8000/api/customeres/") as url:
        data = json.loads(url.read().decode())
    total_balance = sum([item['balance'] for item in data['customeres']])
    print("Total balance is {}.".format(total_balance))
    if total_balance > 100000:
        print("The total balance is over 100,000 points.")

@periodic_task(ignore_result=True, run_every=1)
def periodic():
    import urllib.request, json
    with urllib.request.urlopen("http://127.0.0.1:8000/api/customeres/") as url:
        data = json.loads(url.read().decode())
    for customer in data['customeres']:
        if customer['balance'] == 0:
            print("The balance of {} is 0".format(customer['name']))
        if customer['balance'] > 1000:
            print("The balance of {} is more than 1000".format(customer['name']))

if __name__ == "__main__":
    periodic_balance.delay()
    periodic.delay()