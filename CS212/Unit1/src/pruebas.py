def getTalk(type="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize()+"!"

    def whisper(word="yes") :
        return word.lower()+"...";

    # Then we return one of them
    if type == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout  
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()
talk1 = getTalk()
      

# You can see that "talk" is here a function object:
print talk, talk1
#outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print talk(), talk1()
