class Tool:
    def my_print(self, n):
        for x in range(n):
            print(x, end=' ')
        print()


class A(Tool):
    def test1(self, n):
        self.my_print(n)

    def test2(self, m):
        self.my_print(m)


a = A()
a.test1(8)