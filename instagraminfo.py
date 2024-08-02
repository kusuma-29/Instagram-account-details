# install instaloader by using---pip install instaloader
import instaloader
# creating an Instaloader() object
object=instaloader.Instaloader()
# Taking the instagram username as input from user
username=input("Enter username:")
#Fetching the details of provided useraname using instaloder object
profile=instaloader.Profile.from_username(object.context, username)
# Printing the fetched details and storing the profile pic of that account
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username+" is having " + str(profile.followers)+' followers.')
print(profile.username+" is following " + str(profile.followees)+' people')
print("Bio: ", profile.biography)
