RedShovel
=========

*Digging up the dirt from your redmine.*


Install 
-------

Currently the only version is the development version.  To install it
using pip follow these instructions.

```sh
pip install git+git://github.com/NeCTAR-RC/redshovel.git@master
```

Usage
-----

To authenticate you will need to use your access key, it can be
obtained by pressing my account, then looking in the margin on the
right for the show link under the API key heading.

Example usage:

```sh
rs-issue -u http://localhost/redmine/ -a xxxxxxxxxxxxxxxxxxxxxxxxxxxx -vv --project-id rc-support --tracker-id 3 
+------+---------+----------------+----------+----------------------------------------------+-----------------------+
|  ID  | Tracker |     Status     | Priority |                 Title                        |      Assigned To      |
+------+---------+----------------+----------+----------------------------------------------+-----------------------+
| 1309 | Support |  In Progress   |  Normal  | Issues with creating bananas from in sputnik |                       |
| 1306 | Support |      New       |  Normal  |             Snapshot is a success            |      Kam Orrison      |
+------+---------+----------------+----------+----------------------------------------------+-----------------------+
```

To prevent repetition values can be specified in a *~/.redshovel* file
in the format given below.:
```conf
[DEFAULT]
url = http://localhost/redmine/
api = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
