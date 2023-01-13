import sys

if (args_count := len(sys.argv)) > 3:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target directory")
    raise SystemExit(2)

command = sys.argv[1]

COMMAND_LIST = ['startapp']
HELPER = ['- startapp <app-name>']

if not command in COMMAND_LIST:
    print("Available commands: \n%s" % "\n".join(HELPER))
    raise SystemExit(2)

if args_count < 3:
    print("Application name not defined.")
    raise SystemExit(2)

appName = sys.argv[2]
appName = appName.replace(' ', '-').rstrip().lstrip()
pyName = '%s.py' % appName
htmlName = '%s.html' % appName

# bases
with open('bases/views.txt', 'r') as rf:
    bases_views = rf.read()
    rf.close()

with open('bases/controllers.txt', 'r') as rf:
    bases_controllers = rf.read()
    rf.close()

with open('bases/template.txt', 'r') as rf:
    bases_template = rf.read()
    rf.close()
#

# create views
with open('views/%s' % pyName, 'w') as wf:
    wf.write(bases_views.replace('{appName}', appName))
    wf.close()

# create controllers
with open('controllers/%s' % pyName, 'w') as wf:
    wf.write(bases_controllers.replace('{appName}', appName))
    wf.close()

# create template
with open('templates/%s' % htmlName, 'w') as wf:
    wf.write(bases_template.replace('{appName}', appName))
    wf.close()


print('Application successfully created!')