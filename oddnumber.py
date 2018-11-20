"""input name and print odd number"""
def main():
    name = get_name()
    num = int(input("Enter the skip value"))
    print_name(name, num)

def print_name(name,num):
    print{name[::num]}
    