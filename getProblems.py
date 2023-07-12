import time
import sqlite3
import requests
from bs4 import BeautifulSoup


def get_codeforces_problems(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.content, "html.parser")
    problem_list = soup.find_all("tr")[1:]
    problems = []
    for problem in problem_list:
        problem_number_tag = problem.find("td", class_="id")
        if problem_number_tag is None:
            continue
        problem_number = problem_number_tag.text.strip()
        problem_link = "https://codeforces.com" + problem.find("a").get("href")
        rating_element = problem.find("span", class_="ProblemRating")
        rating = rating_element.text.strip() if rating_element else "N/A"
        problems.append({
            "problem_number": problem_number,
            "problem_link": problem_link,
            "rating": rating
        })
    return problems


def getPages(Max_page):
    conn = sqlite3.connect('database.db')
    for i in range(1, Max_page + 1):
        print(i)
        url = "https://codeforces.com/problemset/page/" + str(i)
        problems = get_codeforces_problems(url)
        for problem in problems:
            if problem['rating'] != 'N/A':
                print(problem['problem_number'], problem['rating'], problem['problem_link'])
                conn.execute('INSERT INTO problems (id,rating,url) VALUES (?,?,?)',
                             (problem['problem_number'], problem['rating'], problem['problem_link']))
                conn.commit()
        time.sleep(5)
    conn.close()


getPages(88)
