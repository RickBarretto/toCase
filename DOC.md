# toCase (python)

## class **`Case`**

### `Case.toCamel(string: str, case1: str = "lower")`
+ Returns a "camelCase"

### `Case.toSnake(string: str, case: str = "lower", case1: str = "lower")`
+ Returns a "snake_case"

### `Case.toKebab(string: str, case: str = "lower", case1: str = "lower")`
+ Returns a "kebab-case"

### `Case.toPascal(string: str, case1: str = "title")`
+ Returns a "PascalCase"

### `Case.toUpperSnake(string: str)`
+ Returnsa an "UPPER_SNAKE_CASE"

### `Case.toSentence(string: str, case: str = "lower", case1: str = "lower")`
+ Returns a "String Sentence"


## Method's Attributes:

### string:
+ It's the input, can be in Camel, Snake, Kebab, Pascal, or in a simple Sentence.
  
### case:
+ case defines the output case of a string with differentiador, (" ", "-", "_")
+ It'll return the formated string in upper, lower or title case.
+ options = ['upper', 'lower', 'title']

### case1:
+ case defines the output case of a string with differentiador, (" ", "-", "_")
+ It'll return the formated string in upper, lower or title case.
+ options = ['upper', 'lower', 'title']

