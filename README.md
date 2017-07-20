
## Abstract

Lets face it. Query strings are hard. Now you don't have to know anything
but good old trusty JSON.


```
$ curl -H "Content-Type: application/json" -X POST https://r6i5b3yao2.execute-api.us-west-2.amazonaws.com/dev/query-string-pls -d '{"key": "value", "second key": "whoa this has spaces, hold on guys"}'
key=value&second+key=whoa+this+has+spaces%2C+hold+on+guys
```

And now after much development effort you can convert querystrings to querystrings.
```
$ curl "https://r6i5b3yao2.execute-api.us-west-2.amazonaws.com/dev/query-2-query?key=value"
key=value
```