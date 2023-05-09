class user:
    def __init__(self,name,hpass):
        self.name=name
        self.hpass=hpass
    def whoami(self):
        print("{} {}".format(self.name,self.hpass))
user1=user("Username","Password")
user.whoami()


with open("C:/Users/vikto/test.txt","a") as fichier:

    fichier.write("Password")
    fichier.write("\n | \n")
   