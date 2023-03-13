---
layout: post
title: Jekyll notes
# date: 2021-07-04 17:39:00
description: My jekyll learning notes
---

## Quick start
- `jekyll new my-awesome-site` to create a new Jekyll site at ./my-awesome-site.
- `cd my-awesome-site` to go into the new directory.
- `bundle exec jekyll serve` to build the site and make it available on a local server.

### Here are simplfied notes for jekyll-assisted blog webpage building.

:warning: `JEKYLL_ENV=production bundle exec jekyll build` to build the website in production environment, then copy contents from `_site` to github.

:warning: Every time after I have modified `_config.yml` file, then I need to restart the server.

:warning: `baseurl=/Blog` does not have `/` in the end

:warning: `link: /Blog/` then needs to have it in the end in `navigation.yml`.


### Jekyll commands
- `bundle exec jekyll serve` to start the server, but :warning: it is not the production environment, and good for local development.
- `JEKYLL_ENV=production bundle exec jekyll build` to build the website in production environment, then copy contents from `_site` to github. 
- `bundle exec jekyll serve --livereload` to start the server with live reload.
- `bundle exec jekyll serve --draft` to start the server with draft posts.


### Jekyll plugins
- How to change theme: 
    * Go to [rubygems.org](https://rubygems.org/) and search **jekyll-theme** for the theme you want to use.
    * Add the theme to your `Gemfile` such as `gem "jekyll-theme-hacker"` and run `bundle install`.
    * Add `theme: jekyll-theme-hacker` to your `_config.yml` file.
    * Run `bundle exec jekyll serve` and your site should now be using the theme you added.

### Jekyll layouts
- How to add a new layout: Create a new file `post.html` in the `_layouts` directory with the following front matter:

### Jekyll styling
- `<br>` for line break. 
- `<hr>` for horizontal line.

### Github pages
- How to launch it on github pages: 
    * Build the site locally with `JEKYLL_ENV=production bundle exec jekyll build`.
    * `git checkout -b gh-pages` to create a new branch called `gh-pages`.
    * Copy the contents of the `_site` directory to the root of the `gh-pages` branch.
    * `git push origin gh-pages` to push the `gh-pages` branch to GitHub.

# Resources
- [Explaining permalinks](https://maximorlov.com/deploying-to-github-pages-dont-forget-to-fix-your-links/)

