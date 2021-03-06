import requests
from requests.exceptions import ProxyError
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sprt=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

repo_dict = repo_dicts[1]
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print('\nSelected information about first repository')
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

#print(response_dict.keys())

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24 
my_config.label_font_size = 14 
my_config.major_label_font_size = 18 
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


names, stars = [], []
for temp_repo_dict in repo_dicts:
    names.append(temp_repo_dict['name'])
    stars.append(temp_repo_dict['stargazers_count'])

my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(style= my_style)
chart.title = 'MOst-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')