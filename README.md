# crusade-tracker

Crusade-tracker (working title) is a django-based project for tracking Warhammer 40k crusade Orders of Battle, as well as leagues. I'm using administratum.net as inspiration.

**This is far from ready for a release.** Please see the [initial release](https://github.com/powens/crusade-tracker/projects/1) project for the current status.

## Tech being used

Python 3.9

- Formatting: black

## Database Structure

OrderOfBattle

- Name
- Faction
- Player
- Description
- RP
- Created
- Modified

Unit

- Name
- Datasheet name
- Datasheet source
- Role
- Points/PL
- Is Character
- Is Psyker
- Is Battle Ready
- Other Rules
- Description
- ExpAdjustment
- Picture

Battles

- Opponent
-
