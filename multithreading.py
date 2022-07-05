def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()



# write(3)
# write(8)
# write(1)

# [1, 8, 3]

# read() -> 3, After:  [1, 8]

# //
# // Producer / Consumer with a Bounded Queue
# //

# void write(int value) 
# {
  
# }

# // Consumer Thread 2

# int read() 
# {

# }
import threading

queue = []
maxSize = 64

def write(val):
    while len(queue) >= 64:
        continue
    queue.insert(val,0)

def read():
    while len(queue) == 0:
        continue
    return queue.pop()

th1 = threading.Thread(target = write, args = (queue))
th2 = threading.Thread(target = read, args = (queue))
th1.start()
th2.start()

# // Thread 1
# write(1);
# write(2);
# write(3); <-- Queue is Full (How do we block this thread from continguign to the next line?
# write(4);

# // Thread 2
# // while (true) { read(); }