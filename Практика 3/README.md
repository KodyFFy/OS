# Практика 3
## __Язык выполнения C#__

____
# Поставленная задача:

### Краткое задание
Разработать программу, имитирующую работу склада (конвейера).

### Детальное задание
Требования к языку программирования: любой язык программирования

Разработать программу, имитирующую работу склада (конвейера).

Дано 3 производителя и 2 потребителя, все разные потоки и работают все одновременно.

Есть очередь с 200 элементами. Производители добавляют случайное число от 1…100, а потребители берут эти числа.

Если в очереди элементов >= 100 производители спят, если нет элементов в очереди - потребители спят.

Если элементов стало <= 80 производители просыпаются.

Все это работает до тех пор пока пользователь не нажал на кнопку “q”, после чего производители останавливаются, а потребители берут все элементы, только потом программа завершается.

