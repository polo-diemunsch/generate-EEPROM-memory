# generate-EEPROM-memory

This simple Python script converts user-input text into a hexadecimal representation using a predefined set of symbols. The output is saved to a file named "memory.hex".

## Usage

1. Run the script.
2. Enter the desired text when prompted.
3. The script will convert the text into hexadecimal values based on the provided symbol set.
4. The output will be saved to a file named "memory.hex" in the same directory as the script.

## Symbol Set

The script uses a set of symbols to represent each character. These symbols are defined in the script, and if a character is not found, it defaults to using the "#" symbol.

## Example

```python
python main.py
```
```
Enter your text:
> Hello, World!
```
The script will generate the corresponding hexadecimal values for each character and save them to "memory.hex".

## Notes
Make sure to keep the script and the symbol set updated if you want to add or modify symbols.
