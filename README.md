tweet-newsfeed-classifier
=========================
All files with capitalized names contain class definitions with the same names.

The fundamental object is the API class which has methods which create and use instances of the other class types.

To run, the user will have to edit API.py so that a file containing a method that returns the user's twitter api is included. In the constructor for the API class set self.api to be equal to the return value of this method.

To use run main.py.