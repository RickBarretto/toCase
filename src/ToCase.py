import re


class Case:
    

    def toCamel(string: str, case: str = "lower"):
        string = string.strip()
        print("String:", string)
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            _list = string.split(" ")
            first = _list[0].lower()
            print("first:", first)
            last = []
            for i in _list[1:]:
                last.append(i.title())
            last = "".join(last)
            print("last:", last)
            sentence = str(first + last)
            return sentence
        
        # For Snakes:
        elif len(string.split("_")) > 1:
            print("Is a Snake")
            _list = string.split("_")
            first = _list[0].lower()
            print("first:", first)
            last = []
            for i in _list[1:]:
                last.append(i.title())
            last = "".join(last)
            print("last:", last)
            snake = str(first + last)
            return snake
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            _list = string.split("-")
            first = _list[0].lower()
            print("first:", first)
            last = []
            for i in _list[1:]:
                last.append(i.title())
            last = "".join(last)
            print("last:", last)
            kebab = str(first + last)
            return kebab
    
        # For Uppers:
        elif string.isupper():
            if case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Lowers:
        elif string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Titles:
        elif string.istitle():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal:
        else:
            print("Is a Pascal")
            _list = re.findall('[A-Z][^A-Z]*', string)
            first = _list[0].lower()
            last = _list[1:]
            print("first:", first)
            print("last:", last)
            last = "".join(last)
            pascal = first + last
            return pascal

            

    def toSnake(string: str, case: str = "lower"):
        string = string.strip()
        print("String:", string)
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            _list = string.split(" ")
            last = []
            for i in _list:
                last.append(i.lower())
            sentence = "_".join(last)
            print("sentence:", sentence)
            return sentence
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            _list = string.split("-")
            last = []
            for i in _list:
                last.append(i.lower())
            kebab = "_".join(last)
            print("kebab:", kebab)
            return kebab
    
        # For Uppers:
        elif string.isupper():
            if case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Lowers:
        elif string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Titles:
        elif string.istitle():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal/Camel:
        else:
            last = re.findall('[A-Z][^A-Z]*', string)
            print("last", last)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break
            print("index:", index)
            if index == 0:
                print("Is a Pascal")
                first = ""
                print("first: None")
                l = []
                for i in last:
                    l.append(i.lower())
                print("list:", l)
                pascal = str("_".join(l))
                return pascal
            else:
                print("Is a Camel")
                first = string[:index]
                print("first:", first)
                l = []
                for i in last:
                    l.append(i.lower())
                print("list:", l)
                r = str("_".join(l))
                camel = first + "_" + r
                return camel
            


    def toKebab(string: str, case: str = "lower"):
        string = string.strip()
        print("String:", string)
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            _list = string.split(" ")
            last = []
            for i in _list:
                last.append(i.lower())
            sentence = "-".join(last)
            print("sentence:", sentence)
            return sentence
        
        # For Snake:
        elif len(string.split("_")) > 1:
            print("Is a Kebab")
            _list = string.split("_")
            last = []
            for i in _list:
                last.append(i.lower())
            snake = "-".join(last)
            print("snake:", snake)
            return snake
    
        # For Uppers:
        elif string.isupper():
            if case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Lowers:
        elif string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Titles:
        elif string.istitle():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal/Camel:
        else:
            last = re.findall('[A-Z][^A-Z]*', string)
            print("last", last)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break
            print("index:", index)
            if index == 0:
                print("Is a Pascal")
                first = ""
                print("first: None")
                l = []
                for i in last:
                    l.append(i.lower())
                print("list:", l)
                pascal = str("-".join(l))
                return pascal
            else:
                print("Is a Camel")
                first = string[:index]
                print("first:", first)
                l = []
                for i in last:
                    l.append(i.lower())
                print("list:", l)
                r = str("-".join(l))
                camel = first + "-" + r
                return camel



    def toPascal(string: str, case: str = "lower"):
        string = string.strip()
        print("String:", string)
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            _list = string.split(" ")
            l = []
            for i in _list:
                l.append(i.title())
            l = "".join(l)
            sentence = l
            return sentence
        
        # For Snakes:
        elif len(string.split("_")) > 1:
            print("Is a Snake")
            _list = string.split("_")
            l = []
            for i in _list:
                l.append(i.title())
            l = "".join(l)
            snake = l
            return snake
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            _list = string.split("-")
            l = []
            for i in _list:
                l.append(i.title())
            l = "".join(l)
            kebab = l
            return kebab
    
        # For Uppers:
        elif string.isupper():
            if case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Lowers:
        elif string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
        # For Titles:
        elif string.istitle():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Camel:
        else:
            print("Is a Camel")
            last = re.findall('[A-Z][^A-Z]*', string)
            print("last", last)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break
            print("index:", index)
            first = string[:index].title()
            print("first:", first)
            l = []
            for i in last:
                l.append(i.title())
            print("list:", l)
            l = "".join(l)
            camel = first + l
            return camel



    def toUpperSnake(string: str):
        
        # For Lowers, Uppers and Titles:
        if string.islower() or string.isupper() or string.istitle():
            string = string.strip()
            print("Was returned a upper case, because the string has no differentiator")
            return string.upper()
        else:
            return Case.toSnake(string).upper()



    def toSentence(string: str, case: str = "lower"):
        string = string.strip()
        print("String:", string)

        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            l = []
            for i in string.split():
                if case == "lower":
                        l.append(i.lower())
                elif case == "upper":
                        l.append(i.upper())
                elif case == "title":
                        l.append(i.title())
            sentence = " ".join(l)
            return sentence
        
        # For Snake:
        elif len(string.split("_")) > 1:
            print("Is a Snake")
            _list = string.split("_")
            last = []
            for i in _list:
                if case == "lower":
                    last.append(i.lower())
                elif case == "upper":
                    last.append(i.upper())
                elif case == "title":
                    last.append(i.title())
                else:
                    raise ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
            snake = " ".join(last)
            print("Snake:", snake)
            return snake
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            _list = string.split("-")
            last = []
            for i in _list:
                if case == "lower":
                    last.append(i.lower())
                elif case == "upper":
                    last.append(i.upper())
                elif case == "title":
                    last.append(i.title())
                else:
                    raise ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
            kebab = " ".join(last)
            print("Kebab:", kebab)
            return kebab
    
        # For Uppers:
        elif string.isupper():
            if case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.title()
            else:
                raise ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
        # For Lowers:
        elif string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.title()
            else:
                raise ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
        # For Titles:
        elif string.istitle():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string
            else:
                raise ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal/Camel:
        else:
            last = re.findall('[A-Z][^A-Z]*', string)
            print("last", last)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break
            print("index:", index)

            if index == 0:
                print("Is a Pascal")
                first = ""
                print("first: None")
                l = []
                for i in last:
                    if case == "lower":
                        l.append(i.lower())
                    elif case == "upper":
                        l.append(i.upper())
                    elif case == "title":
                        l.append(i.title())
                print("list:", l)
                pascal = str(" ".join(l))
                return pascal
            
            else:
                print("Is a Camel")
                first = string[:index]
                if case == "lower":
                        first = first.lower()
                elif case == "upper":
                        first = first.upper()
                elif case == "title":
                        first = first.title()
                print("first:", first)
                l = []
                for i in last:
                    if case == "lower":
                        l.append(i.lower())
                    elif case == "upper":
                        l.append(i.upper())
                    elif case == "title":
                        l.append(i.title())
                print("list:", l)
                r = str(" ".join(l))
                camel = first + " " + r
                return camel
