<style>
 #container {
   display: flex;
   flex-direction: row;
   flex-wrap: nowrap;
   justify-content: space-between;
 }
 #container > img {
   object-fit: contain;
 }
</style>

<p align="center">
   <font size="+1">
      Национальный исследовательский ядерный университет «МИФИ»<br><br>
      Институт интеллектуальных кибернетических систем<br><br>
      Кафедра №12 «Компьютерные системы и технологии»<br><br>
   </font>
</p>

<br>

<div id="container">
  <img width="200" alt="logo_mifi" src="_static/logo_mifi.png">
  <img width="200" alt="icis_logo" src="_static/icis_logo.jpg">
  <img width="200" alt="ksit_logo" src="_static/ksit_logo.svg">
</div>

<br><br><br>

<p align="center">
   <font size="+1">
      <b>
         <font size="+3">
            ОТЧЕТ<br>
         </font>
         О выполнении лабораторной работы №1<br>
         «Изучение принципов сложения целых чисел»<br>
      </b>
   </font>
</p>

<br><br><br><br><br><br><br><br><br><br>

```{mermaid}
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
```
