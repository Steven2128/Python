from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        "name" : "Mont Blac",
        "user" : "Yésica Cortés",
        "timestamp" : datetime.now().strftime("%dth %b %Y - %H:%M"),
        "picture" : "https://i.picsum.photos/id/113/200/200.jpg"

    },
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]


def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <p><img src="{picture}"/></p>
        """.format(**post))
    return HttpResponse("<br>".join(content))