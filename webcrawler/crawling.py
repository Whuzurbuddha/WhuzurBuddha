import requests
from bs4 import BeautifulSoup
import pymysql


def getWebsiteContent():
    db = pymysql.connect(
        host='127.0.0.1',
        user='YOURUSERNAME',
        password='****',
        db='crawling'
    )
    try:
        with db.cursor() as cursor:
            sql = "select * from reachable_IPs;"
            cursor.execute(sql)
            result = cursor.fetchall()

            IDs = [row[0] for row in result]
            IPs = [row[1] for row in result]

        for ID, IP in zip(IDs, IPs):
            try:
                GET = requests.get(IP, verify=False, timeout=2)
                POST = requests.post(IP, verify=False, timeout=2)
                responseType = []
                if GET.status_code == 200:
                    responseType.append(GET)
                else:
                    responseType.append(POST)

                soup = BeautifulSoup(responseType[0].text, 'html.parser')
                title = soup.title.string.strip() if soup.title else 'not title'
                headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
                content = [heading.get_text().strip() for heading in headings]
                print(f"URL: {IP}")
                print(f"title: {title}")
                print(f"topic:{content}")
                try:
                    with db.cursor() as cursor:
                        for KEY, CONTENT in zip(ID, content):
                            print(f"ID: {KEY}")
                            sql = "INSERT INTO content (content_key, content_data) VALUES (%s, %s)"
                            cursor.execute(sql, (KEY, CONTENT))
                    db.commit()
                    print("Data inserted successfully. GET")

                except Exception as e:
                    print("Error:", str(e))
                    continue
            except requests.exceptions.Timeout as e:
                print(f"Timeout occurred for URL {IP}. Moving to the next IP.")
                continue
            except requests.exceptions.RequestException as e:
                print(f"URL {IP} is not accessible.")
                continue
        db.commit()

    finally:
        db.close()


if __name__ == '__main__':
    getWebsiteContent()
