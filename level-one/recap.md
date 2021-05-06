# Recap

### Problem 1

The challenge was to figure out what the largest amount of equal slices a given string could be split into.

#### Approach 1

The initial idea was to iterate through the string for each possible string slice and check to see the subsequent slices were equal all the way through

This is not the ideal way to solve this problem as the algorithm runs in O(n2).

#### Approach 2

There's a way to obtain the solution with only one iteration through the string.

1. Keep track of the current string slice size as you iterate starting with a size of 1.

2. Check to see if the string can be split into equal parts with current slice size

3. Check and see if the current index is equal to the index one string slice behind the current

4. if both true continue

5. if not set the new string slice to the current index + 1

6. at the end of iteration check to see if the stringSlice is less than the string length / 2

7. if so return string slice

8. else return 1 or null
