import * as sqlite from 'sqlite3'
import {notDeepEqual} from "assert"
import 'fs'

const dbFile = '/film.db'
function getDB() {
    return new sqlite.Database(dbFile,
        (err) => {
            if (err) {
                throw new Error(err)
            }
        })
}
function getAllData(db){
    // rows :: [{ }]
     return new Promise((resolve, reject) => {
         let sql = `
         select * from films_cleaned
         order by "Release Year" DESC, Title ASC
         `
        db.all(sql, [], (err, rows) =>
            err ? reject(err) : resolve(rows))
    })
}

export default async function getMovieData(){
    try {
        const db = getDB()
        notDeepEqual(db, undefined, 'db is null')
        const data = await getAllData(db)
        notDeepEqual(data, undefined, 'data is null')
        db.close()
        return data
    } catch (error){
        console.log(error)
        return []
    }
}



