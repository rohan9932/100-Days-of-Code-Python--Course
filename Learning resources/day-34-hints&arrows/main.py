# age: int
# name: str
# height: float
# is_human: bool


# type hint(expected output hints)
def police_check(age: int) -> bool:
    if age < 18:
        return False
    else:
        return True


# print(police_check("twelve")) # shows the error
print(police_check(19))
