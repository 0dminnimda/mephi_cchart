from private_data import repl

repl = {
    "LAB-TITLE": "Работа с массивами данных",
    "LAB-ID": 2,
    "STUDENT-NAME": "",
    "GROUP-ID": "",
    "TEACHER-NAME": "",
    "LOCATION": "Москва",
    "YEAR": 2022,
    "PROBLEM": "Вариант №23 Вычислить значение функции y = √n a в точке по итерационной формуле.",
    "USED-DATA-TYPES": "При выполнении данной лабораторной работы использовался встроенный тип данных double, предназначенный для работы с дробными числами.",
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
{PROGRAM-FILE}<br><br>
<img width="490" alt="graph1" src="graph1.png">
<img width="470" alt="graph2" src="graph2.png">
<img width="500" alt="graph2" src="graph3.png">
<br><br><br>
{PROGRAM-FILE2}<br><br>
<img width="500" alt="graph4" src="graph4.png">
<img width="455" alt="graph2" src="graph2.png">
<br><br>
<img width="500" alt="graph5" src="graph5.png">
    """,
    "PROGRAM-NAME": "root_iter",
    "PROGRAM-FILE": "root_iter.c",
    "C-CODE": """
int main() {
   return 0;
}
""",
    "PROGRAMS-TEMPLATE": """<p>Листинг {number}: Исходные коды программы {filename} (файл: {filepath})</p>
        <pre>
{code}
</pre>""",
    "PROGRAM-NAME2": "root_prec",
    "PROGRAM-FILE2": "root_prec.c",
    "C-CODE2": """
int main() {
   return 0;
}
""",
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
    <th class="tg-0pky">Значение<br>степени корня</th>
    <th class="tg-0pky">Значение x</th>
    <th class="tg-0pky">Значение<br>количества итераций</th>
    <th class="tg-0pky">Ожидаемое значение<br>result</th>
    <th class="tg-0pky">Полученное значение<br>result</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">4</td>
  </tr>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2.5</td>
    <td class="tg-0pky">2.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">15</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">2</td>
  </tr>
  <tr>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">19</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">2.66840199518129895</td>
    <td class="tg-0pky">2.66840199518129895</td>
  </tr>
  <tr>
    <td class="tg-0pky">7</td>
    <td class="tg-0pky">925</td>
    <td class="tg-0pky">150</td>
    <td class="tg-0pky">2.65298340418130296</td>
    <td class="tg-0pky">2.65298340418130296</td>
  </tr>
  <tr>
    <td class="tg-0pky">текст</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">ошибка</td>
    <td class="tg-0pky">ошибка</td>
  </tr>
  <tr>
    <td class="tg-0pky">Ctrl + D</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">ошибка</td>
    <td class="tg-0pky">ошибка</td>
  </tr>
</tbody>
</table>
""",
    "TEST-EXAMPLES2": """
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Значение<br>степени корня</th>
    <th class="tg-0pky">Значение x</th>
    <th class="tg-0pky">Значение<br>эпсилон</th>
    <th class="tg-0pky">Ожидаемое значение<br>result</th>
    <th class="tg-0pky">Полученное значение<br>result</th>
    <th class="tg-0lax">Ожидаемое значение<br>количества итераций</th>
    <th class="tg-0lax">Полученное значение<br>количества итераций</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">10</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0lax">0</td>
    <td class="tg-0lax">0</td>
  </tr>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">2.5</td>
    <td class="tg-0pky">2.5</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
  </tr>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">0.00000000001</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0lax">6</td>
    <td class="tg-0lax">6</td>
  </tr>
  <tr>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">19</td>
    <td class="tg-0pky">0.00001</td>
    <td class="tg-0pky">2.66840164872198971</td>
    <td class="tg-0pky">2.66840164872198971</td>
    <td class="tg-0lax">9</td>
    <td class="tg-0lax">9</td>
  </tr>
  <tr>
    <td class="tg-0pky">7</td>
    <td class="tg-0pky">925</td>
    <td class="tg-0pky">0.00000000000001</td>
    <td class="tg-0pky">2.65298340418130296</td>
    <td class="tg-0pky">2.65298340418130296</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">4</td>
  </tr>
  <tr>
    <td class="tg-0pky">текст</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">ошибка</td>
    <td class="tg-0pky">ошибка</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Ctrl + D</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">ошибка</td>
    <td class="tg-0pky">ошибка</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
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
были рассмотрены базовые принципы работы построения программ на языке C и обработки целых
чисел:<br>
1. Организация ввода/вывода.<br>

2. Разработка функций.<br>

3. Объявление и использование переменных.<br>

4. Выполнение простейших арифметических операций над целочисленными операндами.<br>
""",
    **repl
}
