from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGETED_PRICE = 100
SMTP_ADDRESS = os.environ["SMTP_ADDRESS"]
MY_EMAIL = os.environ["EMAIL_ADDRESS"]
MY_PASS = os.environ["PASSWORD"]
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

# import the price from the website
response = requests.get(url=LIVE_URL, headers=header)
product_webpage = response.text

soup = BeautifulSoup(product_webpage, "lxml")
price_str = soup.find(class_="a-price-whole").getText()
pot_price = float(price_str.split(".")[0])

# send message if the price is below targeted price
title_broken = soup.find(name="span", id="productTitle").getText().split()
title = " ".join(title_broken)

message = f"{title} is now ${pot_price}.\nGo buy it soon. Product link: {LIVE_URL}"

if pot_price < TARGETED_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rohanrahim04@gmail.com",
            msg=f"Subject:Purchase Alert!!\n{message}".encode("UTF-8")
        )


