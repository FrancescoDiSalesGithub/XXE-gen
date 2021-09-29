# XXE-gen
XXE vulnerability creator 

## How to use

`python3 xxe-gen.py [operation] [entity]`

where:
* operation = what do you want to do with the XXE vulnerability
* entity = the name of the xml entity

the possible operations are injection and dos in which:
* injection -> does a xxe 
* dos -> implements a dos xxe

some examples about how to run it:
  ```
        python3 xxe-gen.py injection banana
       python3 xxe-gen.py dos banana
  ```
