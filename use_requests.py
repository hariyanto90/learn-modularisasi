import requests


url = 'https://detik.com'
try :
    response = (requests.get(url))
    if response.status_code == 200:
        print(f'Success {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Program tidak berjalan {response.status_code}')
except Exception as e:
    print(f'Program error {e}')

print('Program ended')



