# Parser

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence

```
expr -> add_or_sub

add_or_sub -> mul_or_div ("+" | "-") add_or_sub
    | mul_or_div

mul_or_div -> neg ("*" | "/") mul_or_div 
    | neg

neg -> "-" neg 
    | grp

grp -> "(" expr ")" 
    | val   

val -> INT
```