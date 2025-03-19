
## Chapter-1: Getting Started with DuckDb
* installation: https://duckdb.org/docs/installation/?version=stable&environment=python
* (for linux CLI) Download  zip, extract and run: `~/Downloads/duckdb`

# SQL Statements
Enter SQLl statements ini CLI directly
; end-of-line

## Query Results
```
select v.* from values (1,), (2), (3) as v;

# output:
┌───────┐
│ col0  │
│ int32 │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```

# Dot commands
* single line, no semi-colone
.help



.open: close current database file and opens a new one 
.read : Reading SQL files to execute from within CLI
.tables: list the currently available tables and views
.timer on/off toggles SQL timing output
.maxrows: number of rows to show
.exit

# CLI arguments

`-readonly` : opens the database in read-only mode.
`-json` sets the output mode to json
`-line` sets the output mode to line
`-unsigned` allows for the loading of unsigned extensions

e.g.
`duckdb --json -c 'select v.* from values (1), (2), (3), (3), (7);`



# Extetnsion systesm:
* Packages you can install with duck db

* Description of extensions
```
DESCRIBE
SELECT *
FROM duckdb_extensions();
```

* installed extesnsions
```
SELECT extension_name, loaded, installed
FROM duckdb_extensions()
ORDER BY installed DESC, loaded DESC;
```

* install extension
```
INSTALL <extension_name>;
```

* load extension
```
LOAD <extension_name>;
```

* uninstall extension
```
UNINSTALL <extension_name>;
```

* comments
-- single line comment
/* Multi-line comment */

* Query files in internet
- use extension named: `httpfs`

```
INSTALL httpfs;
LOAD httpfs;
```

```
FROM duckdb_extensions()
SELECT loaded, installed, install_path
WHERE extension_name='httpfs';
```

# Analyzing a CSV file with the DuckDB CLI
```
SELECT count (*)
FROM 'https://github.com/bnokoro/Data-Science/raw/master/'
'countries%20of%20the%20world.csv';

-- output: 227
```

```
select count(*)
FROM 'https://bit.ly/3KoiZR0';

-- output: Error because url does not end with .csv


select count(*)
FROM read_csv_auto('https://bit.ly/3KoiZR0');
```

## Result model
 * Table based: work well with few columns
 * line based: Work well with many columns (takes alot more space than duckbox)

```
.mode line
SELECT *
FROM read_csv_auto('https://bit.ly/3KoiZR0')
LIMIT 1;
```


* count number of countries and find max. population average across all countries
```
.mode duckbox
SELECT count (*)  AS countries, 
    max(population) AS max_population,
    round(avg(cast("Area (sq. mi.)" as decimal) )) AS avgArea
FROM read_csv_auto('https://bit.ly/3KoiZR0');


/*
┌───────────┬────────────────┬──────────┐
│ countries │ max_population │ avgArea  │
│   int64   │     int64      │  double  │
├───────────┼────────────────┼──────────┤
│    227    │   1313973713   │ 598227.0 │
└───────────┴────────────────┴──────────┘
*/

* save result to file
```
./duckdb -csv \
-s "SELECT Country, Population, Birthrate, Deathrate
FROM read_csv_auto('https://bit.ly/3KoiZR0')
WHERE trim(region) = 'WESTERN EUROPE'" \
> western_europe.csv
```

* read first 6 lines using head tool
head -n6 western_europe.csv

* Writing to parquet file
```
./duckdb \
 -s "COPY (
    SELECT Country, Population,Birthrate, Deathrate
    FROM read_csv_auto('https://bit.ly/3KoiZR0')
    WHERE trim(region) = 'WESTERN EUROPE'
 )TO 'western_europe.parquet' (FORMAT PARQUET)"
```


* view content of parquet file usinig any parquet reader
`./duckdb -s "FROM 'western_europe.parquet' LIMIT 5"`

output
┌────────────────┬────────────┬───────────┬───────────┐
│    Country     │ Population │ Birthrate │ Deathrate │
│    varchar     │   int64    │  varchar  │  varchar  │
├────────────────┼────────────┼───────────┼───────────┤
│ Andorra        │      71201 │ 8,71      │ 6,25      │
│ Austria        │    8192880 │ 8,74      │ 9,76      │
│ Belgium        │   10379067 │ 10,38     │ 10,27     │
│ Denmark        │    5450661 │ 11,13     │ 10,36     │
│ Faroe Islands  │      47246 │ 14,05     │ 8,7       │
└────────────────┴────────────┴───────────┴───────────┘


# Summary
* available for: python, R, Node, ...
* CLI supports dot command
* `.mode <mode> for line, duckbox and ascii modes.
* can query CSV files dierectly from an HTTP server by installing httpfs extension
* can use CLI as step in an data pipelinee, whthout creating tables, by querying  external dataset and writing results to standard out or other files.