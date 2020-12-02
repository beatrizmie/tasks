import requests

# Create your tests here.

post_response = requests.post('http://localhost:8000/tasks/create_task', json={'title': 'primeira task', 'pub_date': '2020-12-02T00:59:43Z', 'description': 'criando uma task para testar'})
post1_response = requests.post('http://localhost:8000/tasks/create_task', json={'title': 'segunda task', 'pub_date': '2020-12-02T00:19:43Z', 'description': 'criando duas tasks para testar'})
post2_response = requests.post('http://localhost:8000/tasks/create_task', json={'title': 'terceira task', 'pub_date': '2020-12-02T00:59:43Z', 'description': 'criando três tasks para testar'})
post3_response = requests.post('http://localhost:8000/tasks/create_task', json={'title': 'quarta task', 'pub_date': '2020-12-02T00:53:43Z', 'description': 'criando quatro tasks para testar'})
post4_response = requests.post('http://localhost:8000/tasks/create_task', json={'title': 'quinta task', 'pub_date': '2020-12-02T00:59:41Z', 'description': 'criando cinco tasks para testar'})
post5_response = requests.post('http://localhost:8000/tasks/create_task', json={'title': 'sexta task', 'pub_date': '2020-12-02T00:22:43Z', 'description': 'criando seis tasks para testar'})
post6_response = requests.post('http://localhost:8000/tasks/create_task', json={'title': 'sétima task', 'pub_date': '2020-12-02T00:59:54Z', 'description': 'criando sete tasks para testar'})

get_all_response = requests.get('http://localhost:8000/tasks/all_tasks')
print(get_all_response.text)

update_title_response = requests.put('http://localhost:8000/tasks/update_task_title/3', json={'title': 'outra task'})
update_pub_date_response = requests.put('http://localhost:8000/tasks/update_task_pub_date/4', json={'pub_date': '2020-12-02T03:34:43Z'})
update_description_response = requests.put('http://localhost:8000/tasks/update_task_description/5', json={'description': 'nova descricao'})

get_task3_response = requests.get('http://localhost:8000/tasks/3')
get_task4_response = requests.get('http://localhost:8000/tasks/4')
get_task5_response = requests.get('http://localhost:8000/tasks/5')

print(get_task3_response.text)
print(get_task4_response.text)
print(get_task5_response.text)

delete_task_response = requests.delete('http://localhost:8000/tasks/delete_task/6')
delete_all_response = requests.delete('http://localhost:8000/tasks/delete_all_tasks')