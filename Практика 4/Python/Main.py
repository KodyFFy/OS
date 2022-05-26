import datetime

timer_start = datetime.datetime.now()

i = 0

fun_sum = 0

b = int(input("Число b: "))
c = int(input("Число c: "))

while i <= 100000000:
    fun_sum += b * 2 + c - i
    i += 1


print(fun_sum)
timer_end = datetime.datetime.now()
print(f"Затраченное время: {timer_end - timer_start}")
