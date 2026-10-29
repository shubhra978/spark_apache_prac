 #assign values to random column name or keys
select struct(1,2,3) 
#assign values with particular key names
select named_struct("a",1,"b",2) 

#mapping values to keys
select map(1, "c", 2, "d");
#finding values of each key
select map_values(map(1, "c", 2, "d"));
#finding key names
select map_keys(map(1, "c", 2, "d"));
