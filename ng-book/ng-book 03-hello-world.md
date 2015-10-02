# Data Binding and Your First AngularJS Web Application

The chapter starts off by writing a *hello world* application to show off *data binding*.

AngularJS creates *live* templates as a view. Individual components of the views are dynamically interpolated live.

**Basic Setup**

1. Include `https://ajax.googleapis.com/ajax/libs/angularjs/1.2.6/angular.js` in the HTML.
2. Set the `ng-app` attribute on an element in the DOM.

The `ng-app` attribute declares that everything inside of it belongs to the Angular app. The only components that will be affected by Angular are the DOM elements that are declared inside of the one with the `ng-app` attribute.

> Automatic data binding gives us the ability to consider the view to be a projection of the model state. Any time the model is changed in the client-side model, the view reflects these changes without writing any custom code. It just works.

**Recommended Reading:** [GUI Architectures](http://martinfowler.com/eaaDev/uiArchs.html)

**How Hello World Works**

When Angular thinks that the value could change, it will call `$digest()` on the value to check whether the value is "dirty". This process is called **dirty checking**. The dirty check is done inside its event loop to ensure everything is consistent.

What we did was to `bind` the "name" attribute to the input field using the `ng-model` directive on the containing model object (`$scope`). This means that whatever value is placed in the input field will be reflected in the model object.

**Miscellaneous**

The model object refers to the `$scope` object. The `$scope` object is a JavaScript object whose properties are all available to the view and with which the controller can interact.

*Bi-directional* in Angular means that if the view changes the value, the model observes the change through dirty checking, and if the model changes the value, the view updates with the change.

Declaring `ng-controller` attribute on a DOM element says that all of the elements inside of it belong to the controller.

It's considered a *best-practice* in Angular to bind references in the views by an attribute on an object, rather than the raw object itself.