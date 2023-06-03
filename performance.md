# Performance

Note that parallel Streams are not always faster than sequential Streams. Especially when the number of elements is small, we can expect sequential Streams to be faster.

The operation that profits most from parallelization is `filter()`

{% hint style="info" %}
If you are not sure wich implementation to choose, let the builder decide:

```python
Stream.of(range(1000))
```
{% endhint %}
