import readline

# Most of the CmdCompleter class was originally written by John Kenyan
# It serves to tab-complete commands inside the program's shell
class CmdCompleter:
    def __init__(self, commands):
        self.commands = commands

    # Traverses the list of available commands
    def traverse(self, tokens, tree):
        retVal = []

        # If there are no commands, or no user input, return null
        if tree is None or len(tokens) == 0:
            retVal = []
        # If there is only one word, only auto-complete the primary commands
        elif len(tokens) == 1:
            retVal = [x+' ' for x in tree if x.startswith(tokens[0])]
        # Else auto-complete for the sub-commands
        elif tokens[0] in tree.keys():
            retVal = self.traverse(tokens[1:],tree[tokens[0]])

        return retVal

    # Returns a list of possible commands that match the partial command that the user has entered
    def complete(self, text, state):
        try:
            tokens = readline.get_line_buffer().split()
            if not tokens or readline.get_line_buffer()[-1] == ' ':
                tokens.append('')
            results = self.traverse(tokens,self.commands) + [None]
            return results[state]
        except Exception as e:
            print("Failed to complete command: %s" % str(e))

        return