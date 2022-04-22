import os
import requests
import shutil


shell = os.environ['SHELL']
if 'zsh' not in shell:
    print('ログインシェルをzshに変更してください')
    exit(1)

home_dir = os.environ['HOME']

git_completion_url = 'https://raw.githubusercontent.com/git/git/master/contrib/completion'
git_completion_target_dir = f'{home_dir}/.zsh'

os.makedirs(git_completion_target_dir, exist_ok=True)

for filename in ['git-prompt.sh', 'git-completion.bash']:
    with open(f'{git_completion_target_dir}/{filename}', mode='wb') as f:
        data = requests.get(f'{git_completion_url}/{filename}').content
        f.write(data)

with open(f'{git_completion_target_dir}/_git', mode='wb') as f:
    data = requests.get(f'{git_completion_url}/git-completion.zsh').content
    f.write(data)

shutil.copy('.zshrc', home_dir)
os.system('$SHELL -c "source ~/.zshrc; exec $SHELL -l"')
