from private_data import repl

repl = {
    "LAB-ID": 3,
    "LAB-TITLE": "Работа с массивами данных",
    "STUDENT-NAME": "",
    "GROUP-ID": "",
    "TEACHER-NAME": "",
    "LOCATION": "Москва",
    "YEAR": 2022,
    "PROBLEM": "Вариант №11 В исходной последовательности вещественных чисел найти те, дробная часть которых, представленная в виде целого числа, превышает по модулю их целую часть. Сформировать из данных чисел новую последовательность, удалив их из исходной.",
    "USED-DATA-TYPES": "При выполнении данной лабораторной работы использовался встроенный тип данных double, предназначенный для работы с дробными числами, и long, предназначенный для работы с целыми числами.",
    "MERMAID-CODE": """
<div class="mermaid">
flowchart RL
   subgraph SG0 [" "]
      direction TB
      n0_0["maximize(n)"] --> n0_1["size = ceil(log10(n))"]
      n0_1 --> n0_2["sorted = 0"]
      n0_2 --> n0_3["sorted = 1"]
      n0_3 --> n0_4["offset = 1"]
      n0_4 --> n0_5{{"i = 0; i < size - 1; i++"}}
      n0_5 --> |false| n0_13{"sorted != 1"}
      n0_13 --> |true| n0_3
      n0_5 --> |true| n0_6["digit1 = n / (offset*10) % 10"]
      n0_6 --> n0_7["digit2 = n / (offset   ) % 10"]
      n0_7 --> n0_8{"digit1 > digit2"}
      n0_8 --> |true| n0_9["n = n - digit1 * offset * 10 + digit2 * offset * 10"]
      n0_9 --> n0_10["n = n - digit2 * offset      + digit1 * offset     "]
      n0_10 --> n0_11["sorted = 0"]
      n0_11 --> n0_12["offset *= 10"]
      n0_8 --> |false| n0_12
      n0_12 --> n0_5
       
   end
   subgraph SG1 [" "]
      direction TB
      n1_0[начало] --> n1_1[/ввод n/] --> n1_2{n > 0}
      n1_2 --> |true| n1_3[/"вывести: maximize(n)"/]
      n1_2 --> |false| n1_4[/"вывести: It's not an integer ;(\nSorry, but you'll have to enter an integer next time!\n"/]
      n1_3 & n1_4 --> n1_5[конец]
   end
</div>
""",
    "GRAPH": """
<img width="490" alt="graph1" src="graphs_lab3/graph1.png">
<img width="470" alt="graph2" src="graphs_lab3/graph2.png">
<img width="500" alt="graph3" src="graphs_lab3/graph3.png">
<br><br><br>
    """,
    "PROGRAMS-TEMPLATE": """<p>Листинг {number}: Исходные коды программы {filename} (файл: {filepath})</p>
        <pre>
{code}
</pre>""",
    "TEST-EXAMPLES": """
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
В ходе выполнения данной работы на примере программы, выполняющей умножение целых чисел,
были рассмотрены принципы работы построения программ на языке C:<br>
1. Организация файлов - *.h и *.c.<br>

2. Разработка функций.<br>

3. Операции для детальной работы с вводом.<br>

4. Использование malloc, realloc и free.<br>
""",
    **repl
}
