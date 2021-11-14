# Seed Encode

A small tool that explores encoding bip39 seed words in customizable character sets.

Disclaimer, this project has not been tested for portability, nor security, it is merely a sharing of my thought experiment on the topic.

You should NEVER put your seed words on a public, internet connected or network connected computer/device.

USE AT YOUR OWN RISK! 🙀

## Installation
Requires **python3** and **virtualenv**:

```
# clone repo
$ git clone git@github.com:CypherToad/seed_encode.git

# create virtual env
$ virtualenv -p python3 venv/

# activate virtual env
$ source venv/bin/activate

# install requirements
(venv) $ pip install -r requirements.txt
```

## Usage

To run encoding merely call `seed_encode.py` with the **set** you with to encode with:

```
$ ./seed_encode.py sets/animals.txt
```

If everything goes well you should be overloaded with data, most of the output is debug confirming encoding and decoding:

```
[WARNING] MAKE SURE THIS IS A SAFE COMPUTER, AND NO ONE IS WATCHING !!

Seed phrase: drum mango crystal sudden palm keep witness slam among echo blush balance spot bargain live cherry neck kidney clock extend much defy tumble surprise

[DEBUG] random word from secret_words is "among"
[DEBUG] word "among" encodes as combo "🐀🦂"
[DEBUG] combo "🐀🦂" decodes as word "among"
[DEBUG] passed!

[DEBUG] secret_words is: ['drum', 'mango', 'crystal', 'sudden', 'palm', 'keep', 'witness', 'slam', 'among', 'echo', 'blush', 'balance', 'spot', 'bargain', 'live', 'cherry', 'neck', 'kidney', 'clock', 'extend', 'much', 'defy', 'tumble', 'surprise']
[DEBUG] combos for your secret_words: ['🐅🐀', '🐊🐁', '🐃🦭', '🐑🐄', '🐋🦛', '🐉🐂', '🐓🦒', '🐐🐄', '🐀🦂', '🐅🐔', '🐁🦝', '🐁🐢', '🐐🦅', '🐁🐪', '🐉🦌', '🐂🦩', '🐊🦬', '🐉🐇', '🐃🐘', '🐅🪳', '🐊🦕', '🐄🐞', '🐒🐧', '🐑🐔']
[DEBUG] secret_words from your combos: ['drum', 'mango', 'crystal', 'sudden', 'palm', 'keep', 'witness', 'slam', 'among', 'echo', 'blush', 'balance', 'spot', 'bargain', 'live', 'cherry', 'neck', 'kidney', 'clock', 'extend', 'much', 'defy', 'tumble', 'surprise']
[DEBUG] passed!

------------------------------------

🐅🐀 => drum
🐊🐁 => mango
🐃🦭 => crystal
🐑🐄 => sudden
🐋🦛 => palm
🐉🐂 => keep
🐓🦒 => witness
🐐🐄 => slam
🐀🦂 => among
🐅🐔 => echo
🐁🦝 => blush
🐁🐢 => balance
🐐🦅 => spot
🐁🐪 => bargain
🐉🦌 => live
🐂🦩 => cherry
🐊🦬 => neck
🐉🐇 => kidney
🐃🐘 => clock
🐅🪳 => extend
🐊🦕 => much
🐄🐞 => defy
🐒🐧 => tumble
🐑🐔 => surprise


[DEBUG] Secret is length 48 without spaces.
🐅🐀 🐊🐁 🐃🦭 🐑🐄 🐋🦛 🐉🐂 🐓🦒 🐐🐄 🐀🦂 🐅🐔 🐁🦝 🐁🐢 🐐🦅 🐁🐪 🐉🦌 🐂🦩 🐊🦬 🐉🐇 🐃🐘 🐅🪳 🐊🦕 🐄🐞 🐒🐧 🐑🐔

[WARNING] MAKE SURE THIS IS A SAFE COMPUTER, AND NO ONE IS WATCHING !!

Encoded seed phrase: 🐅🐀 🐊🐁 🐃🦭 🐑🐄 🐋🦛 🐉🐂 🐓🦒 🐐🐄 🐀🦂 🐅🐔 🐁🦝 🐁🐢 🐐🦅 🐁🐪 🐉🦌 🐂🦩 🐊🦬 🐉🐇 🐃🐘 🐅🪳 🐊🦕 🐄🐞 🐒🐧 🐑🐔
[DEBUG] Encoded seed phrase decoded to:
 ['drum', 'mango', 'crystal', 'sudden', 'palm', 'keep', 'witness', 'slam', 'among', 'echo', 'blush', 'balance', 'spot', 'bargain', 'live', 'cherry', 'neck', 'kidney', 'clock', 'extend', 'much', 'defy', 'tumble', 'surprise']

Save to combos.txt (y/n): y
[DEBUG] Saving full sheet combos.txt
```

If all went well you have a `combos.txt` file containing character combos for each of the 2048 bip39 seed words.

Some sets don't contain enough characters to encode each of our 2048 seed words,
and we may see **errors** as follows:

```
$ ./seed_encode.py sets/ps4.txt
[WARNING] MAKE SURE THIS IS A SAFE COMPUTER, AND NO ONE IS WATCHING !!

Seed phrase: drum mango crystal sudden palm keep witness slam among echo blush balance spot bargain live cherry neck kidney clock extend much defy tumble surprise

[ERROR] Not enough combos to map 2048 seed words, increase repeat.
```

In these cases we need to increase our **repeat**, or how many characters for seed word we wish to use:

```
$ ./seed_encode.py sets/ps4.txt --repeat 4
[WARNING] MAKE SURE THIS IS A SAFE COMPUTER, AND NO ONE IS WATCHING !!

Seed phrase: drum mango crystal sudden palm keep witness slam among echo blush balance spot bargain live cherry neck kidney clock extend much defy tumble surprise

[DEBUG] random word from secret_words is "mango"
[DEBUG] word "mango" encodes as combo "RL▲R"
[DEBUG] combo "RL▲R" decodes as word "mango"
[DEBUG] passed!

[DEBUG] secret_words is: ['drum', 'mango', 'crystal', 'sudden', 'palm', 'keep', 'witness', 'slam', 'among', 'echo', 'blush', 'balance', 'spot', 'bargain', 'live', 'cherry', 'neck', 'kidney', 'clock', 'extend', 'much', 'defy', 'tumble', 'surprise']
[DEBUG] combos for your secret_words: ['L→↑L', 'RL▲R', 'L↑x↓', 'R■←x', 'Rx■↑', 'L●■↑', 'xLxR', 'R↓x↑', 'LL↓←', 'L→→●', 'LR●↓', 'LR↑R', 'R↓▲↓', 'LR↑●', 'RL↑→', 'L←R→', 'RR▲R', 'L●■●', 'L←↑■', 'L↓↑■', 'RR↓L', 'L↑↓R', 'R▲■↑', 'R■↑■']
[DEBUG] secret_words from your combos: ['drum', 'mango', 'crystal', 'sudden', 'palm', 'keep', 'witness', 'slam', 'among', 'echo', 'blush', 'balance', 'spot', 'bargain', 'live', 'cherry', 'neck', 'kidney', 'clock', 'extend', 'much', 'defy', 'tumble', 'surprise']
[DEBUG] passed!

------------------------------------

L→↑L => drum
RL▲R => mango
L↑x↓ => crystal
R■←x => sudden
Rx■↑ => palm
L●■↑ => keep
xLxR => witness
R↓x↑ => slam
LL↓← => among
L→→● => echo
LR●↓ => blush
LR↑R => balance
R↓▲↓ => spot
LR↑● => bargain
RL↑→ => live
L←R→ => cherry
RR▲R => neck
L●■● => kidney
L←↑■ => clock
L↓↑■ => extend
RR↓L => much
L↑↓R => defy
R▲■↑ => tumble
R■↑■ => surprise


[DEBUG] Secret is length 96 without spaces.
L→↑L RL▲R L↑x↓ R■←x Rx■↑ L●■↑ xLxR R↓x↑ LL↓← L→→● LR●↓ LR↑R R↓▲↓ LR↑● RL↑→ L←R→ RR▲R L●■● L←↑■ L↓↑■ RR↓L L↑↓R R▲■↑ R■↑■

[WARNING] MAKE SURE THIS IS A SAFE COMPUTER, AND NO ONE IS WATCHING !!

Encoded seed phrase: L→↑L RL▲R L↑x↓ R■←x Rx■↑ L●■↑ xLxR R↓x↑ LL↓← L→→● LR●↓ LR↑R R↓▲↓ LR↑● RL↑→ L←R→ RR▲R L●■● L←↑■ L↓↑■ RR↓L L↑↓R R▲■↑ R■↑■
[DEBUG] Encoded seed phrase decoded to:
 ['drum', 'mango', 'crystal', 'sudden', 'palm', 'keep', 'witness', 'slam', 'among', 'echo', 'blush', 'balance', 'spot', 'bargain', 'live', 'cherry', 'neck', 'kidney', 'clock', 'extend', 'much', 'defy', 'tumble', 'surprise']

Save to combos.txt (y/n): y
[DEBUG] Saving full sheet combos.txt
```

## Examples

Have a look at some of the example sets in the `examples/` directory.

Feel free to open a pull request and share some of your sets!

## License

  * https://www.gnu.org/licenses/gpl-3.0.txt

## Questions

  [@CypherToad](https://twitter.com/CypherToad) - Twitter
