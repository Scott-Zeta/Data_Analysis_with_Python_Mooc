# Data_Analysis_with_Python_Mooc
https://dap-21.mooc.fi/

## Note for regular expression
https://youtu.be/sa-TUpSx1JA
1. MetaCharacters: . [ { ( ) } ] \ ^ $ | ? * +   have special meaning, if want to search them, add back slash.
e.g search \\. for .
2. \ expression    
    - . for any character excepte newline
    - \d for 0-9 digits
    - \D for non-digits
    - \w word character, a-z, A-Z, 0-9, _ underline
    - \W non-word
    - \s any white space(tab, newline)
    - \S non-white space
    - \b Word Boundary, check if split from other word's character in the same string
    - \B non-word boundary
        eg. ha haha,
        1. \bha, return first and second
        2. ha\b, return first and third
        3. \bha\b, return first
        4. \bha\B, return second
        5. \Bha\b, return third
    - ^ begining of String(a line)
    - $ end of String(a line)
3. character set[], any character inside that want to match, if metacharacters inside [], no need for back slash. e.g. [-.] match only one - or . , 3-4 and 2.6 all match with \d[-.]\d, [89]00 can be 800 or 900.
    - \- between value inside [] can be the range of the value, like [1-7]
    - ^ in the [] means non-in the set, like [^a-z] means non-lowercase letters.
4. Quantifier, Quantifier always outside of the character set []+ []{2} []*
    - \* : 0 or More
    - \+ : 1 or More
    - ? : 0 or 1, Mr\.? looking for Mr or Mr.
    - {} : exact repeat times {3} for 3 times, \d{3} looking for continuesly 3 digits
    - {min,max}: range, {3,5} from 3 times to 5 times
5. group (), group for different parttern
    - | for or, M(r|s|rs) looking for Mr, Ms and Mrs
    - can use $ for group number, e.g. $1, $2, $3 for (1)(2)(3), $2$3 for (2)and(3)

## Regular expression in Python
1. Raw String, put an r before a string, r"\tString", it will use \t literally without turn into tab.
2. re.compile(r'regular expression') will create a seach patterns. Can have flag, such like re.compile(r'', re.IGNORECASE/re.I)
3. pattern.finditer(String) return a iteratable re.match object, each include sub strings matche to pattern
4. for every match in iteratable object group, also follow the re group above, group(0) for whole match substring, then 1,2,3...
5. pattern.sub(r'\2\3', String), replace the original string with group 2 and group 3
6. finditer(String), return match object with extra info. findall(String) return matches as list of String. If it has group in regular expression raw String, it will return group tuples or the only group
7. pattern.match() only return the first one or null(if not exist). pattern.search() will return the first one too but with full info like finditer()
