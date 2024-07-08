#!/user/bin/python3


# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
posts = 0 # total times we see pattern, "POST"

# open the file for reading
with open("/home/student/newcode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        #if this 'fail patter' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            #this statement assumes the if statement failed
        elif "POST" in line: #can ONLY be true if the "if" was false!
            posts += 1 # this is the total number of times we see "POST"

#display failed log in attempts
print("The number of failed log in attempts is", loginfail)


#display the number of successful log in attempts
print("The number of successful POSTs is", posts)
