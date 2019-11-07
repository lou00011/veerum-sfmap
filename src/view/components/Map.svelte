<script>
    import { onMount, setContext } from 'svelte'
    import L from 'leaflet'

    setContext('map', {
        getMap: () => leafletMap
    })

    let leafletMap

    onMount(() => {
        leafletMap = L.map('MapContainer', {
            zoomControl: false
        })
        // Set the view to San Fran
        leafletMap.setView([37.7749, -122.4194], 13)

        // Get the OSM maplayer and apply to map instance
        let osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        })
        osmLayer.addTo(leafletMap)

        // Disabling all zoom and move functionality
        leafletMap.dragging.disable()
        leafletMap.touchZoom.disable()
        leafletMap.doubleClickZoom.disable()
        leafletMap.scrollWheelZoom.disable()
    })
</script>

<style>
    #MapContainer {
        height: 90vh;
        width: 99vw;
        margin: 0 auto;
    }
</style>

<div id="MapContainer">
    {#if leafletMap}
        <slot></slot>
    {/if}
</div>
