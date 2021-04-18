import re


class Case:
    

    def _CamelSep(string:str, sep:str):
        _list = string.split(sep)
        first = _list[0].lower()
        print("first:", first)
        last = []
        for i in _list[1:]:
            last.append(i.title())
        last = "".join(last)
        print("last:", last)
        result = str(first + last)
        return result

    def _OthersSep(string: str, sep:str, sep1:str, case:str):
        _list = string.split(sep)
        last = []
        for i in _list:
            if case == "lower":
                last.append(i.lower())
            elif case == "upper":
                last.append(i.upper())
            elif case == "title":
                last.append(i.title())
        result = sep1.join(last)
        return result


    def toCamel(string: str):
        string = string.strip()
        print("String:", string)
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            return Case._CamelSep(string, " ")
        
        # For Snakes:
        elif len(string.split("_")) > 1:
            print("Is a Snake")
            return Case._CamelSep(string, "_")
            
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            return Case._CamelSep(string, "-")
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.title()
            else:
                ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
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
        sep1 = "_"
        case = case
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            return Case._OthersSep(string, "-", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.title()
            else:
                ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
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
        sep1 = "-"
        case=case
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
            
        # For Snake:
        elif len(string.split("_")) > 1:
            print("Is a Kebab")
            return Case._OthersSep(string, "_", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.title()
            else:
                ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
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



    def toPascal(string: str):
        string = string.strip()
        print("String:", string)
        sep1 = ""
        case= "title"
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
        
        # For Snakes:
        elif len(string.split("_")) > 1:
            print("Is a Snake")
            return Case._OthersSep(string, "_", sep1=sep1, case=case)
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            return Case._OthersSep(string, "-", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.title()
            else:
                ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
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
        sep1= " "
        case=case

        if len(string.split(" ")) > 1:
            print("Is a Sentence")
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
        
        # For Snake:
        elif len(string.split("_")) > 1:
            print("Is a Snake")
            return Case._OthersSep(string, "_", sep1=sep1, case=case)
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            print("Is a Kebab")
            return Case._OthersSep(string, "-", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            if case == "upper":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.upper()
            elif case == "lower":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.lower()
            elif case == "title":
                print(f"Was returned a {case} case, because the string has no differentiator")
                return string.title()
            else:
                ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")
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
