from private_data import repl

repl = {
    "LAB-ID": 1,
    "STUDENT-NAME": "",
    "GROUP-ID": "",
    "TEACHER-NAME": "",
    "LOCATION": "Москва",
    "YEAR": 2022,
    "PROBLEM": "Вариант №1.12 Дано целое число. Поменять местами цифры числа так, чтотобы получилось минимальное цисло из этих цифр.",
    "USED-DATA-TYPES": "При выполнении данной лабораторной работы использовался встроенный тип данных int, предназначенный для работы с целыми числами.",
    "MERMAID-CODE": """
flowchart RL
   subgraph SG0 [" "]
      direction TB
      n0_0["maximize(n)"] --> n0_1["size = ceil(log10(n))"]
      n0_1 --> n0_2["sorted = 0"]
      n0_2 --> n0_3["sorted = 1"]
      n0_3 --> n0_4["offset = 1"]
      n0_4 --> n0_5{{"i = 0; i < size - 1; i++"}}
      n0_5 --> n0_13{"sorted != 1"}
      n0_13 --> |true| n0_3
      n0_5 --> n0_6["digit1 = n / (offset*10) % 10"]
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
""",
    "PROGRAM-NAME": "lab1",
    "PROGRAM-FILE": "lab1.c",
    "C-CODE": """
int main() {
   return 0;
}
""",
    "TEST-EXAMPLES": "",
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
чисел:
1. Организация ввода/вывода.

2. Разработка функций.

3. Объявление и использование переменных.

4. Выполнение простейших арифметических операций над целочисленными операндами.
""",
    **repl
}
