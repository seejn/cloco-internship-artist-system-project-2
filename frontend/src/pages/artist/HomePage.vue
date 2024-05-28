<template>
    <PageLayout>
        <template #main>
            <main class="container mx-auto px-6 py-8">
                <section class="mb-8">
                    <div class="bg-cover bg-center h-64 rounded-lg shadow-lg" style="background-image: url('https://via.placeholder.com/1200x400');">
                        <div class="bg-gray-900 bg-opacity-50 h-full flex items-center justify-center text-center">
                            <div>
                                <h1 class="text-4xl font-bold text-white">Featured Artist</h1>
                                <p class="text-gray-300 mt-2">Discover the latest hits from our featured artist.</p>
                            </div>
                        </div>
                    </div>
                </section>

                <section class="mb-8">
                    <h2 class="text-2xl font-bold mb-4">Latest Releases</h2>
                    <Songs :songs="songs" />
                </section>

                <section>
                    <h2 class="text-2xl font-bold mb-4">Popular Songs</h2>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                        <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                            <img src="https://via.placeholder.com/300" alt="Album Art" class="w-full h-40 object-cover">
                            <div class="p-4">
                                <h3 class="text-lg font-semibold">Song Title</h3>
                                <p class="text-gray-600">Artist Name</p>
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </template>
    </PageLayout>
</template>

<script>
    import Songs from '../../components/songs/card/SongCollection.vue'

    export default {
        components: {
            Songs
        },
        computed: {
            songs() {
                return this.$store.state.songs
            }
        },
        watch: {
            songs(newValue, oldValue) {}
        },
        mounted() {
            this.$store.dispatch("fetchSongs")
        }
    }
</script>