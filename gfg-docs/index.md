---
title: Home
layout: home
nav_order: 1
description: "Jekyll (Just the Docs theme) based GitHub Pages website with built-in search."
permalink: /
---

# DataStructure and Algorithms
{: .fs-9 }

This github pages cover the basics of DSA and related code snippets. This webpage follows https://www.geeksforgeeks.org/dsa
{: .fs-6 .fw-300 }

## Getting Started

Your getting started content...
```

**3. Create your documentation structure** - Inside your `gfg-docs` folder, create a `docs` folder and add your documentation pages:
```
gfg-docs/
├── _config.yml
├── index.md
└── docs/
    ├── topic1.md
    ├── topic2.md
    └── subfolder/
        └── subtopic.md

To run this website locally, you can use the following command:
```bash
cd /mnt/c/Users/manju/Desktop/neetcode-practice/gfg-docs

# Install Ruby
sudo apt update
sudo apt install build-essential zlib1g-dev ruby-full -y

# Configure Ruby Gems path
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Install Jekyll and Bundler
sudo gem install jekyll bundler

# Configure Bundler for this project (tell Bundler to install gems into a local folder inside your project instead of the system folder)
bundle config set --local path 'vendor/bundle'

# Initialize Jekyll site(Check if there is Gem file in the same location as _config.yml and if not create it)
bundle init
bundle add jekyll
bundle add jekyll-remote-theme
bundle add webrick
bundle add jekyll-seo-tag

bundle add jekyll-github-metadata
bundle add jekyll-include-cache
bundle add jekyll-sitemap

# Run the server(for every change, stop and run this command again)
bundle exec jekyll serve --livereload
```