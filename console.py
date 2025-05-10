import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_exit(self, arg):
        """Quit command to exit the program"""
        return True
    
    do_EOF = do_exit

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
        try:
            cls = arg()
        except NameError:
            print("** class doesn't exist **")

        my_model = cls()
        # save to json
        print(my_model.id)
    
    def do_show(self, args):
        cls, id = args.split(" ")
        if not cls:
            print("** class name missing **")
        else:
            try:
                model = cls()
            except NameError:
                print("** class doesn't exist **")
        if not id:
            print("** instance id missing **")
        else:
            try:
                model = cls()
            except NameError:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()