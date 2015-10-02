# Controllers

Controllers exist to augment the view of an AngularJS application. The controller adds additional functionality to the scope of the view. We use it to set up an initial state and to add custom behavior to the scope object.

When we create a new controller on the page, Angular passes it a new `$scope`. This new `$scope` is where we can set up the initial state of the scope on our controller. Since Angular takes care of handling the controller for us, we only need to write the constructor function.

Setting up an initial controller looks like this:

```
function FirstController($scope) {
  $scope.message = "hello";
}
```

**Best Practice:** Name controllers as `[Name]Controller` rather than `[Name]Ctrl`.

Angular will call the controller method when it creates the scope.

**Best Practice:** Namespace controllers by first creating a module and then creating the controller within the module.

```
var app = angular.module('app', []);
app.controller('FirstController', function ($scope) {
  $scope.message = "hello";
});
```

Using controllers allows us to contain the logic of a single view in a single container.

**Best Practice:** Keep slim controllers.

The controller is not the appropriate place to do any DOM manipulation, formatting, data manipulation, or state maintenance beyond holding the model data.

## Controller Hierarchy (Scopes Within Scopes)

Every part of an AngularJS application has a parent scope. At the `ng-app` level this scope is called `$rootScope`.

**One exception:** A scope created inside of a directive is called the *isolate* scope.

With the exception of isolate scopes, all scopes are created with prototypal inheritance (i.e. they have access to their parent scopes).

**How it works**

For any property that AngularJS cannot find on a local scope, AngularJS will crawl up to the containing (parent) scope and look for the property or method there. If AngularJS can't find the property there, it will walk to that scope's parent and so on and so forth until it reaches the `$rootScope`. If it doesn't find it on the `$rootScope`, then it moves on and is unable to update the view.