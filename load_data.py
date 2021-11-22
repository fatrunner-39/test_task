import requests
import json

# r = requests.get('http://jsonplaceholder.typicode.com/users')
# users = r.json()
# users_data = []
# for user in users:
#     users_dict = dict()
#     users_dict['model'] = 'test_app.Users'
#     users_dict['pk'] = user['id']
#     users_dict['fields'] = {
#         'name': user['name'],
#         'username': user['username'],
#         'email': user['email'],
#         'address': f"{user['address']['street']}, {user['address']['suite']}, "
#                    f"{user['address']['city']}, {user['address']['zipcode']}, "
#                    f"geo: lat {user['address']['geo']['lat']}, lng"
#                    f" {user['address']['geo']['lng']} ",
#         'phone': user['phone'],
#         'website': user['website'],
#         'company': f'''name: "{user['company']['name']}", catchPhrase: "{user['company']['catchPhrase']}, bs: "{user['company']['bs']}"''',
#     }
#     users_data.append(users_dict)
# print(users_data)

# with open(r'C:\Users\\alexa_000\PycharmProjects\\test_work\\test_project\\test_app\\fixtures'
#           r'\\users.json', 'w', encoding='UTF-8') \
#         as file:
#     json.dump(users_data, file)

resp = requests.get('http://jsonplaceholder.typicode.com/posts')
posts = resp.json()
posts_data = []
for post in posts:
    posts_dict = dict()
    posts_dict['model'] = 'test_app.Posts'
    posts_dict['pk'] = post['id']
    posts_dict['fields'] = {
        'userId': post['userId'],
        'title': post['title'],
        'body': post['body']
        }
    posts_data.append(posts_dict)
print(posts_data)

with open(r'/test_project/test_app/fixtures/posts.json', 'w', encoding='UTF-8') \
        as file:
    json.dump(posts_data, file)

"""Для загрузки данных в БД применял командыЖ
py manage.py loaddata users.json,
py manage.py loaddata posts.json
"""