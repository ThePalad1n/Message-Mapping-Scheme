'''
Evan Green
CmpSci 472
Spring 2022 with Prof Ganther
This program is to store text messages in a more efficent method
'''

def main():
    infile = input("Enter the text input file name: ")
    outfile = "msgout.txt"
    input_filename = infile + ".txt"
    input_file = open(input_filename, 'r')
    file_contents = input_file.read()
    input_file.close()
    word_list = file_contents.split()

    file = open(outfile, 'w')
    unique_words = set(word_list)
    for word in unique_words:
        file.write(str(word) + "\n")

    input_file = open(input_filename, 'r')
    lines = [line.rstrip() for line in input_file]

    print('Choices\n')
    num = len(lines)
    for x in range(num):
        print(x+1)
        print(lines[x]+"\n")
    choice = int(input("\nPlease select your choice: "))
    print("\n")
    choice = (lines[choice - 1])
    q = choice.split()
    new_list = list(unique_words)

    res = []
    i = 0
    while (i < len(new_list)):
        if (q.count(new_list[i]) > 0):
            res.append(i)
        i += 1

    v = [new_list[i] for i in res]

    final = (list(zip(*sorted(zip(sorted(v), sorted(enumerate(q), key=lambda x: x[1])),
                              key=lambda x: x[1][0])))[0])
    result = " ".join(str(x) for x in final)
    print(result + "\n")

    again()


def again():
    a = input("Would you like to choose again? Y/N  ")
    print("\n")
    r = a.upper()
    if r == 'Y':
        main()
    elif r == 'N':
        print("Goodbye")
        return 0
    else:
        print("try again")
        again()


main()