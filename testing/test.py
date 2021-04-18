from ToCase import Case

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

print("CamelCase:")
for test in tests:
    print(Case.toCamel(test))
print("\nSnakeCase:")
for test in tests:
    print(Case.toSnake(test))
print("\nKebabCase:")
for test in tests:
    print(Case.toKebab(test))
print("\nPascalCase:")
for test in tests:
    print(Case.toPascal(test))
print("\nUpperSnakeCase:")
for test in tests:
    print(Case.toUpperSnake(test))
print("\nSentence")
for test in tests:
    print(Case.toSentence(test))