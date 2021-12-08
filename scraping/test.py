from bs4 import BeautifulSoup
import requests

session = requests.Session()
url = "https://cleaningtheglass.com/stats/team/5#tab-offensive_overview"
my_headers = {
    'authority': 'cleaningtheglass.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
    'cookie': 'wordpress_logged_in_cfb45adfd4102bd74a046b78d76db012=zach225793%7C1670421579%7Cqe3pn3baHEn8lPIIQEpw2tAfbqsdUfINheMSscIPNl5%7Cce0105c6a9be760e3c27785cfabe16ec680f440f05609b1e800ffd1f561775b0; sessionid=yh4dn9hkv9ohcjzjge5twtl0g5skpi2m; csrftoken=DzYXKBmEics8LjNpMZl7B7szJOBuxQOMtO496G8DI2aSwt9pdwJ4TvUkrdAY8GMj',
}

response = session.get(url, headers=my_headers)
print(response)

html_soup = BeautifulSoup(response.text, 'html.parser')
