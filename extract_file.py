directory, location, folder, file_name = input().split('\\')
new_file_name, type_file = file_name.split('.')

print(f'File name: {new_file_name}')
print(f'File extension: {type_file}')
