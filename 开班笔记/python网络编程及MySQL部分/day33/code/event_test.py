from multiprocessing import Event
#创建事件
e = Event()

print(e.is_set())

e.set()

e.wait()
print(e.is_set())

e.clear()
