"""this program is used to write a multiplication table"""

def main():
    user_number = int(input("Enter the number for which you want multiplication table:"))
    counting_number = 12
    call_tables(user_number,counting_number)

def call_tables(user_number,counting_num):
    result = 1
    for i in range(0,counting_num+1):
        result = user_number * i
        print(user_number,"*",i,"=",result)

if __name__ == '__main__':
    main()
