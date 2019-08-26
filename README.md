## Usage

`python bootstrap.py --os macos --profile work`

I recommend reading `bootstrap.py` to understand how it works - it basically renames your existing `.bash_profile` (or any files in here) to `<filename>.bak` and then replaces `.bash_profile` with a symlink to the one in this folder. That way. when you add to `~/.bash_profile`, you can `cd ~/.dotfiles && git add . && git commit -m "updated my bash profile" && git push origin master`.


## Example result

```
Alecs-MacBook-Air  .dotfiles (master)  $ ls -al ~ | grep dotfiles
lrwxr-xr-x   1 alecfwilson  staff     42 Aug 23 12:59 .bash_profile@ -> /Users/alecfwilson/.dotfiles/.bash_profile
drwxr-xr-x  18 alecfwilson  staff    576 Aug 23 12:56 .dotfiles/
-rw-r--r--   1 alecfwilson  staff     67 Aug 23 12:59 .dotfiles_env
lrwxr-xr-x   1 alecfwilson  staff     39 Aug 23 12:59 .gitconfig@ -> /Users/alecfwilson/.dotfiles/.gitconfig
lrwxr-xr-x   1 alecfwilson  staff     65 Aug 23 12:59 .gitconfig.dotfiles_profile@ -> /Users/alecfwilson/.dotfiles/__home__/.gitconfig.dotfiles_profile
lrwxr-xr-x   1 alecfwilson  staff     39 Aug 23 12:59 .gitignore@ -> /Users/alecfwilson/.dotfiles/.gitignore
lrwxr-xr-x   1 alecfwilson  staff     39 Aug 23 12:59 .ideavimrc@ -> /Users/alecfwilson/.dotfiles/.ideavimrc
lrwxr-xr-x   1 alecfwilson  staff     39 Aug 23 12:59 .tmux.conf@ -> /Users/alecfwilson/.dotfiles/.tmux.conf
lrwxr-xr-x   1 alecfwilson  staff     61 Aug 23 12:59 .tmux.conf.dotfiles_os@ -> /Users/alecfwilson/.dotfiles/__macos__/.tmux.conf.dotfiles_os
lrwxr-xr-x   1 alecfwilson  staff     35 Aug 23 12:59 .vimrc@ -> /Users/alecfwilson/.dotfiles/.vimrc
lrwxr-xr-x   1 alecfwilson  staff     35 Aug 23 12:59 .zshrc@ -> /Users/alecfwilson/.dotfiles/.zshrc
```

## To dos
* Set up Sublime Preferences
* Set up Spectacle Preferences
* Set up Snip Preferences
* Create login items
* Create Alfred Preferences
* Create Dropbox Preferences
* Login to chrome, etc
* Create iterm prefs
* Mess with color schemes

## Alternatives

dotfile management resources:
- big list of people doing it different ways: https://dotfiles.github.io/
- fairly opinionated way of doing it, that looked reasonable to me (been meaning to try it) https://www.atlassian.com/git/tutorials/dotfiles
