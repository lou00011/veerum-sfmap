# Documentation

SF film location display in Svelte 3.0 and leaflet

## The stack

- JS Framework: Svelte 3
- Bundler: Rollup.js
- Transpiler: Babel
- Testing: Jest
- Map: Leaflet 
- Initial data cleanup: Python 3 w/ Pandas
- Database: SQLite3
- hosting: Netlify
- Source Control: Git

The project is done in multiple phases:

1. Because the location data are not good enough to create markers on map, Google Geocode API was used to get lat lng coordinate pair. (:wasgit)
2. Because how expensive the Geocode API call is, the data is saved into a database, SQLite3 was used for simplicity.
3. SQL is used to filter out unusable data and combine certain fields
4. Initially the project seeks to connect to SQLite3 directly at client side, and files were created to handle this connection (src/model/MovieData.js), the connection is not used and a flat json file is used instead for simplicity
5. Visualization is done using Leaflet because its ergonomics. Svelte 3 is used for performance.

## Setup

```
git clone
npm install
npm run serve
``` 
