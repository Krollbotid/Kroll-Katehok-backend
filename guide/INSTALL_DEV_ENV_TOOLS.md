# Настройка среды разработки для Windows

## Poetry
Установка (powershell с правами администратора):
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Необходимо добавить `bin`-директорию в `PATH` (вместо `/path/to/poetry/dir` вставить путь к директории с исполняемым файлом poetry)
```
[System.Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";/path/to/poetry/dir", [System.EnvironmentVariableTarget]::User)
```
Чтобы изменения вступили в силу, необходимо перезагрузить powershell

Проверить, что все установилось корректно:
```
poetry --version
```

## Pyenv
Клонируем реп
[Clone repo](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#git-commands)
```
git clone https://github.com/pyenv-win/pyenv-win.git "$HOME\.pyenv"
```
Добавляем переменные окружения
[Adding env vars](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#add-system-settings)
```
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

Проверить, что все установилось корректно:
```
pyenv --version
```

### В PowerShell могут не запускаются сценарии, в этом случае используйте CMD