create table films_cleaned as
select 
"index",
"Release Year",
title,
Locations,
lat,
long as lng,
"Production Company",
"Distributor",
case
  when "Actor 1" is null then null
  when "Actor 2" is null then "Actor 1"
  when "Actor 3" is null then "Actor 1" || ', & ' || "Actor 2"
  else "Actor 1" || ', ' || "Actor 2" || ', & ' || "Actor 3"
  end as Actor,
  writer,
  "Fun Facts"
from films
where not(lat is null or long is null)


select