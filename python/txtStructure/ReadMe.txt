Simle script that creates *.txt structure for one year like so:

2020/
├── 01_january/
│   ├── 01.txt
│   ├── 02.txt
│   ├── 03.txt
│   ├── 04.txt
│   └── 05.txt
├── 02_february/
│   ├── 01.txt
│   ├── 02.txt
│   ├── 03.txt
│   ├── 04.txt
│   └── 05.txt
...

and so on.

*.txt content example:
01.txt
	date 01.01.2020
	date 02.01.2020
	date 03.01.2020
	date 04.01.2020
	date 05.01.2020

filled *.txt content example:
01.txt
	date 01.01.2020
	+ read 10 pages
	+ write PySide conspect
	- watch Blender tutorial
	+- python lessons:
	{
	+ tuple tutorial
	+ stroke totorial
	- dictionry tutorial
	+ functions
	}
	[3] read 10 pages
	<!> 8


It is used to create digital diary, where you can list your every day tasks. Works for every year.
If you will use similar syntax for all days, you can create script to parse this diary. 
Also this diary was made as a part of time management system also known as "tomato method". 
In this system every 25minets count as a cycle.

You can use for example this syntax for tasks:
-      => not done
+      => done
+-     => particularly done
<!>    => how many cycles done for a day
[]     => how many days in a row some task was comleted
tasks: => group of tasks
{
	+/-/+- task 1
	+/-/+- task 2
	+/-/+- task 3
}

