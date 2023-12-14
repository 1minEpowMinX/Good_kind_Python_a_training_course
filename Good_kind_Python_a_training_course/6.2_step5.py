'''Имеется закодированная строка с помощью азбуки Морзе. Коды разделены между собой пробелом. 
Необходимо ее раскодировать, используя азбуку Морзе из предыдущего занятия. 
Полученное сообщение (строку) вывести на экран.

Sample Input:
.-- ... . -...- .-- . .-. -. ---
Sample Output:
все верно'''

morze = {' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
         'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}
reversed_morze = {v: k for k, v in morze.items()}
print(*[reversed_morze[w].lower() for w in input().split()])