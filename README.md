# Boolean Expression Interpreter Application
Simple Boolean Expression Interpreter Application which uses a recursive descent parser\

## How to use it?

_Just run_ ___`main.py`___

* Commands are:
  - `eval <expression>`\
    The expression in eval can only be made of:
    - ` ` (Whitespace)
    - `T` (True)
    - `F` (False)
    - `v` (OR)
    - `^` (AND)
    - `~` (NOT)
    - `->` (IMPLY)
    - `(` (Left parenthesis)
    - `)` (Right parenthesis)
    - `.` (End of statement)
  - `open <filename>`\
     - The filename needs to have an extension specified (or can be empty if there is no extension)
     - The filename can contain spaces. In such case, ___no___ ___need___ to add strings, just type it
  - `exit` or just the `enter` key
   
## Specifications

### Syntax and Selection Set:

| Grammar                                | Selection Set |                        
|----------------------------------------|---------------|                      
| `<B>	        ::=  <IT> .	       `     | {∼,T,F,(}    |                           
| `<IT>	    ::=  <OT> <IT_Tail>    `     | {∼,T,F,(}    |                          
| `<IT_Tail>	::=  −> <OT> <IT_Tail> ` |     {−>}      |                         
| `<IT_Tail>   ::=  ε	           `     |   {.,)}      |                                
| `<OT>	    ::=  <AT> <OT_Tail>	   `     | {∼,T,F,(}    |                          
| `<OT_Tail>   ::=  v <AT> <OT_Tail>`    |     {∨}       |                          
| `<OT_Tail>   ::=  ε	           `     |  {−>,.,)}    |                              
| `<AT>	    ::=  <L> <AT_Tail>	   `     | {∼,T,F,(}    |                              
| `<AT_Tail>	::=  ^ <L> <AT_Tail>   ` |     {^}       |                           
| `<AT_Tail>   ::=  ε               `    |  {∨,−>,.,)}   |                                
| `<L>	        ::=  <A>	       `     |  {T,F,(}|    |                                       
| `<L>            ::=  ~ <L>           `    |     {~}       |                              
| `<A>	        ::=  T  	       `     |    {T}       |                          
| `<A>            ::=  F	           `     |    {F}       |                              
| `<A>            ::=  ( <IT> )	       ` |     {(}       |     
  
### Syntactic Domain
```
<B> : Bool stmt
<IT> : Imply term
<OT> : Or term
<AT> : And term
<IT_Tail> : Imply tail
<OT_Tail> : Or tail
<AT_Tail> : And tail
<L>: Literal
<A>: Atom
```

### Semantic Domain:
```
b = {T.F} (Boolean values True and False)
```

### Semantic Function Domains:
```
α : Bool stmt → b
β : Imply term → b
δ : Or term → b
γ : And term → b
λ : b × Imply tail → b
µ : b × Or tail → b
η : b × And tail → b
φ : Literal → b
ψ : Atom → b
```

Author: N'Godjigui Junior Diarrassouba\
_Written in Fall 2018_
