from bs4 import BeautifulSoup

VALID_TAGS = [
    'p','h1','h2','h3','ul','ol','li',
    'strong','sub','sup',
    'img', 'a', 'video',
    'table','caption','tr','td','th'
    ]

def sanitize_html(value):

    soup = BeautifulSoup(value, "lxml")

    for tag in soup.findAll(True):
        if tag.name not in VALID_TAGS:
            tag.hidden = True

    return soup.renderContents()


if __name__ == '__main__':
    text = '<p>Hello Cleaner</p>'
    ntext = sanitize_html(text)

    # print(text)
    print(ntext.decode())