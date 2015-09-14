# Andrew Allbright
# This is meant to only read in one drone video at a time to produce the color image

import argparse
from pprint import pprint

# Models
def Arg(name,
        terminalVariableName='none',
        defaultValue='default value',
        help='default help text'):
  return {
    'name': str(name),
    'terminalVariableName': str(terminalVariableName),
    'defaultValue': str(defaultValue),
    'help': str(help)
  }

# configuration
config = {
  'description': 'Description of program',
  'help': 'usage: python main.py -d directory --tmp temporary directory in case program failure',
  'args': {
    'example': Arg('example', terminalVariableName='-d')
  },
  'optionalArgs': {
    'optionalExample': Arg('optionalExample', terminalVariableName='--tmp', defaultValue='/tmp')
  }
}

# Get work done:
if __name__ == "__main__":
  print('# Program Description: %s #' % config['description'])
  parser = argparse.ArgumentParser(description=config['description'])

  print('\n\n##Arguments')
  for name, arg in config['args'].iteritems():
    print('- - Argument registered with name of: %s, help text of: %s' % (arg['terminalVariableName'], arg['help']))
    parser.add_argument(arg['terminalVariableName'], help=arg['help'])

  print('\n###Optional arguments')
  for name, arg in config['optionalArgs'].iteritems():
    print('- - Optional argument registered with name of: %s, help text of: %s' % (arg['terminalVariableName'], arg['help']))
    parser.add_argument(arg['terminalVariableName'] or arg['name'], nargs='?', help=arg['help'])

  # Parse arguments if any
  args = parser.parse_args()
  pprint(dir(args))
  pprint(args)

  print('\n\nProgram complete!')

