from private_data import repl

repl = {
    "LAB-ID": 5,
    "LAB-TITLE": "Работа с массивами. Исследование методов сортировки массивов",
    "STUDENT-NAME": "",
    "GROUP-ID": "",
    "TEACHER-NAME": "",
    "LOCATION": "Москва",
    "YEAR": 2023,
    "PROBLEM": """Вариант №35<br><br>
Индивидуальное задание:<br><br>
Структура данных - Избиратель:<br>
- ФИО (строка произвольной длины)<br>
- номер избирательного участка (строка длиной 7 символов вида XXX-YYY, где X — это буква, а Y — цифра)<br>
- возраст (целое число)<br>
<br>
Алгоритмы сортировки:<br>
1. Пузырьковая сортировка (Bubble sort)<br>
2. Двухсторонняя сортировка выбором (Double selection sort)<br>
""",
    "USED-DATA-TYPES": "При выполнении данной лабораторной работы использовался встроенный тип данных char, предназначенный для работы с символами и строками.",
    "GRAPH": """
<img width="300" alt="graph1" src="graphs_lab5/graph1.png">
<img width="350" alt="graph2" src="graphs_lab5/graph2.png">
<br><br><br>
    """,
    "PROGRAMS-TEMPLATE": """<p>Листинг {number}: Исходные коды программы {filename} (файл: {filepath})</p>
        <pre>
{code}
</pre>""",
    "PROGRAMS": "",
    "TEST-EXAMPLES": "",
    "TESTER-TEMPLATE": """<p>Исходный код тестирующей программы {filename} (файл: {filepath})</p>
        <pre>
{code}
</pre>""",
    "TESTER": "",
    "TIMING": """
<img width="600" alt="figure" src="graphs_lab5/figure.png"><br>
Как можно увидеть из приведённого выше графика, пузырьковая сортировка и двухсторонняя сортировка выбором ожидаемо работают за квадратичное время, т.к. их графики являются параболами<br>
И также можно увидеть, что быстрая сортировка работает за ожидаемое O(n * log n), она растёт почти линейно<br>
""",
    "__TEST-EXAMPLES": """
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Введённая команда</th>
    <th class="tg-0pky">Вывод программы</th>
    <th class="tg-0pky">Ожидаемый вывод программы</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">Приветственное сообщение</td>
    <td class="tg-0pky">Приветственное сообщение</td>
  </tr>
  <tr>
<td class="tg-0pky">init</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[]
</td>
<td class="tg-0pky">[]
</td>
</tr>
<tr>
<td class="tg-0pky">init 123.45 123.123 12.345 12 12.0 .34 0.34</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[123.45 123.123 12.345 12.0 12.0 0.34 0.34]
</td>
<td class="tg-0pky">[123.45 123.123 12.345 12.0 12.0 0.34 0.34]
</td>
</tr>
<tr>
<td class="tg-0pky">process</td>
<td class="tg-0pky">Removed [12.345 0.34 0.34]
</td>
<td class="tg-0pky">Removed [12.345 0.34 0.34]
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[123.45 123.123 12.0 12.0] + (3) empty items
</td>
<td class="tg-0pky">[123.45 123.123 12.0 12.0] + (3) empty items
</td>
</tr>
<tr>
<td class="tg-0pky">insert 0 3.1415</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[3.1415 123.45 123.123 12.0 12.0] + (2) empty items
</td>
<td class="tg-0pky">[3.1415 123.45 123.123 12.0 12.0] + (2) empty items
</td>
</tr>
<tr>
<td class="tg-0pky">insert 5 9</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[3.1415 123.45 123.123 12.0 12.0 9.0] + (1) empty items
</td>
<td class="tg-0pky">[3.1415 123.45 123.123 12.0 12.0 9.0] + (1) empty items
</td>
</tr>
<tr>
<td class="tg-0pky">insert 3 8</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[3.1415 123.45 123.123 8.0 12.0 12.0 9.0]
</td>
<td class="tg-0pky">[3.1415 123.45 123.123 8.0 12.0 12.0 9.0]
</td>
</tr>
<tr>
<td class="tg-0pky">insert 7 0</td>
<td class="tg-0pky">Ошибка
</td>
<td class="tg-0pky">Ошибка
</td>
</tr>
<tr>
<td class="tg-0pky">insert 2 9</td>
<td class="tg-0pky">Ошибка
</td>
<td class="tg-0pky">Ошибка
</td>
</tr>
<tr>
<td class="tg-0pky">remove 0</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[123.45 123.123 8.0 12.0 12.0 9.0] + (1) empty items
</td>
<td class="tg-0pky">[123.45 123.123 8.0 12.0 12.0 9.0] + (1) empty items
</td>
</tr>
<tr>
<td class="tg-0pky">insert 0 dfgdfg</td>
<td class="tg-0pky">Ошибка
</td>
<td class="tg-0pky">Ошибка
</td>
</tr>
<tr>
<td class="tg-0pky">resize 4</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[123.45 123.123 8.0 12.0]
</td>
<td class="tg-0pky">[123.45 123.123 8.0 12.0]
</td>
</tr>
<tr>
<td class="tg-0pky">resize 10</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[123.45 123.123 8.0 12.0] + (6) empty items
</td>
<td class="tg-0pky">[123.45 123.123 8.0 12.0] + (6) empty items
</td>
</tr>
<tr>
<td class="tg-0pky">resize 0</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[]
</td>
<td class="tg-0pky">[]
</td>
</tr>
<tr>
<td class="tg-0pky">resize -1</td>
<td class="tg-0pky">Ошибка
</td>
<td class="tg-0pky">Ошибка
</td>
</tr>
<tr>
<td class="tg-0pky">remove 0</td>
<td class="tg-0pky">Ошибка
</td>
<td class="tg-0pky">Ошибка
</td>
</tr>
<tr>
<td class="tg-0pky">resize 3</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">remove 0</td>
<td class="tg-0pky">Ошибка
</td>
<td class="tg-0pky">Ошибка
</td>
</tr>
<tr>
<td class="tg-0pky">insert 0 1</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">print</td>
<td class="tg-0pky">[1.0] + (2) empty items
</td>
<td class="tg-0pky">[1.0] + (2) empty items
</td>
</tr>
<tr>
<td class="tg-0pky">remove 0</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">insert 0 1</td>
<td class="tg-0pky">
</td>
<td class="tg-0pky">
</td>
</tr>
<tr>
<td class="tg-0pky">remove 2</td>
<td class="tg-0pky">Ошибка
</td>
<td class="tg-0pky">Ошибка
</td>
</tr>
<tr>
<td class="tg-0pky">help print</td>
<td class="tg-0pky">Сообщение с помощью
</td>
<td class="tg-0pky">Сообщение с помощью
</td>
</tr>
<tr>
<td class="tg-0pky">exit</td>
<td class="tg-0pky">Сообщение о выходе
<td class="tg-0pky">Сообщение о выходе
</tr>
</tbody>
</table>
""",
    "SCREENSHOTS": """
asdsa: dfgdfg
input 567657
678967
asdsa: fghfgh
asdsa: dgjfghk
asdsa: fkghjk
asdsa: ljkl
""",
    "CONCLUSIONS": """
В ходе выполнения данной работы были рассмотрены сотрировки в языке С
""",
    **repl
}
