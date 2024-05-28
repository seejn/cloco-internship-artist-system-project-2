<template>
    <h2 class="text-2xl font-bold m-4">Artists</h2>
    <section class="mb-8 flex flex-wrap justify-evenly">
            <Artist v-for="artist in artists" :artist="artist" />
    </section>
</template>

<script>
    import Artist from './ArtistCard.vue'

    export default {
        components: {
            Artist
        },
        computed: { 
            artists() {
                return this.$store.state.artists
            }
        },
        watch: {
            artists(newValue, oldValue) {
                console.log(`Artist Update from ${oldValue} to ${newValue}`)
            }
        },
        mounted() {
            this.$store.dispatch("fetchArtists")
        }
    }
</script>