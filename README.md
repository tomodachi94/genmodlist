# genmodlist

Generate a readable Minecraft mod list from a directory of Minecraft mods.


## Development philosophy
This follows the philosophy of 'do one thing, and do it well'; bug fixes and support for new metadata formats will certainly be added, but more features will not (just use shell pipes ffs).

## Usage instructions

```sh
pip install toml
python3 ./genmodlist.py --help
# Read the instructions!
python3 ./genmodlist.py --directory "~/.local/share/PrismLauncher/instances/Tekkit/.minecraft/mods"
# Or, shorter:
python3 ./genmodlist.py -d "~/.local/share/PrismLauncher/instances/SkyFactory 4/.minecraft/mods"
```

## Advanced usage
See 'Development philosophy'. You can do a lot of neat things by just chaining commands together.

### Surround the mod list in wikilinks
Use this program chained with `sed`:
```sh
./genmodlist.py -d path/to/.minecraft/mods | sed -e "s/\(.*\)/[[\1]]/"
```
