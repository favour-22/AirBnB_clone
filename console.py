#!/usr/bin/python3
"""The prompt class"""
import cmd

class HBNBCommand(cmd.Cmd):
    """DEFINES THE HBNB COMMAND INTERPRETER
    Attributes:
        prompt (hbnb): The command prompt.
    """
    prompt = "(hbnb)"
    
    def empty_line(self):
        """Execute nothing when enter is pressed"""
        pass
    def do_quit(self, arg):
        """Quit the hbnb prompt when called"""
        return True
    def do_EOF(self, arg):
        """EOF siginal to exit the program"""
        print("")
        return True
    



if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
