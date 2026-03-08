
# Python Pattern Printing: 12 Fun Loop Exercises for Beginners

---

## Run This Code Online Easily

You can run all the Python code in this guide online without installing anything!

Just visit: [Run Python on Trinket.io](https://trinket.io/embed/python3)

Paste the code into the editor and press the "Run" button. This is a great way to experiment and learn patterns interactively.

---

This guide explains how each pattern in `trianngle.py` is built.

It is written for students who are learning:
- `for` loops
- nested loops
- arithmetic expressions inside loops
- how row/column logic translates into visual output

---

## 1. Core Ideas You Need First

### 1.1 Outer Loop vs Inner Loop

In all patterns:
- The **outer loop** (`for i in range(row)`) controls the current line number.
- The **inner loop(s)** decide what gets printed on that line.

Think like this:
- `i` = which row am I printing right now?
- inner loop count = how many spaces or stars should this row have?

### 1.2 How `range(n)` Works

`range(n)` generates numbers from `0` to `n - 1`.

So:
- `range(6)` -> `0, 1, 2, 3, 4, 5`
- length of `range(6)` is `6`

This is why loop counts use formulas like `i + 1`, `row - i`, and `2 * i + 1`.

### 1.3 Why `print(..., end="")` Is Used

- `print("*", end="")` prints without moving to the next line.
- `print()` alone moves to the next line.

So each row usually does:
1. print spaces/stars with `end=""`
2. call `print()` once to finish that row

### 1.4 Row Indexing

With `row = 6`, outer loop `i` goes `0..5`.

That means:
- first row is `i = 0`
- last row is `i = row - 1`

Most formulas are built around this.

---

## 2. Pattern 1: Left Triangle


Code:
```python
for i in range(row):
    for j in range(i + 1):
        print("*", end="")
    print()
```

Output (`row = 6`):
```
*
**
***
****
*****
******
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | * | * | * | * | * | * |
| 1 | * | * | * | * | * | * |
| 2 | * | * | * | * | * | * |
| 3 | * | * | * | * | * | * |
| 4 | * | * | * | * | * | * |
| 5 | * | * | * | * | * | * |

### Loop Construction
1. Outer loop runs `row` times -> total rows.
2. Inner loop also runs `row` times -> stars per row.


### Step-by-Step Example
Let’s see what happens for `row = 4`:

| Row (i) | Stars Printed |
|---------|--------------|
|   0     |   4          |
|   1     |   4          |
|   2     |   4          |
|   3     |   4          |

So, every row prints 4 stars!

### Math Behind It
- Rows = `row`
- Columns (stars) per row = `row`
- Total stars = `row * row`

For `row = 6`: total stars = `36`.

---

## 3. Pattern 2: Right Triangle


Code:
```python
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
```

Output:
```
     *
    **
   ***
  ****
 *****
******
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | * |   |   |   |   |   |
| 1 | * | * |   |   |   |   |
| 2 | * | * | * |   |   |   |
| 3 | * | * | * | * |   |   |
| 4 | * | * | * | * | * |   |
| 5 | * | * | * | * | * | * |

### Loop Construction
1. Outer loop picks row `i`.
2. On row `i`, print `i + 1` stars.

Why `i + 1`?
- If `i = 0`, you still want 1 star (not 0).
- If `i = 5`, you want 6 stars.


### Step-by-Step Example
Let’s see what happens for `row = 5`:

| Row (i) | Stars Printed | Output |
|---------|--------------|--------|
|   0     |   1          | *      |
|   1     |   2          | **     |
|   2     |   3          | ***    |
|   3     |   4          | ****   |
|   4     |   5          | *****  |

### Math Behind It
Stars per row = `i + 1`

Total stars:
`1 + 2 + 3 + ... + row = row * (row + 1) / 2`

For `row = 6`: total stars = `6 * 7 / 2 = 21`.

---

## 4. Pattern 3: Reverse Triangle


Code:
```python
for i in range(row):
    for j in range(row - i):
        print("*", end="")
    print()
```

Output:
```text
******
*****
****
***
**
*
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | * | * | * | * | * | * |
| 1 | * | * | * | * | * |   |
| 2 | * | * | * | * |   |   |
| 3 | * | * | * |   |   |   |
| 4 | * | * |   |   |   |   |
| 5 | * |   |   |   |   |   |

### Loop Construction
1. Outer loop picks row `i`.
2. Start with full width (`row`) and reduce by 1 each row.
3. Stars count is `row - i`.

### Math Behind It
- At `i = 0`: stars = `row`
- At `i = row - 1`: stars = `1`

This is the reverse of Pattern 2.
Total stars is still:
`row * (row + 1) / 2`

### Step-by-Step Example
For `row = 5`:

| Row (i) | Stars Printed | Output |
|---------|--------------|--------|
|   0     |   5          | *****  |
|   1     |   4          | ****   |
|   2     |   3          | ***    |
|   3     |   2          | **     |
|   4     |   1          | *      |

---

## 5. Pattern 4: Centered Pyramid


Code:
```python
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
```

Output:
```text
     *
    **
   ***
  ****
 *****
******
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 |   |   |   |   |   | * |
| 1 |   |   |   |   | * | * |
| 2 |   |   |   | * | * | * |
| 3 |   |   | * | * | * | * |
| 4 |   | * | * | * | * | * |
| 5 | * | * | * | * | * | * |

### Loop Construction
Each row has 2 parts:
1. Leading spaces
2. Stars

For row `i`:
- spaces = `row - i - 1`
- stars = `i + 1`

### Math Behind It
`spaces + stars = row`

Check row by row:
- `i = 0`: spaces 5, stars 1
- `i = 5`: spaces 0, stars 6

That is exactly right alignment.

### Step-by-Step Example
For `row = 5`:

| Row (i) | Spaces | Stars | Output |
|---------|--------|-------|--------|
|   0     |   4    |   1   |    *   |
|   1     |   3    |   2   |   **   |
|   2     |   2    |   3   |  ***   |
|   3     |   1    |   4   | ****   |
|   4     |   0    |   5   |*****   |

---

## 6. Pattern 5: Inverted Pyramid


Code:
```python
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for j in range((row - i) * 2 - 1):
        print("*", end="")
    print()
```

Output:
```text
******
 *****
  ****
   ***
    **
     *
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | * | * | * | * | * | * |
| 1 |   | * | * | * | * | * |
| 2 |   |   | * | * | * | * |
| 3 |   |   |   | * | * | * |
| 4 |   |   |   |   | * | * |
| 5 |   |   |   |   |   | * |

### Loop Construction
Again 2 parts:
1. Leading spaces increase each row: `i`
2. Stars decrease each row: `row - i`

### Math Behind It
`spaces + stars = row`

This is the opposite direction of Pattern 4.

### Step-by-Step Example
For `row = 5`:

| Row (i) | Spaces | Stars | Output |
|---------|--------|-------|--------|
|   0     |   0    |   5   |*****   |
|   1     |   1    |   4   | ****   |
|   2     |   2    |   3   |  ***   |
|   3     |   3    |   2   |   **   |
|   4     |   4    |   1   |    *   |

---

## 7. Pattern 6: Number Triangle

Code:
```python
for i in range(row):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()
```

Output:
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
```

---

## 8. Pattern 7: Floyd's Triangle

Code:
```python
num = 1
for i in range(row):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()
```

Output:
```
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
```

Code:
```python
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for p in range(i * 2 + 1):
        print("*", end="")
    print()
```

Output:
```text
     *
    ***
   *****
  *******
 *********
***********
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 |   |   |   |   |   | * |
| 1 |   |   |   |   | * | * | * |
| 2 |   |   |   | * | * | * | * | * |
| 3 |   |   | * | * | * | * | * | * | * |
| 4 |   | * | * | * | * | * | * | * | * | * |
| 5 | * | * | * | * | * | * | * | * | * | * | * |

### Loop Construction
Each row has:
1. leading spaces
2. odd number of stars

For row `i`:
- spaces = `row - i - 1`
- stars = `2 * i + 1`

### Math Behind It
Why odd numbers?
- Centered pyramid width sequence is `1, 3, 5, 7, ...`
- formula for nth odd number from 0-indexed row `i` is `2 * i + 1`

Total stars in first `row` odd numbers is:
`row^2`

For `row = 6`: total stars = `36`.

### Step-by-Step Example
For `row = 4`:

| Row (i) | Spaces | Stars | Output   |
|---------|--------|-------|----------|
|   0     |   3    |   1   |   *      |
|   1     |   2    |   3   |  ***     |
|   2     |   1    |   5   | *****    |
|   3     |   0    |   7   |*******   |

---

## 9. Pattern 8: Hollow Triangle (Centered)

Code:
```python
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == row - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
```

Output:
```
     *
    * *
   *   *
  *     *
 *       *
***********
```

Code:
```python
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for p in range((row - i) * 2 - 1):
        print("*", end="")
    print()
```

Output:


```text
***********
 *********
  *******
   *****
    ***
     *
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | * | * | * | * | * | * | * | * | * | * | * |
| 1 |   | * | * | * | * | * | * | * | * | * |
| 2 |   |   | * | * | * | * | * | * | * |
| 3 |   |   |   | * | * | * | * | * |
| 4 |   |   |   |   | * | * | * |
| 5 |   |   |   |   |   | * |

---

## 10. Pattern 9: Pascal's Triangle

Code:
```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        val = factorial(i) // (factorial(j) * factorial(i - j))
        print(val, end=" ")
    print()
```

Output:
```
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 
1 5 10 10 5 1 
```

Code:
```python
# Top pyramid
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for p in range(i * 2 + 1):
        print("*", end="")
    print()
# Bottom inverted pyramid (skip the middle row to avoid duplicate)
for i in range(1, row):
    for j in range(i):
        print(" ", end="")
    for p in range((row - i) * 2 - 1):
        print("*", end="")
    print()
```

Output (row = 6):
```text
     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
```

#### 6x6 Grid Visual (centered)
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|----|
| 0 |   |   |   |   |   | * |   |   |   |   |    |
| 1 |   |   |   |   | * | * | * |   |   |   |    |
| 2 |   |   |   | * | * | * | * | * |   |   |    |
| 3 |   |   | * | * | * | * | * | * | * |   |    |
| 4 |   | * | * | * | * | * | * | * | * | * |    |
| 5 | * | * | * | * | * | * | * | * | * | * | *  |
| 6 |   | * | * | * | * | * | * | * | * | * |    |
| 7 |   |   | * | * | * | * | * | * | * |   |    |
| 8 |   |   |   | * | * | * | * | * |   |   |    |
| 9 |   |   |   |   | * | * | * |   |   |   |    |
|10 |   |   |   |   |   | * |   |   |   |   |    |

---

## 11. Pattern 10: Diamond

Code:
```python
# Top pyramid
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
# Bottom inverted pyramid (skip the middle row to avoid duplicate)
for i in range(1, row):
    for j in range(i):
        print(" ", end="")
    for j in range((row - i) * 2 - 1):
        print("*", end="")
    print()
```

Output (`row = 6`):
```
     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
```

---

## 12. Pattern 11: Right Reverse Triangle

Code:
```python
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for j in range(row - i):
        print("*", end="")
    print()
```

Output (`row = 6`):
```
******
 *****
  ****
   ***
    **
     *
```

---

## 13. Pattern 12: Pascal's Triangle

Code:
```python
# Top left-increasing
for i in range(row):
    for j in range(i + 1):
        print("*", end="")
    print()
# Bottom left-decreasing (skip the middle row to avoid duplicate)
for i in range(row - 1):
    for j in range(row - i - 1):
        print("*", end="")
    print()
```

Output (row = 6):
```text
*
**
***
****
*****
******
*****
****
***
**
*
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | * |   |   |   |   |   |
| 1 | * | * |   |   |   |   |
| 2 | * | * | * |   |   |   |
| 3 | * | * | * | * |   |   |
| 4 | * | * | * | * | * |   |
| 5 | * | * | * | * | * | * |
| 6 | * | * | * | * | * |   |
| 7 | * | * | * | * |   |   |
| 8 | * | * | * |   |   |   |
| 9 | * | * |   |   |   |   |
|10 | * |   |   |   |   |   |

---

## 11. Pattern 10: Right Hourglass (Right Increasing + Right Decreasing)

Code:
```python
# Top right-increasing
for i in range(row):
    for j in range(row - i - 1):
        print(" ", end="")
    for p in range(i + 1):
        print("*", end="")
    print()
# Bottom right-decreasing (skip the middle row to avoid duplicate)
for i in range(row - 1):
    for j in range(i + 1):
        print(" ", end="")
    for p in range(row - i - 1):
        print("*", end="")
    print()
```

Output (row = 6):
```text
     *
    **
   ***
  ****
 *****
******
 *****
  ****
   ***
    **
     *
```

#### 6x6 Grid Visual
|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 |   |   |   |   |   | * |
| 1 |   |   |   |   | * | * |
| 2 |   |   |   | * | * | * |
| 3 |   |   | * | * | * | * |
| 4 |   | * | * | * | * | * |
| 5 | * | * | * | * | * | * |
| 6 |   | * | * | * | * | * |
| 7 |   |   | * | * | * | * |
| 8 |   |   |   | * | * | * |
| 9 |   |   |   |   | * | * |
|10 |   |   |   |   |   | * |

### Loop Construction
For row `i`:
- spaces = `i` (increase each row)
- stars = `(row - i) * 2 - 1` (odd numbers decreasing)

### Math Behind It
At `i = 0`: stars = `2 * row - 1` (maximum width)
At `i = row - 1`: stars = `1`

It is the upside-down version of Pattern 6.

### Step-by-Step Example
For `row = 4`:

| Row (i) | Spaces | Stars | Output   |
|---------|--------|-------|----------|
|   0     |   0    |   7   |*******   |
|   1     |   1    |   5   | *****    |
|   2     |   2    |   3   |  ***     |
|   3     |   3    |   1   |   *      |

---

## 9. Step-by-Step Thinking Process (Use for Any New Pattern)

When building a pattern, ask these in order:

1. How many rows?  
Usually `row`.

2. What changes each row?  
- spaces increasing or decreasing?
- stars increasing or decreasing?

3. Write row formulas in terms of `i`.
- increase: often `i`, `i + 1`, `2 * i + 1`
- decrease: often `row - i`, `row - i - 1`, `2 * (row - i) - 1`

4. Convert each formula into one inner loop.

5. Test first row (`i = 0`) and last row (`i = row - 1`).

6. If alignment is wrong, check spaces formula first.

---

## 9.1. Example: Building a Right-Aligned Triangle (Pattern 4)

Let’s walk through the first 3 rows for `row = 5`:

| i | spaces = 5 - i - 1 | stars = i + 1 | Output |
|---|--------------------|--------------|--------|
| 0 |        4           |      1       |    *   |
| 1 |        3           |      2       |   **   |
| 2 |        2           |      3       |  ***   |

See how the spaces go down and the stars go up!

---

## 10. Common Mistakes and Fixes

1. `range()` missing value or wrong formula
- Mistake: `range()` with no argument.
- Fix: always pass an integer expression like `range(i + 1)`.

2. Off-by-one errors
- Mistake: using `row - i` when you needed `row - i - 1`.
- Fix: test with `i = 0` and `i = row - 1`.

3. Forgetting `print()` at the end of each row
- Result: all output appears in one line.

4. Mixing up spaces and stars order
- For right-aligned patterns, spaces must be printed before stars.

---

## 11. Time Complexity and Space Complexity

For all these patterns:
- Time complexity: about `O(row^2)` because nested loops run many times.
- Extra space complexity: `O(1)` (ignoring output), since only loop variables are used.

---

## 12. Practice Tasks for Students

1. Change all `*` to `#`.
2. Try `row = 3`, `row = 8`, `row = 10` and verify formulas.
3. Create a diamond by combining Pattern 6 and Pattern 7.
4. Build a pattern with numbers instead of stars.
5. Print right-aligned triangle using visible space symbol (example `o`).

---

## 13. Quick Formula Cheat Sheet

- Pattern 1 (square): `stars = row`
- Pattern 2 (left increasing): `stars = i + 1`
- Pattern 3 (left decreasing): `stars = row - i`
- Pattern 4 (right increasing): `spaces = row - i - 1`, `stars = i + 1`
- Pattern 5 (right decreasing): `spaces = i`, `stars = row - i`
- Pattern 6 (pyramid): `spaces = row - i - 1`, `stars = 2 * i + 1`
- Pattern 7 (inverted pyramid): `spaces = i`, `stars = 2 * (row - i) - 1`

Use these as building blocks for almost every beginner pattern-printing exercise.
