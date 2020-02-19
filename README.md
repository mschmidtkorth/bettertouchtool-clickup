# ClickUp Task View for Touch Bar with BetterTouchTool
Show the ClickUp task that became most recently due and the number of open tasks in a specific ClickUp list on your MacBook touch bar via BetterTouchTool. Tasks are colored based on their priority.

Never forget a task again!

## Requirements
- Execute `pip install requests` to install the Python requests module

## Installation & Configuration
1. Import the `ClickUp.bttpreset` preset (double-click)
2. Go to *Better Touch Tool > Preferences > All Apps > Touch Bar* and select "Shell Script/Task: ClickUp Inbox" from the list
3. Put your cursor into the text area field "Script" on the right side and replace all occurences of `1234567` with your ClickUp details:
- `https://api.clickup.com/api/v2/team/1234567/task` Id of your ClickUp Workspace
- `space_ids` (optional, uncomment) Id of your ClickUp Space
- `project_ids` Id of your ClickUp Project
- `list_ids` (optional, uncomment) Id of your ClickUp list
- `Authorization` Your ClickUp API token/key
4. Go to *Better Touch Tool > Preferences > All Apps > Touch Bar* and select "Shell Script/Task: Due Today" (below previous)
5. Put your cursor into the text area field "Script" on the right side and perform the same steps as above (URL is different)
- `https://api.clickup.com/api/v2/list/1234567/task` Id of your ClickUp list

*Note* The `.py` files are not to be used and only added for clarity. You may use them to edit the code more easily than in BetterTouchTool's prompt.

See [here](https://github.com/mschmidtkorth/alfred-clickup-msk#clickup-terminology) for an explanation of terminology and where to find the ClickUp Ids.

## How to Contribute

Please see the [contribution guidelines](CONTRIBUTING.md).

## Changelog

- **0.1.0** (2020-02-19)
  - Initial release