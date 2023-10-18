import pytest
# import pytest_check as check


def test_first():
    # check.is_true(True, "test_first should be true")
    assert True == False


@pytest.mark.depends(on=['test_second'])
def test_third():
    # check.is_true(True, "test_third should be true")
    pass


@pytest.mark.depends(on=['test_first'])
def test_second():
    # check.is_true(False, "test_second should be true")
    print("a")


class sai():
    def __init__(self,name,gender) -> None:
        self.name=name
        self.gender=gender
        self.c=2023
        print(self.c)

    def s1(self,birthyear):
        print(f'name {self.name} gender {self.gender} age {self.c-birthyear}')
    #overloading
    def s1(self,birthyear,son):
        print(f'name {self.name} gender {self.gender} age {self.c-birthyear} {son}')

class s2(sai):
    def __init__(self, name, gender) -> None:
        super().__init__(name, gender)
    def s1(self,birthyear):
        print(f'name {self.name} gender {self.gender} age {self.c-birthyear+2}')

s=sai("sai","Male")
s.s1(1998)


s=s2("sai","Male")
s.s1(1998)

