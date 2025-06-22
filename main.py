# Emanuel Biruk Seifegebreal - 2024 --> This project is for learning purposes
# To guess a number add in the search bar "/yourNumber"

from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num) # Print solution in the terminal

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<div style="width:100%;height:0;padding-bottom:76%;position:relative;"><iframe ' \
           'src="https://giphy.com/embed/90PPv7eqekhrO" width="200" height="400" style="position:absolute" ' \
           'frameBorder="0" allowFullScreen></iframe></div>'


@app.route("/<int:guess>")
def guess_num(guess):
    if guess == random_num:
        return '<h1 style="color: green">Good Job! You guessed right!</h1>' \
               '<div style="width:100%;height:0;padding-bottom:76%;position:relative;"><iframe ' \
               'src="https://giphy.com/embed/90PPv7eqekhrO" width="200" height="400" style="position:absolute" ' \
               'frameBorder="0" allowFullScreen></iframe></div>'
    elif guess > random_num:
        return '<h1 style = "color: blue">Too High!</h1>' \
               '<div style="width:100%;height:0;padding-bottom:76%;position:relative;"><iframe ' \
               'src="https://giphy.com/embed/90PPv7eqekhrO" width="200" height="400" style="position:absolute" ' \
               'frameBorder="0" allowFullScreen></iframe></div>'
    else:
        return '<h1 style = "color: red">Too Low!</h1>' \
               '<div style="width:100%;height:0;padding-bottom:76%;position:relative;"><iframe ' \
               'src="https://giphy.com/embed/90PPv7eqekhrO" width="200" height="400" style="position:absolute" ' \
               'frameBorder="0" allowFullScreen></iframe></div>'


if __name__ == "__main__":
    app.run(debug=True)
