import getMovieData from './MovieData.js'

describe('Testing Fetching data from DB', () => {
    test('Valid - Able to get movie data from DB', async () => {
        const value = await getMovieData()
        expect(Array.isArray(value)).toBeTruthy()
        const [head, ...tail] = value
        expect(head).toHaveProperty('lat')
        expect(head).toHaveProperty('lng')
        expect(head).toHaveProperty('Title')
    })
})