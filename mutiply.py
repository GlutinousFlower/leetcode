class Solution:
    """
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
    """
    def multiply(self, num1: str, num2: str) -> str:
        num3=int(num1)
        num4=int(num2)
        return str(num3*num4)

if __name__ == '__main__':
    print(Solution().multiply("9223372036854775807","2"))
