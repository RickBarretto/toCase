import re

class Case:

    def _CamelSep(string:str, sep:str):
        """ Don't use it!"""
        _list = string.split(sep)
        first = _list[0].lower()
        last = []
        for i in _list[1:]:
            last.append(i.title())
        last = "".join(last)
        result = str(first + last)
        return result

    def _OthersSep(string: str, sep:str, sep1:str, case:str):
        """ Don't use it!"""
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

    def _Error():
        """ Don't use it!"""
        #if feedback:
            #print(f"Was returned a {case1} case, because the string has no differentiator")
        raise ValueError("case is wrong, choose between: 'lower', 'upper' or 'title'")


    def toCamel(string: str, case1: str = "lower", feedback:bool = False):
        """toCamel
        string: str, case1: str = "lower"

        Returns a "camelCase"

        + string is the input - It can be in a Pascal, a Sentence, Snake or Kebab case.
        + case1 defines the output case of a string without differentiador, (" ", "-", "_")
        + case1 options: "lower", "title", "upper"

        """
        string = string.strip()
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            return Case._CamelSep(string, " ")
        
        # For Snakes:
        elif len(string.split("_")) > 1:
            return Case._CamelSep(string, "_")
            
        # For Kebab:
        elif len(string.split("-")) > 1:
            return Case._CamelSep(string, "-")
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            Case._Error()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal:
        else:
            _list = re.findall('[A-Z][^A-Z]*', string)
            first = _list[0].lower()
            last = _list[1:]
            last = "".join(last)
            pascal = first + last
            return pascal

            

    def toSnake(string: str, case: str = "lower", case1: str = "lower", feedback:bool = False):
        """toSnake
        string: str, case: str = "lower", case1: str = "lower"

        Returns "snake_case"

        + string is the input - It can be in a Pascal, a Sentence, Snake or Kebab case.
        + case defines the output case of a string with differentiador, (" ", "-", "_")
        + case1 defines the output case of a string without differentiador, (" ", "-", "_")
        + case/case1 options: "lower", "title", "upper"
        """
        string = string.strip()
        sep1 = "_"
        case = case
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            return Case._OthersSep(string, "-", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            Case._Error()
            
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal/Camel:
        else:
            last = re.findall('[A-Z][^A-Z]*', string)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break
            if index == 0:
                first = ""
                l = []
                for i in last:
                    l.append(i.lower())
                pascal = str("_".join(l))
                return pascal
            else:
                first = string[:index]
                l = []
                for i in last:
                    l.append(i.lower())
                r = str("_".join(l))
                camel = first + "_" + r
                return camel
            


    def toKebab(string: str, case: str = "lower", case1: str = "lower", feedback:bool = False):
        """toKebab
        string: str, case: str = "lower", case1: str = "lower"

        Returns "kebab-case"

        + string is the input - It can be in a Pascal, a Sentence, Snake or Kebab case.
        + case defines the output case of a string with differentiador, (" ", "-", "_")
        + case1 defines the output case of a string without differentiador, (" ", "-", "_")
        + case/case1 options: "lower", "title", "upper"
        """
        string = string.strip()
        sep1 = "-"
        case=case
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
            
        # For Snake:
        elif len(string.split("_")) > 1:
            return Case._OthersSep(string, "_", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            Case._Error()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal/Camel:
        else:
            last = re.findall('[A-Z][^A-Z]*', string)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break
            if index == 0:
                first = ""
                l = []
                for i in last:
                    l.append(i.lower())
                pascal = str("-".join(l))
                return pascal
            else:
                first = string[:index]
                l = []
                for i in last:
                    l.append(i.lower())
                r = str("-".join(l))
                camel = first + "-" + r
                return camel



    def toPascal(string: str, case1: str = "title", feedback:bool = False):
        """toPascal
        string: str, case: str = "lower", case1: str = "lower"

        Returns "PascalCase"

        + string is the input - It can be in a Pascal, a Sentence, Snake or Kebab case.
        + case1 defines the output case of a string without differentiador, (" ", "-", "_")
        + case1 options: "lower", "title", "upper"
        """
        string = string.strip()
        sep1 = ""
        case= "title"
        
        # For Sentences:
        if len(string.split(" ")) > 1:
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
        
        # For Snakes:
        elif len(string.split("_")) > 1:
            return Case._OthersSep(string, "_", sep1=sep1, case=case)
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            return Case._OthersSep(string, "-", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            Case._Error()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Camel:
        else:
            last = re.findall('[A-Z][^A-Z]*', string)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break
            first = string[:index].title()
            l = []
            for i in last:
                l.append(i.title())
            l = "".join(l)
            camel = first + l
            return camel



    def toUpperSnake(string: str):
        """toUpperSnake
        string: str, case: str = "lower", case1: str = "lower"

        Returns "UPPER_SNAKE_CASE"

        + string is the input - It can be in a Pascal, a Sentence, Snake or Kebab case.
        """
        
        # For Lowers, Uppers and Titles:
        if string.islower() or string.isupper() or string.istitle():
            string = string.strip()
            print("Was returned a upper case, because the string has no differentiator")
            return string.upper()
        else:
            return Case.toSnake(string).upper()



    def toSentence(string: str, case: str = "lower", case1: str = "lower", feedback:bool = False):
        """toSentence
        string: str, case: str = "lower", case1: str = "lower"

        Returns "String sentence"

        + string is the input - It can be in a Pascal, a Sentence, Snake or Kebab case.
        + case defines the output case of a string with differentiador, (" ", "-", "_")
        + case1 defines the output case of a string without differentiador, (" ", "-", "_")
        + case/case1 options: "lower", "title", "upper"
        """
        string = string.strip()
        sep1= " "
        case=case

        if len(string.split(" ")) > 1:
            return Case._OthersSep(string, " ", sep1=sep1, case=case)
        
        # For Snake:
        elif len(string.split("_")) > 1:
            return Case._OthersSep(string, "_", sep1=sep1, case=case)
        
        # For Kebab:
        elif len(string.split("-")) > 1:
            return Case._OthersSep(string, "-", sep1=sep1, case=case)
    
        # For Uppers, Titles and Lowers:
        elif string.istitle() or string.isupper() or string.islower():
            Case._Error()
        # Errors:
        elif string.isdecimal() or string.isdigit() or string.isnumeric():
            raise ValueError("It's a number")
        elif string == "":
            raise ValueError("It's a white space")

        # For Pascal/Camel:
        else:
            last = re.findall('[A-Z][^A-Z]*', string)
            for i in re.finditer('[A-Z][^A-Z]*', string):
                index = i.span()[0]
                break

            if index == 0:
                first = ""
                l = []
                for i in last:
                    if case == "lower":
                        l.append(i.lower())
                    elif case == "upper":
                        l.append(i.upper())
                    elif case == "title":
                        l.append(i.title())
                pascal = str(" ".join(l))
                return pascal
            
            else:
                first = string[:index]
                if case == "lower":
                        first = first.lower()
                elif case == "upper":
                        first = first.upper()
                elif case == "title":
                        first = first.title()
                l = []
                for i in last:
                    if case == "lower":
                        l.append(i.lower())
                    elif case == "upper":
                        l.append(i.upper())
                    elif case == "title":
                        l.append(i.title())
                r = str(" ".join(l))
                camel = first + " " + r
                return camel

print(Case.toCamel("helloworld"))