import sys

def downcase_it(text):
    return text.lower()

if len(sys.argv) == 1:
    print("none")

else:
    x = sys.argv[1:]
    for i in x:
        print(downcase_it(i))