# Pyramid Learning Journal
- Allan Liebold(allan.liebold@gmail.com)

A learning journal made using the Pyramid framework.
Heroku: https://sheltered-inlet-14538.herokuapp.com/

## Routes:

- `/` - home page, lists all journal entries
<<<<<<< HEAD
- `/journal/create-entry` - to create a new journal entry
=======
- `/journal/new-entry` - to create a new journal entry
>>>>>>> 53683f2ed619da31508974c742482f5b75f70a47
- `/journal/{id:\d+}` - view a specific entry
- `/journal/{id:\d+}/edit-entry` - edit an existing entry

## Set Up and Installation:

- `pip install` in a virtual environment (Python 3.6 recommended)

- `$ initdb development.ini` to initialize the journal entry database.

- `$ pserve development.ini` to serve the journal on `http://localhost:6543`

## To Test

- Install the `testing` extras. In the same directory as `setup.py` type:

```
$ pytest pyramid_learning_journal
```
<<<<<<< HEAD

=======
>>>>>>> 53683f2ed619da31508974c742482f5b75f70a47
