list1=[11,-21,0,45,66,-93]
positive=[pos for pos in list1 if pos>=0]
print("positive number : ",positive)

n=int(input("\nEnter nth Number : "))
print("Square : ",[s*s for s in range(1,n+1)])

def check_vow(string,vowels):
    final=[each for each in string if each in vowels]
    print("\ntotal vowels: ",len(final))
    print(final,"\n")
string="Geeks for Geeks is doing good job"
vowels="AaEeIiOoUu"
check_vow(string,vowels)

word="hallucination"
print("ordinale values : ",[ord(each) for each in word])


