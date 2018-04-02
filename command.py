from subprocess import call


class Command(object):

    @staticmethod
    def execute(cmd, params=None, output=False):

        return Command.__internal_execute(cmd, params, output)

    @staticmethod
    def __internal_execute(cmd, params, get_output):
        if not get_output:
            call([cmd, ', '.join(str(x) for x in params)])
        else:
            return call([cmd, ', '.join(str(x) for x in params)])

    def _init__(self, *args):
        super(Command, self).__init__(*args)
