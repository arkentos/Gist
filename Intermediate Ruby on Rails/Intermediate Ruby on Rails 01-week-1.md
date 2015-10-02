# Week 1

The first part helps us start with a great foundation. It's about how to set up a Rails application correctly. Then in future lessons we move onto complex associations, unit testing and other advanced topics.

**Requirements**

- Ruby 1.9.3
- Rails 3.2.12

We build an application called `Shouter` that is a Twitter like app. Users make shouts.

**Specific Gems**

- `gem 'strong_parameters', '0.2.0'`, https://github.com/rails/strong_parameters
- `gem 'monban', '0.0.6'`, https://github.com/halogenandtoast/monban

## Q&A

- How to install a specific version of Rails?

        $ gem install rails -v 3.2.12

- How to write a good commit message?

  - [A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
  - [5 Useful Tips for a Better Commit Message](http://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message)
  - [Linus Torvalds on Commit Messages](https://github.com/torvalds/linux/pull/17#issuecomment-5659933)

- How to use Strong Paramters?

  http://guides.rubyonrails.org/action_controller_overview.html#strong-parameters

- At `7:27` you open your browser and there is an app running that tells the time among other things. What is it called and where can I get it?

- How does database indexing work?

  - [A Stack Overflow answer to the question](http://stackoverflow.com/questions/1108/how-does-database-indexing-work)
  - [Database index on Wikipedia](http://en.wikipedia.org/wiki/Database_index)

- What are some other approaches to redirecting the user to a specific page after sign in?

  - [Other approaches to redirect user to their dashboard on sign in](http://forum.thoughtbot.com/t/other-approaches-to-redirect-user-to-their-dashboard-on-sign-in/2311)
  - [Redirect user after log in only if it's on root_path](http://stackoverflow.com/questions/8640326/redirect-user-after-log-in-only-if-its-on-root-path)

## Resources

- [Fork a Repo](https://help.github.com/articles/fork-a-repo)
- [`div_for`](http://api.rubyonrails.org/classes/ActionView/Helpers/RecordTagHelper.html#method-i-div_for)
- [`time_ago_in_words`](http://api.rubyonrails.org/classes/ActionView/Helpers/DateHelper.html#method-i-time_ago_in_words)
- [`rails s -d`](http://guides.rubyonrails.org/command_line.html#rails-server)