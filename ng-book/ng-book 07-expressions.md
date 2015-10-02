# Expressions

Expression are roughly the result of an `eval(javascript)`. Properties include:

- All expressions are executed in the context of the scope and have access to local `$scope` variables.
- An expression doesn't throw errors if it results in a `TypeError` or a `ReferenceError`.
- They do not allow for any control flow functions (conditionals; e.g., if/else).
- They can accept a filter and/or filter chains.

**N.B.** Expressions all operate on the containing scope within which they are called.

**Parsing an Angular Expression**

Although your Angular app will run parse for you automatically when running the `$digest` loop, sometimes it's useful to parse an Angular expression manually.

Angular evaluates expressions by an internal service (called the `$parse` service) that has knowledge of the current scope.

To manually parse an expression, we can inject the `$parse` service into a controller and call the service to do the parsing for us.

**Interpolating a String**

Although it's uncommon to need to manually interpolate a string template in Angular, we do have the ability to manually run the template compilation. Interpolation allows us to live update a string of text based upon conditions of a scope, for instance.

To run an interpolation on a string template, we need to inject the `$interpolate` service in our object.