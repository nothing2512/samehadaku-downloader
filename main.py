from samehadaku import Samehadaku

if __name__ == '__main__':

    samehadaku = Samehadaku()
    url = samehadaku.get_page()
    samehadaku.get_file(url)

    while True:
        c = input("\n\nDo you want to download another file ? ")
        if c.lower() in ["y", "yes"]:
            samehadaku.get_page(True)
        else:
            exit(0)
