
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version

from line import lib

VERSION_BANNER = get_version()


class Base(Controller):
    class Meta:
        label = 'base'
        
        title = _("sub-commands")

        # text displayed at the top of --help output
        description = _('App is calculated inital state of tape')

        # text displayed at the bottom of --help output
        epilog = _('Usage') + (': olymp-line command1 --foo bar')

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
        help=_('get inital state of tape'),

        # sub-command level arguments. ex: 'line command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-l', '--list' ],
              { 'help' : _('space-separated numbers simulating a folded tape, the number of digits in the set must be a multiple of 4'),
                'action'  : 'store',
                'type':float,
                'nargs':'*',
                'dest' : 'list' } ),
        ],
    )
    def istate(self):
        if self.app.pargs.list is not None and len(self.app.pargs.list)/4>=1 and len(self.app.pargs.list)%4==0:
            inital_tape = lib.find_initial_state_of_tape(self.app.pargs.list)
            data = {'inital_tape' : inital_tape}
            self.app.render(data, 'istate.jinja2')
