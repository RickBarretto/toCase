from rb_tocase import Case

STRINGS = [

    "Hello World Haha", 
    "hello world haha",
    "HELLO WORLD HAHA",

    "Hello-World-Haha",
    "hello-world-haha",
    "HELLO-WORLD-HAHA",

    "Hello_World_Haha",
    "hello_world_haha",
    "HELLO_WORLD_HAHA",

    "HelloWorldHaha",
    "helloWorldHaha"
]

for s in STRINGS:

    try: 
        print(
            s, "=>\tCamel\t=>", Case.to_camel(s)
        )
    except:
        print("Can't change case for", s)
    try:
        print(
            s, "=>\tKebab\t=>", Case.to_kebab(s)
        )
    except:
        print("Can't change case for", s)
    try:
        print(
            s, "=>\tPascal\t=>", Case.to_pascal(s)
        )
    except:
        print("Can't change case for", s)
    try:
        print(
            s, "=>\tSentence\t=>", Case.to_sentence(s)
        )
    except:
        print("Can't change case for", s)
    try:
        print(
            s, "=>\tSnake\t=>", Case.to_snake(s)
        )
    except:
        print("Can't change case for", s)
    try:
        print(
            s, "=>\tUpperSnake\t=>", Case.to_upper_snake(s)
        )
    except:
        print("UpperSnake =>Can't change case for", s)