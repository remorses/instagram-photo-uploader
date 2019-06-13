
from instabotnet import execute
import getpass

script = """
bot:
  username: {{ username }}
  password: {{ password }}
  settings_path: {{ username + '_cookies.json' }}

actions:
  - 
    name: post photo
    nodes: 
      - {{ path }}
    from: arg
    edges:
      - upload_post
"""

def main():
    print('inserisci l\'username instagram:')
    username = input()
    password = getpass.getpass('inserisci la password:\n')
    # password = input()
    print('inserisci il percorso del file:')
    path = input()
    try:
        result = execute(script, {
            'username': username,
            'password': password,
            'path': path,
        })
        events = [event for event in result['events'] if event['type'] == 'upload_post']
        if not len(events):
            raise Exception('errore nel caricamento')
        url = events[0]['node']['url']
        print('puoi trovare il post in "{url}"')
    except Exception as e:
        print(f'errore: probabilmente password sbagliata\n\n{e}')

main()