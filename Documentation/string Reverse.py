class NewString(str):
    def reverse(self):
        return self.__class__(self[::-1])  # casts to the specific type of self

string = NewString('Python')
rev = string.reverse()
print(rev)
# nohtyP
type(rev)
# NewString