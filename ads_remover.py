import requests


def remove_ads(link: str, x=1):
    print()
    if "anjay.info" in link:
        print("passing ADS", x, "From anjay.info", sep=" ")
        data = requests.get(link)
        action = data.text.split("action=\"")[1].split("\"")[0]
        value = data.text.split("value=\"")[1].split("\"")[0]
        key = data.text.split("\" value")[-2].split("\"")[-1]

        data = requests.post(action, {key: value})
        link = data.text.split("function generate()")[1].split("var a='")[1].split("'")[0]
        status = True
    elif "ahexa.com" in link:
        print("passing ADS", x, "From ahexa.com", sep=" ")
        data = requests.get(link)
        link = data.text.split("download-link")[1].split("a href=\"")[1].split("\"")[0]

        data = requests.get(link)
        link = "https://" + data.text.split("<meta property=\"og:url\" content=\"//")[1].split(" />")[0]
        status = True
    else:
        link, status = "", False

    if not status:
        return status, "ADS has been not handled, contact admin master to handle it", None

    if "zippyshare" in link:
        return status, None, link
    else:
        return remove_ads(link, x + 1)
