import requests
import pymysql

def http_ping():
    reachable_IPs = []
    start_ip = (193, 10, 12, 50)
    end_ip = (193, 99, 144, 85)
    for a in range(start_ip[0], end_ip[0] + 1):
        for b in range(start_ip[1], end_ip[1] + 1):
            for c in range(start_ip[2], end_ip[2] + 1):
                for d in range(start_ip[3], end_ip[3] + 1):
                    ip_address = f"{a}.{b}.{c}.{d}"
                    url = f"http://{ip_address}"
                    try:
                        response = requests.get(url, timeout=0.5)
                        if response.status_code == 200:
                            print(f"found source: {url}")
                            reachable_IPs.append(url)
                        else:
                            print(f"{url} failed")
                    except requests.exceptions.RequestException:
                        print(f"{url} failed")
                    except requests.exceptions.Timeout:
                        print("Timeout")
                        continue
    return reachable_IPs


def insert_data(addresses):
    db = pymysql.connect(
        host='127.0.0.1',
        user='YOURUSERNAME',
        password='****',
        db='crawling'
    )

    try:
        with db.cursor() as cursor:
            for address in addresses:
                sql = "INSERT INTO reachable_IPs (IP) VALUES (%s)"
                cursor.execute(sql, address)
                db.commit()

        print("Data inserted successfully.")

    except Exception as e:
        print("Error:", str(e))


if __name__ == '__main__':
    IPs = http_ping()
    insert_data(IPs)
