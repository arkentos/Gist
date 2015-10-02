# Angular in the Rails asset pipeline

The first integration method uses the sprockets asset pipeline to deliver the Angular app. This ability comes baked into Rails already and so no special configuration is needed to support Angular.

Advantages of the approach:

- Zero configuration in Rails
- Rendering of the Angular app only to Rails-based authenticated users
- Rendering of custom data in the JavaScript files
- Choice of using either CoffeeScript or JavaScript without changing workflow
- Simultaneous Rails and Angular development

Inside of this approach, we'll do our work in the directories as follows:

- `app/assets/` - Our custom JavaScript, stylesheets, images, etc
- `lib/assets/` - Our libraries
- `vendor/assets/` - Our assets that we're loading from other authors, such as Twitter Bootstrap and custom Angular libraries

In order to set up our app to deliver Angular apps, we can:

1. Download and embed the necessary JavaScripts in our `vendor/assets/` directory, or
2. Use the Rails `angularjs-rails` gem, which is a thin wrapper around the Angular libraries.

**TIP:** Include the `ngmin-rails` gem to take care of running the pre-minifier for us.

Feel free to include Twitter's Bootstrap or the Zurb Foundation gem:

```ruby
# For Twitter's Bootstrap
gem 'bootstrap-sass-rails'
# or for Zurb Foundation
gem 'zurb-foundation'
```

**NOTE:** If `turbolinks` is listed in your Gemfile, make sure you [remove](http://blog.steveklabnik.com/posts/2013-06-25-removing-turbolinks-from-rails-4) it. Turbolinks will affect the Angular app development, so it's just easier to not deal with the feature.

## Building the share API

**Bug:** To get the application working as it was built up to this point you need to move the `SharesController` into `app/controllers/api` and rename it to `Api::SharesController`.

**Bug:** The `create` action is incorrect. See below for a working version:

```ruby
def create
  # Not used
  # link = params[:url]

  share_params = { from_user_id: current_user.id, url: params[:url] }
  
  # No such method on User called find_by_name_or_email  
  # if to_user = User.find_by_name_or_email(params[:user])

  if to_user = User.where("name = :name OR email = :email", { name: params[:user], email: params[:user] }).first
    share_params[:to_user_id] = to_user.id
  else
    share_params[:to_email] = params[:user]
  end

  share = Share.create(share_params)
  render status: 200,
    json: {
      success: share.persisted?,
      share_id: share.id
    }
end
```