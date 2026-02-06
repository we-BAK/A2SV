class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr=[]
        for i in range(1,n+1):
            three=i%3==0
            five=i%5==0
            if three and five:
                arr.append("FizzBuzz")
            elif three:
                arr.append("Fizz")
            elif five:
                arr.append("Buzz")
            else: 
                arr.append(str(i))
        return arr

