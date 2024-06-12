# OctoPi Relay Plugin

This README documents the OctoPi Relay Plugin, which allows users to remotely control the power state of a 3D printer connected to a Raspberry Pi via GPIO pins. The plugin provides a simple user interface on the OctoPrint web control panel for turning the printer on and off.

## Features

- **Web Control Interface**: Adds buttons to the OctoPrint control panel for turning the 3D printer on and off.
- **GPIO Control**: Utilizes the Raspberry Pi's GPIO pins to control a relay that powers the 3D printer.

## Installation

1. **Setup OctoPrint**:
   Ensure that OctoPrint is installed and running on your Raspberry Pi. If not installed, follow the official OctoPrint setup guide.

2. **Install Plugin**:
   Copy the plugin files into the OctoPrint plugin directory and restart OctoPrint.

3. **Hardware Setup**:
   Connect a relay to the specified GPIO pin on your Raspberry Pi. Ensure that the relay is compatible with the GPIO voltage levels and can handle the power requirements of the 3D printer.

## Usage

After installation, two new buttons will appear on the OctoPrint web interface:
- **Turn printer on**: Sends a signal to the relay to power the printer on.
- **Turn printer off**: Sends a signal to the relay to power the printer off.

These actions are executed through AJAX calls from the web interface, which in turn trigger the Raspberry Pi GPIO to activate/deactivate the relay.

## Configuration

You can modify the GPIO pin used by editing the Python script argument `--pin`. The default GPIO pin is 24.

## Security Considerations

Ensure that your OctoPrint installation is secure to prevent unauthorized access to the relay controls.

## Dependencies

- OctoPrint
- RPi.GPIO Python library (pre-installed on Raspberry Pi OS)

## Limitations

- The plugin does not currently support feedback mechanisms to verify the state of the printer.
- Ensure the GPIO setup and relay used are capable of handling the power load safely to prevent any electrical hazards.

## License

This software is provided "as is", without warranty of any kind. Use at your own risk.
