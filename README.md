# ElasticSearch - Search-as-you-type Demo
Steps to activate the demo:
* Run ElasticSearch on local machine.
if ElasticSearch is running in a diffrent location, edit the api files on line 13 with the correct host.
* Open a terminal and run: `python ./Frontend/app.py`. The Frontend service will run in the terminal.
* Open another terminal and run: `python ./Backend/api_with_prefix.py` or `python ./Backend/api_with_ngram.py`. This will also run continuously in the terminal.
* Open another terminal and run `python ./reindex_with_prefix.py` or `python ./reindex_with_ngram.py` corisponding to the api file you ran in the previous step.
* Open the brawser on [localhost:5000](http://localhost:5000/) and start searching!
* Before reindexing, stop the Backend service. Deactivate it (the corresponding to the reindexing file) when the reindex is finished.