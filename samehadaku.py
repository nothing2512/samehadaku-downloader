import requests

from ads_remover import remove_ads
from zippyshare import download


class Samehadaku:

    def __init__(self):
        self.animes = []

    def get_page(self, loop=False):

        if not loop:
            while True:
                page = input("input page : ")
                print()

                if page.lower() in ["exit", "e"]:
                    exit(0)
                elif not page.isdigit():
                    print("invalid page")
                    print()
                else:
                    break

            link = "https://www.samehadaku.tv"
            link = link if page in ["1", "0"] else link + "/page/" + page

            data = requests.get(link)
            temp = data.text.split("<div class=\"white updateanime\">")[1]
            temp = temp.split("<div class=\"white updatekomik\">")[0].split("<div class=\"clear\"")[0]
            temp = temp.split("<ul>")[1].split("</ul>")[0].replace("\n", "").split("<li")[1:]

            self.animes = []

            for x in range(len(temp)):
                item = temp[x]
                link = item.split("href=\"")[1].split("\"")[0]
                title = item.split("title=\"")[1].split("\"")[0]
                self.animes.append({
                    'link': link,
                    'title': title
                })
                print(x + 1, title, sep=". ")
        else:
            for x in range(len(self.animes)):
                print(x + 1, self.animes[x]['title'], sep=". ")

        while True:
            print()
            result = input("input choice : ")
            print()

            if result.lower() in ["back", "b"]:
                return self.get_page()
            elif result.lower() in ["exit", "e"]:
                exit(0)
            elif result.isdigit():
                if 1 <= int(result) <= 8:
                    return self.animes[int(result)]['link']
                else:
                    print("invalid choice")
            else:
                print("invalid Choice")

    @staticmethod
    def get_file(link: str):
        print("Getting data from samehadaku")
        data = requests.get(link)
        temp = data.text.split('<div class="download-eps" style="text-align: center;">')[-1]
        temp = temp.replace("</ul>", "<ul>").strip().split("<ul>")[1].strip().split("ZS")[0].strip()
        link = temp.split("href=\"")[-1].split("\"")[0].strip()

        status, message, link = remove_ads(link)

        if not status:
            print(message)
        else:
            download(link)

        return True
