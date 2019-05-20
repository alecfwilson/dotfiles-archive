## Usage

`python bootstrap.py --os macos --profile work`

I recommend reading `bootstrap.py` to understand how it works - it basically renames your existing `.bash_profile` (or any files in here) to `<filename>.bak` and then replaces `.bash_profile` with a symlink to the one in this folder. That way. when you add to `~/.bash_profile`, you can `cd ~/.dotfiles && git add . && git commit -m "updated my bash profile" && git push origin master`.



## Example result

```
Andrews-MacBook-Pro:.dotfiles alook$ ls -al ~ | grep dotfiles
lrwxr-xr-x     1 alook  staff       23 Aug  9  2015 .bash_profile -> .dotfiles/.bash_profile
lrwxr-xr-x     1 alook  staff       17 Aug  9  2015 .bashrc -> .dotfiles/.bashrc
drwxr-xr-x    13 alook  staff      442 Dec 21 19:32 .dotfiles
lrwxr-xr-x     1 alook  staff       20 Aug  9  2015 .gitconfig -> .dotfiles/.gitconfig
lrwxr-xr-x     1 alook  staff       33 Nov 20 09:39 .tmux.conf -> /Users/alook/.dotfiles/.tmux.conf
lrwxr-xr-x     1 alook  staff       16 Aug  9  2015 .vimrc -> .dotfiles/.vimrc
```

## Alternatives

dotfile management resources:
- big list of people doing it different ways: https://dotfiles.github.io/
- fairly opinionated way of doing it, that looked reasonable to me (been meaning to try it) https://www.atlassian.com/git/tutorials/dotfiles
