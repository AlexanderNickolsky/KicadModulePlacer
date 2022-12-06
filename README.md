# KicadModulePlacer

## What is KicadModulePlacer

This is a Kicad PCB editor plugin that helps to place modules at pre-computed coordinates.

## Who may need it

I am using it to place LEDs on boards. Any project that comprises many similar components, like LEDs, logic gates, diodes, resistors, etc.
arranged in a systematic order may benefit from this plugin.

## How to use it

1. Install the plugin as usual. See https://dev-docs.kicad.org/en/python/pcbnew/

2. Create a file in your favorite spreadsheet program (Libre Office, Microsoft Office, whatever)

3. Calculate coordinates for modules. You need at least three colums: module name, X coordinate, Y coordinate.
You may want to add the third one for rotation. Select the range with coordinates, copy and paste it into a plain text
file. coord.txt is a good name for it.

4. Start the plugin in the Kicad PCB editor using Tools - External Plugins - Module Placer. File selection dialog will appear.
Open your coord.txt file.

5. That's it. You may want to close the file and reopen it for ratsnests to be re-created.

There is an example project in the ModulePlacerTesting folder.
