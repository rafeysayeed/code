class Solution(object):
    def fizzBuzz(self, n):
        return [[str(i), 'Fizz', 'Buzz', 'FizzBuzz'][(i%3==0)+(i%5==0)*2] for i in range(1, n+1)]