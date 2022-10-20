12 * 4 - 3 / (12-3)


```py
ast = {
    type: "minus"
    left {
        type: "mul"
        left {
            type: "number"
            value: 12
        }
        right {
            type: "number"
            value: 4
        }
    }
    right {
        type: divide
        left {
            type: "number"
            value: 5
        }
        right {
            type: "minus"
            left {
                type: "number"
                value: 14
            }
            right {
                left {
                    type: "number"
                    value: 3
                
            }
        }
    }

}
```