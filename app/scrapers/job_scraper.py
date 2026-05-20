import requests

URL = "https://realpython.github.io/fake-jobs/"


def fetch_jobs_page():

    response = requests.get(URL)

    return response.text