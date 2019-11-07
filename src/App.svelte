<script>
    import Map from './view/components/Map.svelte'
    import MarkerLayer from './view/components/MarkerLayer.svelte'
    import data from './model/data.js'

    let filmLocations = data
    let titleSelection = '-'
    let yearSelection = '-'

    $: titles = Array.from(new Set(filmLocations.map(x => x["Title"]))).sort()
    $: years = Array.from(new Set(filmLocations.map(x => x["Release Year"]))).sort().reverse()

    function reset() {
        filmLocations = data
        titleSelection = '-'
        yearSelection = '-'
        // on reset, fire Select's clearAll
    }

    function filterByYear() {
        filmLocations = filmLocations.filter(x => x["Release Year"] === yearSelection)
    }

    function filterByTitle() {
        filmLocations = filmLocations.filter(x => x["Title"] === titleSelection)
    }

</script>
<style>
    #AppContainer {
        display: flex;
        flex-direction: column;
    }

    #controlContainer {
        display: flex;
        flex-direction: row;
        justify-content: center;
        width: 100vw;
        margin: auto;
        position: relative;
        z-index: 9999
    }

    #controlContainer > * {
        margin-left: 20px
    }

    #yearselect {
        width: 150px
    }

    #titleSelect {
        width: 250px
    }

    map {
        position: relative;
        z-index: -1
    }

    button {
        width: 100px
    }


</style>


<div id="AppContainer">

    <div id="controlContainer">
        <label>Release Year
            <select id="yearSelect" bind:value="{yearSelection}" on:change="{filterByYear}">
                <option value={yearSelection} selected disabled hidden>{yearSelection}</option>
                {#each years as year}
                    <option value="{year}">{year}</option>
                {/each}
            </select>
        </label>

            <label>Title
                <select id="titleSelect" bind:value="{titleSelection}" on:change="{filterByTitle}">
                <option value={titleSelection} selected disabled hidden>{titleSelection}</option>
                {#each titles as title}
                    <option value="{title}">{title}</option>
                {/each}
                </select>
            </label>
        <button on:click="{reset}">Reset</button>
    </div>

    <Map>
        <MarkerLayer data="{filmLocations}"/>
    </Map>
</div>
