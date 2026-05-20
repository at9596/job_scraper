from app.scrapers.job_scraper import fetch_jobs_page
from app.parsers.parser import parse_jobs


def main():

    html = fetch_jobs_page()
    jobs = parse_jobs(html)

    for job in jobs:

        print("\n------------------------")
        print(f"Title    : {job['title']}")
        print(f"Company  : {job['company']}")
        print(f"Location : {job['location']}")