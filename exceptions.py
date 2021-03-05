class Impossible(Exception):
    '''Exception raised when an action is impossible to be preformed.

    The reason is given as the exception message.
    '''

class QuitWithoutSaving(SystemExit):
    '''Can be raised to exit the game without automatically saving.'''