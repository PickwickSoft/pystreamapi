# API Reference

Dive into the specifics of each stream operation by checking out our complete documentation.

## Intermediate Operations

Intermediate operations are transformative and filtering operations applied to the elements of a Stream, enabling diverse data manipulations and facilitating the chaining of operations to construct intricate processing pipelines while maintaining the Stream's continuity.

{% content-ref url="intermediate-operations.md" %}
[intermediate-operations.md](intermediate-operations.md)
{% endcontent-ref %}

## Terminal Operations

A terminal operation is an operation that is performed on a stream and produces a result or a side effect. Terminal operations are the final step in a stream pipeline and trigger the processing of the elements in the stream.

When a terminal operation is invoked on a stream, it consumes the elements from the stream and produces a result, which could be a single value or a collection, or performs a side effect, such as writing to a file or displaying information on the console. Once a terminal operation is executed, the stream is considered consumed and cannot be reused.

If you try to reuse the stream, it will throw a `RuntimeError`.

{% content-ref url="terminal-operations.md" %}
[terminal-operations.md](terminal-operations.md)
{% endcontent-ref %}

## Numeric Stream

`NumericStream` is a special Stream type that extends the default functionality with operations for numerical data sources such as statistical and mathematical functions.

{% content-ref url="numeric-stream.md" %}
[numeric-stream.md](numeric-stream.md)
{% endcontent-ref %}
