<script>
    import { onMount } from 'svelte'
    import L from 'leaflet'
    // export let data;

    onMount(() => {
        let leafletMap = L.map('MapContainer', {
            zoomControl: false
        })
        // Set the view to San Fran
        leafletMap.setView([37.7749, -122.4194], 13)

        // Get the OSM maplayer and apply to map instance
        let OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        })

        OpenStreetMap_Mapnik.addTo(leafletMap)

        // Disabling all zoom funtionality
        leafletMap.dragging.disable()
        leafletMap.touchZoom.disable()
        leafletMap.doubleClickZoom.disable()
        leafletMap.scrollWheelZoom.disable()

        // Set markers
    })

    // Create a marker with appropriate popup and attach to map
    // function markerFactory(dataPt, map){
    //     const coordinate = L.LatLng(dataPt.lat, dataPt.lng)
    //     const popUp = L.popup('PLACEHOLDER TEXT')
    //    return L.marker(coordinate, {
    //         keyboard: false,
    //     }).bindPopup(popUp)
    //             .addTo(map)
    // }
</script>

<style>
    #MapContainer {
        height: 90vh;
        width: 99vw;
        margin: 0 auto;
    }
</style>

<div id="MapContainer"></div>
