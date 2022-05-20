# DomainSearch
Find domain names from your monitored browsing. Not all domains is 100% owned by the searched company but can be related in some ways (SSL, login stuff).

## Usage
### Log your traffic into a file
```
$ bash ./generate.sh <output_filename>
```
Press CTRL+C to stop the monitoring.
### Filter out
```
$ python3 filter.py <output_filename_from_generate> <search_term>
```
where the searchTerm should be a string with the terms **separated by a comma (,)**. 

### Example
```
$ bash ./generate.sh dump
```
Press CTRL+C
```
$ python3 filter.py dump snapchat,tinder > domainList
```
