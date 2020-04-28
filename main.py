from bs4 import BeautifulSoup
import requests
import re


class Scrape:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36",
            "Referer": "http://tools.iedb.org/bcell/"
        }
        self.url = "http://tools.iedb.org/bcell/"

    def get_result(self, seq="", method="Parker"):
        if seq == "":
            raise Exception("没有蛋白质序列")

        session = requests.Session()
        response = session.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        result = soup.find_all("input", attrs={"name": "csrfmiddlewaretoken"})[0]
        token = result["value"]
        print("Token get as", token)
        data = {
            "csrfmiddlewaretoken": token,
            "pred_tool": "bcell",
            "source": "html",
            "form_name": "submission_form",
            "sequence_text": seq,
            "method": method,
            "submit": "Submit",
            "swissprot": ""
        }
        print("Waiting for response")
        response = session.post(self.url, headers=self.headers, data=data)
        print("Got")
        soup1 = BeautifulSoup(response.text, "lxml")
        res = soup1.find_all("div", attrs={"id": "content"})[0].text
        pat = "(-?\d+\.\d{3})"
        result = re.compile(pat).findall(res)
        return result


if __name__ == "__main__":
    Sc = Scrape()
    print(Sc.get_result(seq="HAAVWNAQEAQADFAK"))