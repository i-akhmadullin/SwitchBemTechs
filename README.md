SwitchBemTechs
=======================

Switch between different bem-tech files(css,js,priv.js,deps.js,bh.js, bemhtml...) on same level with one keypress.

If a different file can't be found on same level, does nothing.


Example
=======
![sublimetext switch between bem-tech files ](/demo.png "switch between bem techs")


Installation
=======

1. Ctrl+Shift+P → Package Control: Add Repository → https://github.com/i-akhmadullin/SwitchBemTechs

2. Ctrl+Shift+P → Package Control: Install Package → SwitchBemTechs

3. (Optional) If you want to override default F3 shortcut add line like this: 
```json
    { "keys": ["type_your_shortcut_here"], "command": "switch_bem_techs", "args": {"extensions": [".css", ".js", ".priv.js", ".deps.js", ".bh.js"]} } }
```
in `Sublime Text 3/Packages/User/Default.sublime-keymap` file.