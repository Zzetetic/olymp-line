
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version

from line import lib

VERSION_BANNER = """
MyApp Does Amazing Things! %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'MyApp Does Amazing Things!'

        # text displayed at the bottom of --help output
        epilog = 'Usage: line command1 --foo bar'

        # controller level arguments. ex: 'line --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help='example sub command1',

        # sub-command level arguments. ex: 'line command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-l', '--list' ],
              { 'help' : 'space-separated numbers simulating a folded tape',
                'action'  : 'store',
                'type':float,
                'nargs':'*',
                'dest' : 'list' } ),
        ],
    )
    def istate(self):
        if self.app.pargs.list is not None:
            inital_tape = lib.find_initial_state_of_tape(self.app.pargs.foo)
            data = {'inital_tape' : inital_tape}
            self.app.render(data, 'istate.jinja2')
