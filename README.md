<h1 align="center">RB toCase<h1>
<img alt="Cover" src="./assets/cover.svg">
<h4 align="center">made by: <a href="https://github.com/RickBarretto/">RickBarreto</a></h4>

## What is it?
**RB toCase** is a Case converter made in python, for peoples who wants simplify this feature. It can convert to and from Camel, Pascal, Snake, Kebab and Strings Sentences.
**And, You don't need say what is the input type, the code parse it. Just say whats is the output type.**

> Older name was toCase, but when I was publishing on Pipy tocase package already exists. So I changed the name!

## Why I must to use it?
+ toCase was made to make easy your life with case converting
+ I was made in python, so, if you want, you can copy the [toCase.py](https://github.com/RickBarretto/toCase/blob/main/src/ToCase.py) and use in your project. **It's free to use, look the [MIT LICENSE](LICENSE).**

## Glossary:
- [What is it?](#what-is-it)
- [Why I must to use it?](#why-i-must-to-use-it)
- [Glossary:](#glossary)
- [Installing](#installing)
- [Examples:](#examples)
  - [Importing:](#importing)
  - [Convert to Camel Case:](#convert-to-camel-case)
  - [Convert to Snake Case:](#convert-to-snake-case)
  - [Convert to Kebab Case:](#convert-to-kebab-case)
  - [Convert to Pascal Case:](#convert-to-pascal-case)
  - [Convert to Sentence:](#convert-to-sentence)
- [Read The Docs!](#read-the-docs)

## Installing

```bash
$ poetry add rb_tocase

or

$ pip install rb_tocase
```

## Examples: 

### Importing:
```py
>>> from rb_tocase import Case
>>> # or
>>> from rb_tocase import *
>>> # see the examples below
```

### Convert to Camel Case:
```py
>>> Case.to_camel("Changing to CaMel CASE")   # From String Sentence
'changingToCamelCase'
>>> Case.to_camel("Changing-to-camel-case")   # From Kebab Case
'changingToCamelCase'
>>> Case.to_camel("Changing_to_CAMEL_CASE")   # From Snake Case
'changingToCamelCase'
>>> Case.to_camel(" ChangingToCamelCase  ")   # From Pascal Case
'changingToCamelCase'
```
+ [See more](DOC.md#casetocamelstring-str-case1-str--lower)

### Convert to Snake Case:
```py
>>> Case.to_snake(" ChanginToSnakeCase ")     # From Pascal Case
'changin_to_snake_case'
>>> Case.to_snake(" Changin To Snake Case ")  # From String
'changin_to_snake_case'
>>> Case.to_snake(" Changin-To-Snake-Case ")  # From Kebab
'changin_to_snake_case'
>>> Case.to_snake(" changinToSnakeCase ")     # From Camel
'changin_to_snake_case'
```
[See more](DOC.md#casetosnakestring-str-case-str--lower-case1-str--lower)

### Convert to Kebab Case:
```py
>>> Case.to_kebab("Changing to Kebab")    # From String
'changing-to-kebab'
>>> Case.to_kebab("ChangingToKebab")      # From Pascal Case
'changing-to-kebab'
>>> Case.to_kebab("changingToKebab")      # From Camel Case
'changing-to-kebab'
>>> Case.to_kebab("changing_to_kebab")    # From Snake Case
'changing-to-kebab'
```

[See more](DOC.md#casetokebabstring-str-case-str--lower-case1-str--lower)

### Convert to Pascal Case:
```py
>>> Case.to_pascal("Changing to Pascal")  # From String
'ChangingToPascal'
>>> Case.to_pascal("Changing-to-Pascal")  # From Kebab
'ChangingToPascal'
>>> Case.to_pascal("Changing_to_Pascal")  # From Snake
'ChangingToPascal'
>>> Case.to_pascal("ChangingtoPascal")    # From Pascal
'ChangingtoPascal'
>>> Case.to_pascal("changingToPascal") # From Camel
'ChangingToPascal'
```
+ [See more](DOC.md#casetopascalstring-str-case1-str--title)

### Convert to Sentence:
```py
>>> Case.to_sentence("ItsAPascalCase")
'its a pascal case'
>>> Case.to_sentence("itsACamelCase")
'its a camel case'
>>> Case.to_sentence("Its-A-Kebab-Case")
'its a snake case'
>>> Case.to_sentence("Its_a_snake_case")
'its a snake case'
```
+ [See more](DOC.md#casetosentencestring-str-case-str--lower-case1-str--lower)


## Read The Docs!
[Documentation](DOC.md)