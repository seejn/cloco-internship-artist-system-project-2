<template>
    <PageLayout>
        <template #main>
            <span v-if="!isAdding && !isEditing">
                <main class="container mx-auto px-6 py-8">
                    <div class="bg-white rounded-lg shadow-lg p-6">
                        <div class="flex items-center  flex-col md:flex-row mb-6">
                            <img src="https://via.placeholder.com/150" alt="Artist Picture" class="w-32 h-32 rounded-full mr-6">
                            <div>
                                <h1 class="text-3xl font-bold">{{ artist.fullname }}</h1>
                                <p class="text-gray-600">Brief biography of the artist. This section can include a short introduction about the artist's background, career, and notable achievements.</p>
                                <div class="mt-4 space-x-4">
                                    <a href="#" class="text-blue-500 hover:text-blue-700">Twitter</a>
                                    <a href="#" class="text-blue-700 hover:text-blue-900">Facebook</a>
                                    <a href="#" class="text-purple-500 hover:text-purple-700">Instagram</a>
                                </div>
                            </div>
                        </div>
    
                        <div class="mb-6">
                            <div class="flex justify-between items center">
                                <h2 class="text-2xl font-bold mb-4">Artist Details</h2>
                                <div v-if="userId == artistId || authUser.data.is_admin">
                                    <button @click="toggleEditing" class="bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Edit Profile</button>
                                </div>
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div>
                                    <h3 class="text-lg font-semibold">Stage Name:</h3>
                                    <p class="text-gray-700">{{ artist.stagename }}</p>
                                </div>
                                <div>
                                    <h3 class="text-lg font-semibold">Date of Birth:</h3>
                                    <p class="text-gray-700">{{ artist.dob }}</p>
                                </div>
                                <div>
                                    <h3 class="text-lg font-semibold">Gender:</h3>
                                    <p class="text-gray-700">{{ artist.gender }}</p>
                                </div>
                                <div>
                                    <h3 class="text-lg font-semibold">Nationality:</h3>
                                    <p class="text-gray-700">{{ artist.nationality }}</p>
                                </div>
                            </div>
                        </div>
    
                        <div class="border-b mb-4">
                            <nav class="-mb-px flex items-center justify-between space-x-8">
                                <p class="text-gray-900 py-4 px-1 border-b-2 font-medium text-sm border-indigo-500">Songs</p>
                                <div v-if="userId == artistId">
                                    <button @click="toggleAdding" class="bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Add New Song</button>
                                </div>
                            </nav>
                        </div>
    
                        <Songs :songs="songs" />                    
    
                    </div>
                </main>
            </span>
            <span v-else-if="isAdding">
                <CreateSong :artistId="artist.id" @handleSubmit="addSong" @handleClose="toggleAdding" />
            </span>
            <span v-else="isEditing">
                <EditArtist :artist="artist" @handleSubmit="setArtist" @handleClose="toggleEditing" />
            </span>

        </template>
    </PageLayout>

</template>

<script>
    import Songs from '../../components/songs/card/SongCollection.vue' 
    import EditArtist from '../../components/users/forms/EditArtist.vue'
    import CreateSong from '../../components/songs/forms/CreateSong.vue'

    import axios from 'axios'

    export default {
        
        components: {
            Songs,
            EditArtist,
            CreateSong,
        },
        data() {
            return {
                isAdding: false,
                isEditing: false,
                artistId: this.$route.params.artistId,
                artist: {},
                songs: []
            }
        },
        computed: {
            userId() {
                return this.$store.state.user.data.id
            },
            authUser() {
                return this.$store.state.user
            },
            songs() {
                return this.songs.reverse()
            }
        },
        methods: {
            setArtist(artist) {
                this.artist = artist
            },
            addSong(song) {
                this.songs.push(song)
            },
            toggleEditing() {
                this.isEditing = !this.isEditing
            },
            toggleAdding() {
                this.isAdding = !this.isAdding
            },
            async fetchArtist() {
                const url = `${import.meta.env.VITE_BASE_URL}/user/get_artist/${this.artistId}/`
                await axios(url, {
                    method: 'get',
                })
                .then((response) => {
                    this.artist = response.data.data
                })
                .catch((error) => {
                    console.log(error)
                })
            },
            async fetchSongs() {
                const url = `${import.meta.env.VITE_BASE_URL}/user/${this.artistId}/get_songs/`
                await axios(url, {
                    method: 'get',
                })
                .then((response) => {
                    this.songs = response.data.data
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        },
        mounted() {
            this.fetchArtist()
            this.fetchSongs()
        }
    }
</script>