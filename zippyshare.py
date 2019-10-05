import os
import sys

import requests

from resizer import size

directory = os.environ["HOME"] + "/Downloads/samehadaku"


def download(link: str):
    print()
    print("Getting file from zippyshare")
    print()
    data = requests.get(link)
    link = link.split("/v/")[0]
    temp = data.text.split("document.getElementById('dlbutton').href = ")[1].split(";")[0]
    temp = temp.replace(" ", "").replace("\"", "").replace("+(", ")+").split(")+")
    content_id = temp[0]
    code1 = temp[1].split("+")[0].split("%")
    code2 = temp[1].split("+")[1].split("%")
    security_code = str(int(code1[0]) % int(code1[1]) + int(code2[0]) % int(code2[1]))
    filename = temp[2]

    link += content_id + security_code + filename
    filename = temp[2].replace("%5b", "[").replace("%5d", "]")

    if not os.path.exists(directory):
        os.makedirs(directory)

    print("Downloading", filename.replace("/", ""))

    with open(directory + filename, "wb") as f:
        data = requests.get(link, stream=True)
        length = data.headers.get('content-length')
        if length is None:
            f.write(data.content)
        else:
            dl = 0
            length = int(length)
            for data in data.iter_content(chunk_size=1024):
                dl += len(data)
                f.write(data)
                sys.stdout.write("\r%s/%s Downloaded" % (size(dl), size(length)))
                sys.stdout.flush()
