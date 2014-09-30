import sublime, sublime_plugin
import os.path
import platform
import re

def compare_file_names(x, y):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        return x.lower() == y.lower()
    else:
        return x == y

def commonBase(fileName, extensions):
    base = fileName
    ext = ''
    for e in extensions:
        match = re.match('(.*)(' + re.escape(e) + ')$', fileName)
        if match and base.startswith(match.group(1)):
            base = match.group(1)
            ext = match.group(2)
    return base, ext

class SwitchBemTechsCommand(sublime_plugin.WindowCommand):
    def run(self, extensions=[]):
        if not self.window.active_view():
            return

        path = self.window.active_view().file_name()
        if not path:
            return

        dir, file = os.path.split(path)
        base, ext = commonBase(file, extensions)

        start = 0
        count = len(extensions)


        if ext != "":
            for i in range(0, len(extensions)):
                if compare_file_names(extensions[i], ext):
                    start = i + 1
                    count -= 1
                    break

        for i in range(0, count):
            idx = (start + i) % len(extensions)

            new_file = base + extensions[idx]
            new_path = os.path.join(dir, new_file)

            if os.path.exists(new_path):
                sublime.status_message("File to switch found in current directory.")
                self.window.open_file(new_path)
                return
