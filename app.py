import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.ebay.com/itm/Lenovo-ThinkPad-X1-12-Full-HD-2160-x-1440-2-in-1-PC-Tablet-Keyboard-Active-Pen/254291258934?epid=2151884872&_trkparms=ispr%3D1&hash=item3b34f0ae36:g:0J0AAOSw27RdJLuT&enc=AQADAAAB4KX%2FKt4E1xf3SDqEdBclaYYzx0oKUKo981MGtT1DTt2dS65yt%2FfwEBbEhJHxsnNLI8IPqxgmBI9evkv4iYkkzqFret9ApAdBchufqu4ofhcJKm2Vxqm5Kt6C4JWvHGA7fH%2ByfVTLSBNETHTRo2h5fc6Kmbv40gE0wcuB6jAGiYja8SnRXaoGzwPCA%2FcNjc5oVjLsamffHWAC33Pc25NOwvhB3EONVP%2BfhnsaNewlTKViQkfFwst0Htnr%2B5oqTGHCJlSwCOkdg8YbmIrolGcdOAf%2Bf4uy80%2Fp%2BcfXgkzuA3onwsNuk4zPCoejdCWyUnwo7NsZb9J01TivtigObvKkHs2UivQM1djXM0G%2FA75kOcPxU5J6dnKLUYya9M%2Bcc12z7DQ3lgSmJjyV7mo40Dd%2BzqNSxp4mParnKjVkqIleTsCb2Y6nPOp3494LcPekEkADWYlMkXz9Sp%2FP8AEweLNGtZ%2BJtHjG0Srxv3H%2BZkVCljC9rpq8enRh9A1AccV8kFwl2Qq5B5%2FD%2FIKGPQiisRPaTebWU6Ci%2B%2BS7Dt4Xo3mrD%2B3ArVj8gSqqB3ahKLNzQ6%2FvZuqRIosN0i%2BP0Q47K%2BTIl5Pav3kr%2BviVlafX%2BryiFEXVClezuNMj0bswZAakqPYRsg%3D%3D&checksum=25429125893457afe51d3ac249de8b5efeb11edd9a39'


headers = {"User-agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "Priceblock_ourprice").get_text
    converted_price = float(price[0:5])

    if(converted_price > 1.70):
        send_mail()

    print(converted_price)
    print(title.strip())

    if (converted_price < 1.70):
        send_mail()    


def send_mail():
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('saumenroy323@gmail.com', 'Soma1998')

    subject = 'price fell down'
    body = 'check ebay link https://www.ebay.com/itm/Lenovo-ThinkPad-X1-12-Full-HD-2160-x-1440-2-in-1-PC-Tablet-Keyboard-Active-Pen/254291258934?epid=2151884872&_trkparms=ispr%3D1&hash=item3b34f0ae36:g:0J0AAOSw27RdJLuT&enc=AQADAAAB4KX%2FKt4E1xf3SDqEdBclaYYzx0oKUKo981MGtT1DTt2dS65yt%2FfwEBbEhJHxsnNLI8IPqxgmBI9evkv4iYkkzqFret9ApAdBchufqu4ofhcJKm2Vxqm5Kt6C4JWvHGA7fH%2ByfVTLSBNETHTRo2h5fc6Kmbv40gE0wcuB6jAGiYja8SnRXaoGzwPCA%2FcNjc5oVjLsamffHWAC33Pc25NOwvhB3EONVP%2BfhnsaNewlTKViQkfFwst0Htnr%2B5oqTGHCJlSwCOkdg8YbmIrolGcdOAf%2Bf4uy80%2Fp%2BcfXgkzuA3onwsNuk4zPCoejdCWyUnwo7NsZb9J01TivtigObvKkHs2UivQM1djXM0G%2FA75kOcPxU5J6dnKLUYya9M%2Bcc12z7DQ3lgSmJjyV7mo40Dd%2BzqNSxp4mParnKjVkqIleTsCb2Y6nPOp3494LcPekEkADWYlMkXz9Sp%2FP8AEweLNGtZ%2BJtHjG0Srxv3H%2BZkVCljC9rpq8enRh9A1AccV8kFwl2Qq5B5%2FD%2FIKGPQiisRPaTebWU6Ci%2B%2BS7Dt4Xo3mrD%2B3ArVj8gSqqB3ahKLNzQ6%2FvZuqRIosN0i%2BP0Q47K%2BTIl5Pav3kr%2BviVlafX%2BryiFEXVClezuNMj0bswZAakqPYRsg%3D%3D&checksum=25429125893457afe51d3ac249de8b5efeb11edd9a39'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'saumenroy323@gmail.com',
        'soma1998@gmail.com',
        msg
    ) 

    print('Email sent')

    server.quit()


while (True):
    check_price()
    time.sleep(60 * 60)
    