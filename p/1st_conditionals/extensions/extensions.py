name = input('File Name: ').strip().lower()
name = name.split('.')[-1]

match name:
    case 'gif' | 'png':
        print(f'image/{name}')
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case 'pdf' | 'zip':
        print(f'application/{name}')
    case 'txt':
        print('text/plain')
    case _:
        print('application/octet-stream')