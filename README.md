

Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.

To request data from the microservice programmatically, you'll need to create an input.txt file in the microservice directory. In this file, specify the number of movie suggestions you want and list the movies you've already seen, separated by commas. Save and close input.txt, then run the microservice script (movie_rec_micro.py). The microservice will read input.txt, process the data, and generate movie recommendations based on your input.



Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.


To programmatically receive data from the microservice, start by ensuring that the microservice script (movie_rec_micro.py) is up and running. Once the microservice has completed processing and generating movie recommendations, you can access the recommendations from the output file named output.txt. Read the contents of output.txt programmatically and process the received data based on your application's requirements. This could involve parsing the recommendations, displaying them to the user, or performing further processing as needed. After processing the recommendations from output.txt, it's advisable to clear the file to prepare it for the next set of recommendations. Following these steps will allow you to seamlessly receive and handle data outputted by the microservice.



UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader) will understand





+---------------+  +---------------+  +---------------+  +---------------+
|   Requester   |  |   input.txt   |  | Microservice  |  | output.txt    |
+---------------+  +---------------+  +---------------+  +---------------+
|write number of|                  |                  | 
|movie recs     |  --------------->|    read request  |
|desired and    |                  |                  |
|list of movies |                  |    write movie   | 
|previously     |                  |   recommendation |
|watched,       |                  |                  |
|separated by   |                   ----------------->| 
|commas         |                  |                  |
|               |                  |                  |
|               |                  |                  |
|read movie     |                  |                  |
|recommendation |<------------------------------------|




