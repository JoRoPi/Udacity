import bcrypt

# Hash a password for the first time, with a randomly-generated salt
password="1234"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print hashed

# gensalt's log_rounds parameter determines the complexity.
# The work factor is 2**log_rounds, and the default is 12
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
print hashed
hashed2=hashed[:10]+'J'+hashed[11:]
print hashed2

# Check that an unencrypted password matches one that has
# previously been hashed
#password="1233"
if bcrypt.hashpw(password, hashed2) == hashed:
        print "It matches"
else:
        print "It does not match"
