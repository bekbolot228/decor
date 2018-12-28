from decorators import address
from helpers import send_response
from renderer import render


@address('about')
def about_handler(request, conn, match=True):
    template = "about.html"
    content = render(template)
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(content)

    send_response(resp, conn, match)
    

@address('contacts')
def contact_handler(request, conn, match=True):
    template = "contacts.html"
    content = render(template)
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(content)
    send_response(resp, conn, match)
