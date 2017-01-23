# [jarmac.org](http://jarmac.org)
> "But you're not an organization!!"


This readme will serve as a catalog of all the information needed to start a blog on a (very) low end VPS. I'll leave out specifics, like what theme I'm running (although that [does sometimes make a difference in functionality](https://euer.krebsco.de/piwik-for-this-blog.html), unfortunately)

## Table of contents
- [Deploying](#deploying)
- [Transparency](#transparency)
- [Features](#features)
- [Repro](#repro)

## Deploying

As of now, this blog is hosted on an nginx server obtained through apt-get and configured the traditional way. I want to move it to nix management, especially as this server does not scale well at all and the more config I can sanely keep in version control the better.

When I see 'doesn't scale well at all' I mean I run oom just running nix-env -q. Attempts to compile it with the Boehm GC (as described in the wiki) doesn't work, as I can't even compile ZNC. What does work, very, very well is the ability to install locally on my own machine, export it to a closure, and then rsync it over to the machine and import it to the store, installing from there.

This can be accomplished [in two ways](https://nixos.org/nix/manual/#ssec-copy-closure), I do it the second way:

``` bash
local $ nix-store --export $(nix-store -qR $(type -p nginx)) > nginx.closure
local $ rsync . jarmac.org:~/closures/
local $ ssh jarmac.org

jarmac.org $ nix-store --import < nginx.closure
# yank the relevant line from the import output, should be the last line
jarmac.org $ nix-env -i /nix/store/8padg3vj1mbbx9kcph41xqfy130xhgac-nginx-1.11.5
jarmac.org $ which nginx
~/.nix-profile/bin/nginx
```

I've done exactly this to get znc and nginx running. This more than likely could be placed into some default.nix file so that instead I can just push that, and execute it with nix-build.

Further, while I will be using pelican (moving from jekyll, both static site generators), I  will be using [piwik](https://github.com/piwik/piwik), just so I can visualize the reality that I'm posting to /dev/null.

I aim to keep as much deploy logic locally as possible, including login credentials (another reason to use RSA keys!) The only thing I did on the remote server is create a symlink from /usr/share/nginx/www to where it is pushed to.

I've considered git as a deployment model instead but I know octopress has growing pains from adopting that. I don't like pain.

## Transparency
I aim to make this process as transparent as possible, excepting secrets and server details. So I'm removing the Makefile and fabfile.py, which are both autogenerated and look like files I won't ever be changing. If I make any notable changes, I will likely include them here. I will definitely be modifying pelican's configuration, so it's in here.


## Features

- Pelican
- Piwik (pending)


## Repro
I do not suggest git cloning this. I'd rather you read this document, specifically [deploy](#deploy) as that is how I do everything that isn't blog writing.

First, you need either a shared hosting provider or a VPS of your own. I'm currently using Ramnode for a (very) cheap VPS, as my needs are miniscule. I do not like how locked down shared hosting is, and I don't really want to play ball with cpanel if I can help it.
