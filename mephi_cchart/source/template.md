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
         О выполнении лабораторной работы №{LAB-ID}<br>
         «Изучение принципов сложения целых чисел»<br>
      </b>
   </font>
</p>

<br><br><br><br><br><br><br><br><br><br>

<p align="right">
   <b>Студент:</b> {STUDENT-NAME}<br>
   <b>Группа:</b> {GROUP-ID}<br>
   <b>Преподаватель:</b> {TEACHER-NAME}<br>
</p>

<p align="center">
   {LOCATION} — {YEAR}
</p>

<font size="+2"><b>1. Формулировка индивидуального задания<b></font>

{PROBLEM}

<font size="+2"><b>2. Описание использованных типов данных<b></font>

{USED-DATA-TYPES}

<font size="+2"><b>3. Описание использованного алгоритма<b></font>

```{mermaid}
{MERMAID-CODE}
```

<font size="+2"><b>4. Исходные коды разработанных программ<b></font>

Листинг 1: Исходные коды программы {PROGRAM-NAME} (файл: {PROGRAM-FILE})

<pre>
{C-CODE}
</pre>

<font size="+2"><b>5. Описание тестовых примеров<b></font>

{TEST-EXAMPLES}

<font size="+2"><b>6. Скриншоты<b></font>

<img width="400" alt="terminal" src="terminal.png">

Рис. 3: Сборка и запуск программы {PROGRAM-NAME}

<font size="+2"><b>7. Выводы<b></font>

{CONCLUSIONS}
