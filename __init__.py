from __future__ import absolute_import
import octoprint.plugin

class OctoButtonPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SimpleApiPlugin,
                       octoprint.plugin.AssetPlugin):

    # This method will run when OctoPrint starts up
    def on_after_startup(self):
        self._logger.info("OctoButton Plugin started")

    # This method is required for the TemplatePlugin mixin
    # We will use it to inject our JavaScript file into the page
    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    # This method is required for the AssetPlugin mixin
    # We will use it to tell OctoPrint where our JavaScript file is
    def get_assets(self):
        return dict(
            js=["js/octo_relay.js"]
        )

    # This method is required for the SimpleApiPlugin mixin
    # We will use it to handle requests from our JavaScript
    def on_api_command(self, command, data):
        if command == "octo_relay_on":
            self._logger.info("Running script...")
            subprocess.Popen(["python", "/home/pi/relaySwitch.py", "-state on"])
        elif command == "octo_relay_off":
            subprocess.Popen(["python", "/home/pi/relaySwitch.py", "-state on"])

__plugin_name__ = "OctoButton"
__plugin_pythoncompat__ = ">=2.7,<4"
def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = OctoButtonPlugin()