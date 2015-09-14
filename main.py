# Andrew Allbright
# Command line program template to ease development of future scripts.  The main idea
# is to be able to add arguments via configuration so I don't have to look up argparse
# anymore.

import argparse

# Models
def Arg(name,
        terminalVariableName=None,
        defaultValue=None,
        help='default help text'):
  return {
    'name': name,
    'terminalVariableName': terminalVariableName,
    'defaultValue': defaultValue,
    'help': str(help)
  }

# Utility FNs
def log(logText):
  # Easy to add volatile or more permanent log storage solution later.
  print(logText)

# Configuration
config = {
  'description': 'Description of program',
  'help': 'usage: python main.py -d directory --tmp temporary directory in case program failure',
  'args': [
    Arg('example', terminalVariableName='-d')
  ],
  'optionalArgs': [
    Arg('optionalExample', terminalVariableName='--tmp', defaultValue='/tmp')
  ]
}

# Get work done:
if __name__ == "__main__":
  log('---- - - - Program start... - - - ----')
  log('-- Program Description: %s  --' % config['description'])
  # Set up args -- fill in via config above
  parser = argparse.ArgumentParser(description=config['description'])

  for arg in config['args']:
    outputTextTmpl = '- - Argument registered with name of: %s, help text of: %s'
    log(outputTextTmpl % (arg['name'], arg['help']))
    parser.add_argument(arg['terminalVariableName'],
                        help=arg['help'],
                        default=arg['defaultValue'])

  for arg in config['optionalArgs']:
    outputTextTmpl = '- - Optional argument registered with name of: %s, help text of: %s'
    log(outputTextTmpl % (arg['terminalVariableName'], arg['help']))
    parser.add_argument(arg['terminalVariableName'],
                        nargs='?',
                        help=arg['help'],
                        default=arg['defaultValue'])

  args = parser.parse_args()

  print('Program primary function go')
  # Program function logic
  for key, value in dict(args.__dict__).iteritems():
    if value:
      print('.... Arg %s has value %s' % (key, value))

  # Program function logic end
  print('\n\n---- - - - Program complete! - - - ----\n\n\n')
