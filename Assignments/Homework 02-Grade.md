### Homework 1:
| #       | Item                                                       | Value       | Earned   |                |
|:--------|:-----------------------------------------------------------|:------------|:---------|:---------------|
| ***1*** | ***General***                                              |             |          |                |
| -       | Code was on github                                         | pass/fail   |          | ![Alt text][1] |
| -       | Code could be ran.                                         | pass/fail   |    -20   | ![Alt text][2] |
| -       | Code was commented                                         |    10       |    5    | ![Alt text][2] |
| ***2*** | ***Add Method***                                           |             |          |                |
| -       | Employed some kind of gcd method                           |    30       |    30    | ![Alt text][1] |
| -       | Handled a whole number portion of the fraction             |    30       |    30    | ![Alt text][1] |
| ***2*** | ***Overloaded Add Operator***                              |             |          |                |
| -       | `__add__` existed and worked                               |    30       |    10    | ![Alt text][3] |
|         | Totals:                                                    | **100**     |  **55** | ![Alt text][2] |

### Comments:
```
file was named incorrectly! should be named fraction_class.py 

Traceback (most recent call last):
  File "Homework 2", line 56, in <module>
    c = a + b
  File "Homework 2", line 51, in __add__
    self.__simple__(x,y)
  File "Homework 2", line 33, in __simple__
    common_divisor = gcd(self.numerator, self.denominator)
NameError: global name 'gcd' is not defined


If you are having trouble getting your code to run, you need to get help from me or Dr Griffin. Message him on slack or see him in his office! 
```

[1]: http://f.cl.ly/items/3E231i211n2E042B1U3K/right.png  "Correct"
[2]: http://f.cl.ly/items/2X473C1Q1F2x3S1E4231/wrong.gif  "Incorrect"
[3]: http://f.cl.ly/items/1A0d2Q1J1N1u0C3g0C1s/null.gif  "Errors"