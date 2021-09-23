alp = 'abcdefghijklmnopqrstuvwxyz'  # Алфавит
long_alp = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'   # Удвоенный алфавит
word = input('Enter a message: ')   # Сообщение для расшифровки или зашифровки
st = int(input('Enter shift: '))    # Смещение
word = word.lower()     # Перевод в нижний регистр

# Если введено значение больше или меньше, чем нужно оно должно быть, то оно приведется к нормальному
while st > 25:
    st -= 26
while st < -26:
    st += 26

zawarudo = []   # Массив для номеров букв
# Преобразование строки в массив с номерами букв
for i in range(len(word)):
    zawarudo.append(word[i])

for i in range(len(word)):
    if zawarudo[i] == ' ' or zawarudo[i] == '\'' or zawarudo[i] == '.' or zawarudo[i] == ',' \
            or zawarudo[i] == '!' or zawarudo[i] == '?':
        continue
    for j in range(len(alp)):
        if zawarudo[i] == alp[j]:
            zawarudo[i] = alp.find(zawarudo[i])
new_str = ''    # Строка для вывода

for i in range(len(word)):      # Вывод зашифрованного или расшифрованного сообщения
    if zawarudo[i] == ' ':
        new_str += ' '
        continue
    if zawarudo[i] == '\'':
        new_str += '\''
        continue
    if zawarudo[i] == '.':
        new_str += '.'
        continue
    if zawarudo[i] == ',':
        new_str += ','
        continue
    if zawarudo[i] == '!':
        new_str += '!'
        continue
    if zawarudo[i] == '?':
        new_str += '?'
        continue
    new_str += long_alp[zawarudo[i] + st]
print('Encrypted message: ', new_str)

