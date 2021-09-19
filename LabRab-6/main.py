def code(line, key):
    result = ''.join([chr(ord(smb)+key) for smb in line])
    return result


# rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# nums = '1234567890'
# smbs = ':; !&-+=()*/.,'
# alph = rus + rus.upper() + nums + smbs

line = 'Привед Медвед...'

key = 3 # это шаг смещения - может быть + или -

line_code = code(line, key)
print(line_code)