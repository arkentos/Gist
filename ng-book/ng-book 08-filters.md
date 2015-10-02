# Filters

A filter provides a way to format the data we display to the user. Filters are invoked in HTML with the | (pipe) character inside the template binding characters {{ }}. For e.g. to use the `uppercase` filter,

```html
{{ name | uppercase }}
```

We can also use filters from within JavaScript by using the `$filter` service. For e.g. to use the lowercase filter,

```javascript
app.controller('DemoController', ['$scope', '$filter',
  function ($scope, $filter) {
    $scope.name = $filter('lowercase')('Dwayne');
  }
]);
```

To pass an argument to a filter in the HTML form, we pass it with a colon after the filter name (for multiple arguments, we can simply append a colon after each argument). For e.g. the number filter allows us to limit the number of decimal places a number can show.

```html
{{ 123.456789 | number:2 }} <!-- Displays: 123.46 -->
```

We can use multiple filters at the same time by using two or more pipes.

## Making Our Own Filter

To create a filter, we put it under its own module.

```javascript
var filters = app.module('app.filters', []);

filters.filter('capitalize', function () {
  return function (input) {
    if (input) {
      return input[0].toUpperCase() + input.slice(1);
    }
  }
});
```

Filters are just functions to which we pass input.

## Resources

- [AngularJS: Filters](http://docs.angularjs.org/guide/filter)
- [Built-in Filters](http://docs.angularjs.org/api/ng#filter)
- [`ng.$filter`: The `$filter` service](http://docs.angularjs.org/api/ng.$filter)