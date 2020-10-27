# See how the Ackermann function works!

I implemented the [two argument Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function) in Python and added a print for each recursive call so you can see what's going on. Just clone this repo (or even copy the script into your own file), navigate to the script, and run `python3 ackermann.py m n`, where `m` and `n` are the two nonnegative arguments to the Ackermann function. For `python3 ackermann.py 1 2`, you should see 

```
% python3 ackermann.py 1 2
(1, 2)
 (1, 1)
  (1, 0)
   (0, 1)
  (0, 2)
 (0, 3)

ack(1, 2) = 4
```

Warning: the Ackermann function is famous because it gives computers a headache. Expect a `RecursionError` when running `ackermann.py` with `m` > 3. `n` can go approx two orders of magnitude higher. 

Enjoy!
