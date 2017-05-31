# Starting Hands
## A Quick way to check the score of your hand

### Adding folder:

Add this folder (starting_hands) to any local directory. You can do so by git cloning within that directory, 
or just creating one manually and copying the file content over.

If you do it manually be sure to name your files appropriately (you only need `hand.py` and `hands.py`)

Be sure to check that you have python installed. You can download it [here](https://www.python.org/downloads/)

### Create bash alias

Use vim to modify your bash profile file: `vi ~/.bash_profile`

**to enter text insert mode in vim, type `i`**

If you don't have it set up yet, you'll need to source it to your `.baschrc`:
```
# Path to the bash config
source ~/.bashrc
```

And then paste insert the function alias:
```
hand() {
    python ~/<whatever directory>/starting_hands/hand.py -s "$1"
}
```

Type `escape` to exit out of insert mode
Type `:wq` to write and quit out of the file.

Then you just need to source the changes. In console type: `source ~/.bash_profile`

And that should save the `hand` alias for you so you can trigger it on the console.

### Usage

In the console, simply type `$ hand <your_hand>`
your_hand is just the 2-3 letter abbreviation, appending a `!` for suited connectors, like `T9!`

You should get something like:
```
$ hand T9!
  Your hand ranks 23 out of 169
  Quality of hand is 86.98%
```

glhf!
