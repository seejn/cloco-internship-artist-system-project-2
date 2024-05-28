<template>
    <PageLayout>
        <template #main>
            <span v-if="!isEditing">
                <main class="container mx-auto px-6 py-8">
                    <div class="bg-white rounded-lg shadow-lg p-6">
                        <div class="flex items-center flex-col md:flex-row mb-6">
                            <img src="https://via.placeholder.com/150" alt="Cover Art" class="w-32 h-32 rounded-lg mr-6">
                            <div>
                                <h1 class="text-3xl font-bold">{{ song.title }}</h1>
                                <p class="text-gray-600">
                                    <RouterLink :to="'/artist/profile/'+artist.id">{{ artist.fullname }}</RouterLink>
                                </p>
                            </div>
                        </div>
    
                        <!-- <div class="mb-6">
                            <audio controls class="w-full">
                                <source src="" type="audio/mpeg">
                                Your browser does not support the audio element.
                            </audio>
                        </div> -->
    
                        <!-- <div class="mb-6">
                            <h2 class="text-2xl font-bold mb-4">Lyrics</h2>
                            <pre class="bg-gray-100 p-4 rounded-lg overflow-auto">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
                                nisi ut aliquip ex ea commodo consequat.
                            </pre>
                        </div> -->
    
                        <div class="mb-6">
                            <h2 class="text-2xl font-bold mb-4">Song Information</h2>
                            <ul class="list-disc pl-5">
                                <li><strong>Release Date:</strong> {{ song.release_date }}</li>
                                <li><strong>Duration:</strong> {{ song.duration }}</li>
                                <li><strong>Genre:</strong> {{ song.genre }}</li>
                            </ul>
                        </div>
    
                        <div class="mb-6" v-if="userId === artist.id || authUser.data.is_admin">
                            <button @click="toggleEditing" class="bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Edit Song</button>
                        </div>
    
                    </div>
                </main>
            </span>
            <span v-else="isEditing">
                <EditSong :song="song" :artistId="artist.id" @handleSubmit="updateSong" @handleClose="toggleEditing" />
            </span>

        </template>
    </PageLayout>
</template>

<script>
    import EditSong from '../../components/songs/forms/EditSong.vue'

    import axios from 'axios'

    export default {
        components: {
            EditSong,
        },
        data() {
            return {
                isEditing: false,
                songId: this.$route.params.songId,
                song: {},
                artist: {},
            }
        },
        computed: {
            authUser() {
                return this.$store.state.user
            },
            userId() {
                return this.$store.state.user.data.id
            }
        },
        methods: {
            toggleEditing() {
                this.isEditing = !this.isEditing
            },
            updateSong(song) {
                this.song = song
            },
            async fetchSong() {
                const url = `${import.meta.env.VITE_BASE_URL}/song/${this.songId}/`
                await axios(url, {
                    method: "get"
                })
                .then((response) => {
                    this.song = response.data.data
                    this.artist = response.data.data.artist
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        },
        mounted() {
            this.fetchSong()
        }
    }
</script>
