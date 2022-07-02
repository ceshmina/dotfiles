# dotfiles


## 使い方

事前にログインシェルをzshに変更してください。

```
% git clone https://github.com/ceshmina/dotfiles.git
% cd dotfiles
% python3 setup.py
```


## 注意

Pythonのライブラリが不足している場合、事前にインストールしてください。

```
% pip3 install requests
```

以下のファイルがすでに存在する場合、**上書きされます**。

- `~/.zshrc`
- `~/.zsh/git-prompt.sh`
- `~/.zsh/git-completion.bash`
- `~/.zsh/_git`
