import datetime
import sublime
import sublime_plugin


class SignCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #load settings
        settings = sublime.load_settings("Sign.sublime-settings")
        #generate the timestamp
        timestamp_str = ''
        timestamp_str = '[' + settings.get('user_name', '') + ' @ '
        timestamp_str = timestamp_str + datetime.datetime.now().strftime(settings.get('date_format',''))
        timestamp_str = timestamp_str + '] '

        #for region in the selection
        #(i.e. if you have multiple regions selected,
        # insert the timestamp in all of them)
        for r in self.view.sel():
            if not settings.get('select_after_insert'):
                #put in the timestamp
                #(if text is selected, it'll be
                # replaced in an intuitive fashion)
                if r.size() > 0:
                    self.view.replace(edit, r, timestamp_str)
                else:
                    self.view.insert(edit, r.begin(), timestamp_str)
            else:
                self.view.replace(edit, r, timestamp_str)
