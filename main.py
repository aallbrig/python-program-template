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

def log(logText):
  # Easy to add volatile or more permanent solution later.
  print(logText)

# configuration
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

  log('\n## Arguments')
  for arg in config['args']:
    outputTextTmpl = '- - Argument registered with name of: %s, help text of: %s'
    log(outputTextTmpl % (arg['name'], arg['help']))
    parser.add_argument(arg['terminalVariableName'],
                        help=arg['help'],
                        default=arg['defaultValue'])

  log('\n### Optional arguments')
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

  print('....You passed in %s for -d' % (args.d))
  if args.tmp:
    print('....You passed in %s for --tmp' %(args.tmp))

  # Program function logic end
  print('\n\n---- - - - Program complete! - - - ----\n\n\n')

