# DomainSearch
Monitor your network activity and list out domain names of websites you have visited. A search term is recommended to be used but it can list out every single one. Not all domains are 100% owned by the searched company but can be related in some ways (SSL, login stuff).
## Dependencies
- tshark^3.6
- python^3.10
## Usage
### Log your traffic into a file
```
$ bash ./generate.sh <output_filename>
```
Press CTRL+C to stop the monitoring.
### Filter out
```
$ python3 filter.py -i <output_filename_from_generate> -kw <search_term1> <search_term2> <search_term3>
```
where
- i means inputFile name and can be set as `-i dump`
- kw means KeywordList and can be set as `-kw snapchat tinder google facebook`.
## Example
```
$ bash ./generate.sh dump
```
Press CTRL+C
```
$ python3 filter.py -i "dump" -kw snapchat tinder > domainList
```
-h parameter is available for list of options
