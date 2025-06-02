class Test_Class:
    def __init__(self) -> None:
        self.msg = 'Hello world!'

    def test_method(self) -> None:
        print(self.msg)

    def zest_method(self) -> None:
        #zest before test
        print('zest')

testClass = Test_Class()
testClass.zest_method()
testClass.test_method()
