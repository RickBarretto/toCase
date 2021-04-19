from CopyCase import Case
import sys

tests = [
    "   Case TEST word 1 word2  ",
    "     CaseTestWord1Word2  ",
    "    Case_TEST_word1_word2  ",
    "    Case-TEST-word1-word2  ",
    "     CaseTEST word 1 word2  ",
    "   Case-TEST word1-word2  ",
    "    caseTestWord1Word3  ",
    "    CASE_TEST_WORD2_WORD3  ",
    "    CASE TEST WORD2 WORD3  ",
    "   casetest   ",
    "   CASETEST     ",
    "   Casetest   "
]

cases = [
    "lower", "upper", "title"
]

tabsize = 5

to_write = ["""
- Inputs = [
    "   Case TEST word 1 word2  ",
    "     CaseTestWord1Word2  ",
    "    Case_TEST_word1_word2  ",
    "    Case-TEST-word1-word2  ",
    "     CaseTEST word 1 word2  ",
    "   Case-TEST word1-word2  ",
    "    caseTestWord1Word3  ",
    "    CASE_TEST_WORD2_WORD3  ",
    "    CASE TEST WORD2 WORD3  ",
    "   casetest   ",
    "   CASETEST     ",
    "   Casetest   "
]

cases = [
    "lower", "upper", "title"
]


- Outputs:

"""]

print("[!] CamelCase:\n")
for test in tests:
    for case in cases:
        print(f"'{test.center(30)}'\t->\t'{Case.toCamel(test, case1=case)}' - case:{case} ".expandtabs(tabsize))
        to_write.append(f"'{test.center(30)}'\t->\t'{Case.toCamel(test, case1=case)}' - case:{case} ".expandtabs(tabsize))

print("\n[!] SnakeCase:\n")
for test in tests:
    for case in cases:
        print(f"'{test.center(30)}'\t->\t'{Case.toSnake(test, case1=case)}' - case:{case} ".expandtabs(tabsize))
        to_write.append(f"'{test.center(30)}'\t->\t'{Case.toSnake(test, case1=case)}' - case:{case} ".expandtabs(tabsize))

print("\n[!] KebabCase:\n")
for test in tests:
    for case in cases:
        print(f"'{test.center(30)}'\t->\t'{Case.toKebab(test, case1=case)}' - case:{case} ".expandtabs(tabsize))
        to_write.append(f"'{test.center(30)}'\t->\t'{Case.toKebab(test, case1=case)}' - case:{case} ".expandtabs(tabsize))

print("\n[!] PascalCase:\n")
for test in tests:
    for case in cases:
        print(f"'{test.center(30)}'\t->\t'{Case.toPascal(test, case1=case)}' - case:{case} ".expandtabs(tabsize))
        to_write.append(f"'{test.center(30)}'\t->\t'{Case.toPascal(test, case1=case)}' - case:{case} ".expandtabs(tabsize))

print("\n[!] UpperSnakeCase:\n")
for test in tests:
    for case in cases:
        print(f"'{test.center(30)}'\t->\t'{Case.toUpperSnake(test)}' - case:{case} ".expandtabs(tabsize))
        to_write.append(f"'{test.center(30)}'\t->\t'{Case.toUpperSnake(test)}' - case:{case} ".expandtabs(tabsize))

print("\n[!] Sentence:\n")
for test in tests:
    for case in cases:
        print(f"'{test.center(30)}'\t->\t'{Case.toSentence(test, case1=case)}' - case:{case} ".expandtabs(tabsize))
        to_write.append(f"'{test.center(30)}'\t->\t'{Case.toSentence(test, case1=case)}' - case:{case} ".expandtabs(tabsize))

def writing():
    f = open("./result.txt", "a")
    f.truncate(0)
    for line in to_write:
        f.writelines(line + "\n")
    f.close()   

writing()