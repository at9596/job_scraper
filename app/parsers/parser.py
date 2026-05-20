from bs4 import BeautifulSoup


def parse_jobs(html):

    soup = BeautifulSoup(html, "html.parser")

    job_cards = soup.find_all(
        "div",
        class_="card-content"
    )

    jobs = []

    for job in job_cards:

        title = job.find(
            "h2",
            class_="title"
        ).text.strip()

        company = job.find(
            "h3",
            class_="company"
        ).text.strip()

        location = job.find(
            "p",
            class_="location"
        ).text.strip()

        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })

    return jobs