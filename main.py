print("      welcome to Guessing Game      ")
print("The word you are supposed to guess, we use it in our practical lives a lot because it is the future ")
secret_word="programming"
guess=""
guess_count =0
guess_limit=3
out_of_guessess = False

while guess != secret_word and not out_of_guessess :
       if guess_count < guess_limit:
           guess = input("enter guess")
           guess_count+=1
       else:
          out_of_guessess=True
if out_of_guessess:
    print("you lose out of guessess!")
else:
     print("YOU WIN")