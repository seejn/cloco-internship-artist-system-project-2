<template>
    <PageLayout>
        <template #main>
            <Songs :songs="songs" />
        </template>
    </PageLayout>
</template>

<script>
    import Songs from '../components/songs/card/SongCollection.vue'

    export default {
        components: {
            Songs,
        },
        computed: {
            songs() {
                return this.$store.state.songs
            }
        },
        watch: {
            songs(newValue, oldValue){}
        },
        mounted() {
            this.$store.dispatch("fetchSongs")
        }
    }
</script>