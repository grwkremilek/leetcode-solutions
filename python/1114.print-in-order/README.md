# Print in Order

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().


python

#### Runtime: 44 ms, faster than 45.82%         #locks

#### Runtime: 36 ms, faster than 76.36%         #semaphores

#### Runtime: 36 ms, faster than 76.36%         #events


cpp

#### Runtime: 140 ms, faster than 76.55%        #semaphores
