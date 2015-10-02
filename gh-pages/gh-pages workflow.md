**First Time**

The `gh-pages` branch does not exist on the remote.

```sh
# Set up the build directory on an orphan branch
$ mkdir build && cd build
$ git init
$ git checkout --orphan gh-pages

# Seed the repository
$ echo 'Hello, world!' > index.html
$ git add .
$ git commit -m "Initial commit"

# Publish the branch
$ REMOTE_URL=`cd .. && git config --get remote.origin.url`
$ git remote add origin $REMOTE_URL
$ git push origin gh-pages
```

**Other Times**

The `gh-pages` branch is already on the remote.

```sh
# Checkout the branch
$ mkdir build && cd build
$ git init
$ REMOTE_URL=`cd .. && git config --get remote.origin.url`
$ git remote add origin $REMOTE_URL
$ git fetch origin
$ git checkout gh-pages

# Do some work
$ git add --all
$ git commit -m "..."

# Push the changes
$ git push origin gh-pages
```

**References**

- https://github.com/neo/middleman-gh-pages/blob/master/lib/middleman-gh-pages/tasks/gh-pages.rake
- https://help.github.com/articles/creating-project-pages-manually/