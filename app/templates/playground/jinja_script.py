from jinja2 import FileSystemLoader, Environment

# sample1. read file and output
loader = FileSystemLoader('playground')
env = Environment(loader=loader)
tmp = env.get_template('hello_world.txt')
tmp.render()

# output: 'hello world.'

# sample2. read file and replace variable
loader = FileSystemLoader('playground')
env = Environment(loader=loader)
tmp = env.get_template('replace.txt')
tmp.render(name='jack', animal='cat')

# output: 'jack got a cat'

# inheriter and html
tmp = env.get_template('father.html')
tmp.render(title='hi hi hi')
# output:
# '<html>\n    <head>\n    <title>hi hi hi</title>\n</head>\n    <body>\n     
#   \n    </body>\n</html>'

tmp = env.get_template('son.html')
tmp.render(title='hi title', body='content-content')

# output: '<html>\n    <head>\n    <title>hi title</title>\n</head>\n
#     <body>\n        \n    <p>\n        content-content\n
#     </p>\n\n    </body>\n</html>'

tmp = env.get_template('son.html')
tmp.render(title='t1', body='boody', items=[1, 2, 3, 4, 45, 5, 6, 7, 3])
''''<html>\n    <head>\n    <title>t1</title>\n</head>\n    <body>\n        \n    <p>\n
    boody\n    </p>\n\n    <hr>\n    \n    <ul>\n    \n       
         <li>1</li>\n    \n        <li>2</li>\n    \n       
              <li>3</li>\n    \n        <li>4</li>\n    \n      
                    <li>45</li>\n    \n
<li>5</li>\n    \n        <li>6</li>\n    \n        <li>7</li>\n    \n        <li>3</li>\n    \n
   </ul>\n\n\n    </body>\n</html>'''
