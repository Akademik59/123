name_file_txt = 'block.txt'
name_file_html = 'pattern.html'
name_file_out = name_file_txt.split('.')[0] + '.html'

file_in = open(name_file_txt, encoding='utf-8')
lines_in = file_in.readlines()
file_in.close()

file_pat = open(name_file_html, encoding='utf-8')
lines_pat = file_pat.readlines()
file_pat.close()
print(lines_pat)

parags = []
for parag_lines in ''.join(lines_in[2:]).split('\n\n'): # абзац по двойному символу переноса
    parags.append('<p>' + '<br>\n'.join(parag_lines.split('\n')) + '</p>\n')

lines_for_public = []
for line in lines_pat: # читаем из шаблона
    lines_for_public.append(line) # добавляем в итоговый
    if '<title>' in line:
        lines_for_public.append(lines_in[0].strip())
    if '<body>' in line:
        lines_for_public.extend(parags)

file_out = open(name_file_out, mode='w', encoding='utf-8')
file_out.writelines(lines_for_public)
file_out.close()