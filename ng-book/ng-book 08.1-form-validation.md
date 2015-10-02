# Form Validation

AngularJS supports form validation with a mix of the HTML5 form validation inputs as well as with its own validation directives. It makes it pretty easy for us to handle client-side form validations without adding a lot of extra effort.

To use form validations:

- Ensure that the form has a name associated with it
- Use the `novalidate` attribute on the form element, as it prevents the browser from natively validating the form

```html
<form name="form" novalidate>
  <!-- ... -->
</form>
```

## Control Variables in Forms

AngularJS makes properties available to us (in the format `formName.inputFieldName.property`) on the containing `$scope` object available to us as a result of setting a form inside the DOM. These properties enable us to react to the form in real time.

`formName.inputFieldName.$pristine` is a boolean property that tells us whether the user has modified the form. It is `true` if the user hasn't touched the form, and `false` if they have.

`formName.inputFieldName.$dirty` is a boolean property that tells us if and only if the user has actually modified the form. It is set regardless of validations on the form.

`formName.inputFieldName.$valid` is a boolean property that tells us whether or not the form is valid. If the form is currently *valid*, then it would be `true`.

`formName.inputFieldName.$invalid` is a boolean property that tells us whether or not the form is invalid. If the form is currently *invalid*, then it would be `true`.

`formName.inputFieldName.$error` contains all of the validations on a particular form and a record of whether they are valid or invalid. If a validation fails, then this property will be `true`; if it is `false`, then the value has passed the input field.

When AngularJS is handling a form, it adds specific classes to the form based upon the current state of the form (i.e. if it's currently valid, unchanged, etc.). These classes are named similarly to the properties that we can check, as well.

These classes are:

- `ng-pristine`
- `ng-dirty`
- `ng-valid`
- `ng-invalid`

There are some really good examples in this section of the book. Consult the book to find out more.

## Resources

- [form](http://docs.angularjs.org/api/ng.directive:form)
- [input](http://docs.angularjs.org/api/ng.directive:input)
- [input.checkbox](http://docs.angularjs.org/api/ng.directive:input.checkbox)
- [input.email](http://docs.angularjs.org/api/ng.directive:input.email)
- [input.number](http://docs.angularjs.org/api/ng.directive:input.number)
- [input.radio](http://docs.angularjs.org/api/ng.directive:input.radio)
- [input.text](http://docs.angularjs.org/api/ng.directive:input.text)
- [input.url](http://docs.angularjs.org/api/ng.directive:input.url)
- [select](http://docs.angularjs.org/api/ng.directive:select)
- [textarea](http://docs.angularjs.org/api/ng.directive:textarea)
- [ngModelController](http://docs.angularjs.org/api/ng.directive:ngModel.NgModelController): Learn about `$parsers` and `$formatters` among other things