# Modules

- Placing code in the global namespace is a **BAD** idea
- It can cause collisions that are tough to debug
- Which costs development time

This chapter talks about how to write efficient, production-ready controllers by encapsulating functionality in a single core unit called a *module*.

In Angular, a module is the main way to define an AngularJS app. An app can contain several modules, each one pertaining to specific functionality.

Advantages of modules include:

- Keeping the global namespace clean
- Making tests easier to write and keeping them clean so as to more easily target isolated functionality
- Making it easy to share code between applications
- Allowing the app to load different parts of the code in any order

The Angular module API allows us to declare a module using the `angular.module()` API method.

    // the setter method
    angular.module('myApp', []); // name of module, list of dependencies (or injectables)

We can always reference the module by using the same method with only one parameter.

    // the getter method
    angular.module('myApp'); // this method fetches the app

From here, we can create our applications on top of the `angular.module('myApp')` variable.

When writing large applications:

- Create several different modules to contain your logic
- Creating a module for each piece of functionality gives the advantage of isolation in which to write and test large features

Angular modules have properties we can use to inspect the module.

The `name (string)` property on the module gives the name of the module as a string.

The `requires (array of strings)` property contains a list of modules (as strings) that the `injector` loads before the module itself is loaded.