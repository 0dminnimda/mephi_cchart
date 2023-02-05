from private_data import repl

repl = {
    "LAB-ID": 4,
    "LAB-TITLE": "Работа со строками»",
    "STUDENT-NAME": "",
    "GROUP-ID": "",
    "TEACHER-NAME": "",
    "LOCATION": "Москва",
    "YEAR": 2023,
    "PROBLEM": """Вариант №12<br><br>
Индивидуальное задание:<br>
Удалить из строки слова, которые состоят из одинаковых символов. Например, слова «none», «one» и «neon» удовлетворяют указанному условию.""",
    "USED-DATA-TYPES": "При выполнении данной лабораторной работы использовался встроенный тип данных char, предназначенный для работы с символами и строками.",
    "GRAPH": """
<img width="400" alt="graph1" src="graphs_lab4/graph1.png">
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
<pre>
Average gnu to custom time ratio: 129.48298104360828
Minimum gnu to custom time ratio: 6.508752823788254
Maximum gnu to custom time ratio: 330.7712517619555

Input (first 50 characters)                           - Custom time  Gnu time     - Gnu to custom ratio
asdas sad fff fff ff f fghjhg                     ... - 0.0001595020 0.0035521984 - 22.270557109001768
                                                  ... - 0.0000052452 0.0000784397 - 14.954567985968122
a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa       ... - 0.0000119209 0.0011248589 - 94.36023286832369
a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaa... - 0.0000689030 0.0108642578 - 157.6746701885259
a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaa... - 0.0005664825 0.0855045319 - 150.93940571862325
a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaa... - 0.0054180622 0.9535932541 - 176.00264059353177
e3zvshdbS43brt3pRsVz0kSHzjrHdbMcJIx5WfMaB e3zvshdb... - 0.0000159740 0.0025219917 - 157.88103793664706
o85tBatcMzWKkLJqy9lvkXMy o85tBatcMzWKkLJqy9lvkXMy ... - 0.0000095367 0.0015232563 - 159.72572273427917
F7t4EPy8rEr OWi F7t4EPy8rEr OWi F7t4EPy8rEr OWi   ... - 0.0000064373 0.0011918545 - 185.14819877899117
vxSPKsh b                                         ... - 0.0000038147 0.0003261566 - 85.49993446404697
jkS8NMXw jkS8NMXw jkS8NMXw jkS8NMXw jkS8NMXw      ... - 0.0000059605 0.0005359650 - 89.91946984313397
e e e e e                                         ... - 0.0000040531 0.0001547337 - 38.17663023364832
yHeBTkW0xmdCpjLk0F 2eKDu7uaa 8ggYlxSrpDPLUVfvs8H2 ... - 0.0000164509 0.0029213428 - 177.57951236710454
ts097t84G9uz rgYvYQoccTJSQX6c7PHdvoo ts097t84G9uz ... - 0.0000128746 0.0021152496 - 164.29633542012954
hSnzXv9Uc61bulQ ZrP7lM0NxWAS hSnzXv9Uc61bulQ ZrP7l... - 0.0000061989 0.0008909702 - 143.7303715175273
Br77E76Zk7an8 Br77E76Zk7an8 Br77E76Zk7an8 Br77E76Z... - 0.0000069141 0.0008049011 - 116.41444294991396
uPfv5 uPfv5 uPfv5 uPfv5 uPfv5                     ... - 0.0000047684 0.0003836155 - 80.4495218521936
RExqEu RExqEu RExqEu                              ... - 0.0000045300 0.0004332066 - 95.63059602649007
gCWE91Wc9rxgI8vLAkUC1Cdhxe                        ... - 0.0000047684 0.0003449917 - 72.34957218354165
jyAqHqx w6bSz50GgxkUS1e9j4LiTg5DK5JqvdJQjukmQ3mG j... - 0.0000135899 0.0023734570 - 174.6485993274417
vykdM4YspWIDts3oPGz8zIPG3exmx4dTIETeNow5T0p vykdM4... - 0.0000095367 0.0015056133 - 157.87571172418131
8GEfCDQFPBgoRMmCP0CAqTFXUUrY 8GEfCDQFPBgoRMmCP0CAq... - 0.0000061989 0.0007505417 - 121.07659423446096
aAGbuDspi35vY9WRoN Pvi0dSsmX6vfWhXEUSVkYVxv aAGbuD... - 0.0000097752 0.0021378994 - 218.70646124887475
uzU9AuyGEahjtNjr8RQGXR7qRN2MZ0JCNRs syT 3NHPlXg3O ... - 0.0000169277 0.0040330887 - 238.2537911234249
3aShXn6xMFrWFHMzRwaY26Is853vp2jugYerX 3aShXn6xMFrW... - 0.0000085831 0.0015330315 - 178.6104670806585
LlekDd3DMOp9vdCf5ISL8H1R dTKWjTmyZXTyFvbzVvXMH3 Fn... - 0.0000233650 0.0038137436 - 163.22463513802694
JxHzz1oauQ uY JxHzz1oauQ uY JxHzz1oauQ uY JxHzz1oa... - 0.0000066757 0.0007035732 - 105.39317225159908
bB bB                                             ... - 0.0000033379 0.0001184940 - 35.49956559513466
vDLYISGJWyDwtfoEfnorZzAcoB vDLYISGJWyDwtfoEfnorZzA... - 0.0000054836 0.0006420612 - 117.08753373696112
mC1gz56Bg d1AYZUHn6wZe8P mC1gz56Bg d1AYZUHn6wZe8P ... - 0.0000083447 0.0011360645 - 136.14204225436504
6jjCa 6jjCa                                       ... - 0.0000035763 0.0001754761 - 49.06638145569443
RsMVUCSD RsMVUCSD RsMVUCSD RsMVUCSD RsMVUCSD      ... - 0.0000054836 0.0005400181 - 98.47875483259172
7cqrxakum9k0QVYB4tAAW9txpSesjyi97lDAUfXC 7cqrxakum... - 0.0000107288 0.0018975735 - 176.8672638132876
Ua5TFw3bt2y5mYUzn Ua5TFw3bt2y5mYUzn Ua5TFw3bt2y5mY... - 0.0000076294 0.0019876957 - 260.5310640417333
bYIQGFdkGQ AP4WbEwFeP0XQ6oK bYIQGFdkGQ AP4WbEwFeP0... - 0.0000216961 0.0024511814 - 112.9779729997557
U6qygAU f3ukD1QbseXfj ByRZYvWiNoh8zRHy0AC jVZIGM U... - 0.0000145435 0.0048105717 - 330.7712517619555
ouNtQ5EYMNj 4gGcUcW1i ouNtQ5EYMNj 4gGcUcW1i ouNtQ5... - 0.0000078678 0.0020022392 - 254.48526907140499
j9YxHOaGME 48uAtbTccUlC35F7BJLTivQnlmaMu i j9YxHOa... - 0.0000081062 0.0018677711 - 230.41265944585626
wWw1XAk9UICSwWCpNZduMJBB2Oz16 wWw1XAk9UICSwWCpNZdu... - 0.0000078678 0.0017893314 - 227.424616792496
tJsowhc5DU4KgbBFRmpgKylwZBHeX9isOKbO1xfWLxMLdtY3Fs... - 0.0000054836 0.0005953312 - 108.56575971989204
XCQeh54C ecuhNWLRjRc Qz4LrUUuKcLJ7OzofWbr XCQeh54C... - 0.0000140667 0.0032162666 - 228.64400321326252
6G 6G                                             ... - 0.0000033379 0.0001177788 - 35.285299140177955
q8qrtGi0z q8qrtGi0z                               ... - 0.0000040531 0.0002593994 - 64.00024672472921
wme3g1JuF                                         ... - 0.0000038147 0.0001528263 - 40.062468870422315
x6gRe8YVKdVs x6gRe8YVKdVs x6gRe8YVKdVs x6gRe8YVKdV... - 0.0000061989 0.0007481575 - 120.69197760893061
CW3                                               ... - 0.0000135899 0.0000884533 - 6.508752823788254
PSd U9aFi8gzFMBWTcerTVtQHWPRcES PSd U9aFi8gzFMBWTc... - 0.0000159740 0.0010678768 - 66.85093276574433
wLjY8babTcLg7GfQJS6ADJdrjZsdILezsS3y3nyDHI0 wLjY8b... - 0.0000166893 0.0009863377 - 59.100004194304134
P8i3brMRWH P8i3brMRWH                             ... - 0.0000040531 0.0002791882 - 68.88263304631023
DFa6jk6ayUS URyreITeA D5 DFa6jk6ayUS URyreITeA D5 ... - 0.0000061989 0.0005967617 - 96.2689670748036
70qCrhwBFf0 TmgMtJ9O5T2W9E 70qCrhwBFf0 TmgMtJ9O5T2... - 0.0000102520 0.0024714470 - 241.0697424892704
PRBeP2FlWKbTdvTPaODHsGl9eoII PRBeP2FlWKbTdvTPaODHs... - 0.0000059605 0.0006875992 - 115.35931549366663
diwpmj9m XVFEjU8 diwpmj9m XVFEjU8 diwpmj9m XVFEjU8... - 0.0000176430 0.0013923645 - 78.91880632545485
Cz7J9DXV47LA9bNX5VoFYj7VdHam5 Cz7J9DXV47LA9bNX5VoF... - 0.0000061989 0.0006878376 - 110.96123505783285
UUkKLANQH6G8GcNAwjGaiIDOgaDMGgbSK2KDnrH oshj9B    ... - 0.0000057220 0.0005536079 - 96.75076896190144
4HgMjknlU5QKuUAVtuDYoLUXAMRkphw6Z 4HgMjknlU5QKuUAV... - 0.0000081062 0.0011558533 - 142.5887962300461
</pre>""",
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
В ходе выполнения данной работы были рассмотрены принципы работы со строками в языке С:<br>
1. Устройство функции readline<br>
2. Функции из \<string.h\> и их устройство.<br>
""",
    **repl
}
