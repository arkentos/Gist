# Scopes

A core of any Angular app. The scopes of the application refer to the application model. Scopes are the execution context for expressions. The `$scope` object is where we define the business functionality of the application, the methods in our controllers, and properties in the views.

Scopes serve as the glue between the controller and the view.

- Before our app renders the view to the user
- The view template links to the `$scope`
- And the app sets up the DOM to notify Angular for property changes

**Scopes are the source of truth** for the application state. Because of *live binding*, we can rely on the `$scope` to update immediately when the view modifies it, and we can rely on the view to update when the `$scope` changes.

`$scope` in angularJS are arranged in a hierarchical structure that mimics the DOM and thus are nestable: We can reference properties on parent `$scope`s.

Scopes provides the ability to `watch` for model changes. They give the developer the ability to propagate model changes throughout the application by using the apply mechanism available on the scope. We define and execute expressions in the context of a scope; it is also from here that we can propagate events to other controllers and parts of the application.

## The $scope View of the World

- Angular starts to run
- It generates the view
- It creates a binding from the root `ng-app` element to the `$rootScope`
- The `$rootScope` eventually becomes the parent of all `$scope` objects

> The `$rootScope` object is the closest object we have to the global context in an Angular app. It's a bad idea to attach too much logic to this global context, in the same way that it's not a good idea to dirty the JavaScript global scope.

- The `$scope` object is a plain old JavaScript object
- The `$scope` object is the *data model* in Angular

**All properties found on the `$scope` object are *automatically* accessible to the view.**

Through Angular, we can use different types of markup in a template. These include:

- Directive: the attributes or elements that augment the existing DOM element into a reusable DOM component
- Value bindings: the template syntax `{{ }}` binds expressions to the view
- Form controls: user input validation controls

Scopes have the following basic functions:

- They provide `observers` to watch for model changes
- They provide the ability to propagate model changes through the application as well as outside the system to other components
- They can be nested such that they can isolate functionality and model properties
- They provide an execution environment in which expressions are evaluated

**You can think of scopes as *view models*.**

## `$scope` Lifecycle

When the browser receives a JavaScript callback that executes *inside* of the Angular execution context the $scope will be made aware of the model mutation. If the callback executes *outside* of the Angular context, we can force the $scope to have knowledge of the change using the `$apply` method.

After the scope expression is evaluated and the `$digest` loop runs, the `$scope`'s watch expressions will run dirty checking.

- Creation
    - When we create a controller or directive, Angular creates a new scope with the `$injector` and passes this new scope for the controller or directive at runtime.
- Linking
    - When the `$scope` is linked to the view, all directives that create `$scope`s will register their watches on the parent scope. These watches watch for and propagate model changes from the view to the directive.
- Updating
    - During the `$digest` cycle, which executes on the `$rootScope`, all of the children scopes will perform dirty digest checking. All of the watching expressions are checked for any changes, and the scope calls the listener callback when they are changed.
- Destruction
    - When a `$scope` is no longer needed, the child scope creator will need to call `scope.$destroy()` to clean up the child scope. Note that when a scope is destroyed, the `$destroy` event will be broadcasted.

**Links**

- http://docs.angularjs.org/api/ng.$rootScope
- http://docs.angularjs.org/guide/scope
- http://docs.angularjs.org/api/ng.$rootScope.Scope