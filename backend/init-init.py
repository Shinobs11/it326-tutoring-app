import os, pathlib, importlib, ast, typing







modules = ['classes', 'factories', 'fields', 'models', 'serializers']
apiPath = pathlib.Path(os.getcwd() + '/api/')

for module in modules:
  modulePath = apiPath.joinpath(module)
  classFiles = [f for f in modulePath.iterdir() if (f.match('*.py') and not f.match('__init__.py'))]
  classDict: typing.Dict[str, str] = {}
  for filePath in classFiles:
    with open(filePath) as f:
      tree = ast.parse(f.read())
      for cl in tree.body:
        if(isinstance(cl, ast.ClassDef)):
          classDict[cl.name] = f'api.{module}.{filePath.name.removesuffix(".py")}'
  with open(modulePath.joinpath('__init__.py'), mode='w') as f:
    initString = ""
    initString += "try:\n"
    for k,v in classDict.items():
      initString+= f"\tfrom {v} import {k}\n"
    initString += "\nexcept ImportError:\n"
    for k,v in classDict.items():
      initString+= f"\tfrom .{v.split('.')[-1]} import {k}\n"
    f.write(initString)





