from __future__ import absolute_import
import octoprint.plugin
import flask
import subprocess
import os

class OctoPiRelayPlugin(octoprint.plugin.StartupPlugin,
                        octoprint.plugin.TemplatePlugin,
                        octoprint.plugin.AssetPlugin,
                        octoprint.plugin.SettingsPlugin,
                        octoprint.plugin.BlueprintPlugin):

    def on_after_startup(self):
        self._logger.info("OctoPiRelay Plugin started")
        
    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/octopirelayplugin.js"]
        )
    
    def handle_output(self, process):
        stdout, stderr = process.communicate()
        self._logger.info(stdout.decode('utf-8'))
        if stderr:
            self._logger.error(stderr.decode('utf-8'))

    @octoprint.plugin.BlueprintPlugin.route("/relay", methods=["POST"])
    def handle_relay(self):
        relay_script_dir = os.path.dirname(os.path.realpath(__file__))
        relay_script_path = os.path.join(relay_script_dir, "relaySwitch.py")

        command = flask.request.json.get("command")
        
        if command == "octo_relay_on":
            self._logger.info("Turning on relay...")
            p = subprocess.Popen(["python3", relay_script_path, "-state", "on"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.handle_output(p)
        elif command == "octo_relay_off":
            self._logger.info("Turning off relay...")
            p = subprocess.Popen(["python3", relay_script_path, "-state", "off"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.handle_output(p)
        else:
            return flask.make_response("Unknown command", 400)
        return flask.make_response("Success", 200)

__plugin_name__ = "octopirelayplugin"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = OctoPiRelayPlugin()
