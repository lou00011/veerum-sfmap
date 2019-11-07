<script>
    import { onMount, getContext, afterUpdate } from 'svelte'
    import L from 'leaflet'

    export let data

    const { getMap } = getContext('map')
    const map = getMap()
    let markerLayer = L.layerGroup().addTo(map)

    // Marker and popUp creation f(x)
    function markerFactory(dataPt) {
        const popUpText =
                `
                    <b>TITLE</b>: ${dataPt["Title"]} <br>
                    <b>YEAR</b>: ${dataPt["Release Year"]} <br>
                    <b>LOCATION</b>: ${dataPt["Locations"]} <br>
                    <b>ACTORS</b>: ${dataPt["Actor"]} <br>
                    <b>WRITER</b>: ${dataPt["Writer"]} <br>
                    <b>PRODUCTION COMPANY</b>: ${dataPt["Production Company"]}
                    `
        const popUp = L.popup()
        popUp.setContent(popUpText)
        const marker = L.marker([dataPt.lat, dataPt.lng])
        marker.bindPopup(popUp)
        marker.addTo(markerLayer)
    }

    function reset(){
        markerLayer.clearLayers()
    }

    function draw(){
        data.map(x => markerFactory(x))
    }

    // Lifecycle functions
    onMount(() => {
        draw()
    })

    afterUpdate(() => {
        reset()
        draw()
    })
</script>

