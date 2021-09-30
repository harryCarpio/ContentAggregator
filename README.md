# ContentAggregator
A Content Aggregation Website is a place where people can go to see all latest news and contents from different places.
A content aggregator fetches information from various places online and gathers all of that information in one place. Therefore, you don’t have to visit multiple sites to get the latest info.


# Setting up
1. Clone repository 
```shell 
 git clone https://github.com/harryCarpio/ContentAggregator
```
2. Move into project
```shell 
cd ContentAggregator
```
3. Create a virtual environment and activate
```shell 
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
```
4. Install requeriments 
```shell
 pip install -r requirements.txt
```
5. Fetch feed news
```shell 
python manage.py aggregate
```
6. Run server 
```shell 
python manage.py runserver
```
7. Go to home Django home page http://127.0.0.1:8000/


# Features
* Fetch feed news from three sources
  * Mashable
  * The verge
  * TechCrunch
* Shows list of feed news on Django home page
  
# Tech Stack
* Django
* Sqlite
