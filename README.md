# PTR-LM-Studio-Plugin
A "plug-in" for powertoys run that allows you to use LM Studio

This is not a real plugin for Powertoys Run but is a python script that sends a request (user defined prompt) to the local server (LM Studio)

## Installation

- Download the latest release of the [script](https://github.com/Bawsermatt/PTR-LM-Studio-Plugin/releases/tag/V1.0)
- Put AI.py and config.json in %userprofile%
- Enjoy

## Usage

- Press Alt + Space to open  Powertoys Run (If it doesn't work, check if it is enabled or if the shortcut is different)
- Type > AI.py + -Ask + "Whatever you think" (If it doesn't work, check if Shell command is enabled on Powertoys Run Plugin)
example:
```bash
  >AI.py -Ask "write me the pizza recipe"
```

## Settings

**API:** Set the API KEY.
**Temperature:** Set how much randomness to introduce. 0 will yield the same result every time, while higher values will increase creativity and variance.
**Model:** Set the name of the current model.
**Language:** Set the AI ​​language.

## License
[AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)
