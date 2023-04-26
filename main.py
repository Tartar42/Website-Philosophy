from website import create_app
#u can import stuff from multiple python-files from a folder if u type its' name 
app = create_app()

if __name__ == '__main__':
#only if we run this file (not if we inout this file), are we going to execute this line
    app.run(debug=True)
    #runs this application. debug=True = means that every time we make a change in our python code
    #the app is going to rerun
    #without it we would have to manually rerun the app every time we made a change

#if Terminal didn't find flask: Strg+Shift+P -> type "python: select interpreter" -> then: the version u want
#to use of python

#sources:
  #For creating website: https://www.youtube.com/watch?v=dam0GPOAvVI&list=PLsCTnBEpCwH-MZja6wejVZ6sdMbghuGYd&index=32&t=53s
  #For creating database: 
  #For fixing problems:
