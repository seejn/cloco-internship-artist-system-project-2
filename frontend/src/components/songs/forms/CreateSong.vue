<template>
    <!-- {{ form }} -->
    <!-- {{ id }} -->
        <main class="container mx-auto px-6 py-8">
            <div class="bg-white rounded-lg shadow-lg p-6">
                <div class="flex justify-between items-center">
                    <h1 class="text-3xl font-bold mb-6">Add New Song</h1>
                    <div>
                        <button @click="$emit('handleClose')" class="bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Close</button>
                    </div>
                </div>
                <form @submit.prevent="createSong">
                    <div class="mb-6">
                        <label for="song-title" class="block text-gray-700 font-medium mb-2">Song Title</label>
                        <input v-model="form.title" type="text" id="song-title" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter song title">
                    </div>

                    <div class="mb-6">
                        <label for="duration" class="block text-gray-700 font-medium mb-2">Song's Duration</label>
                        <input type="text" v-model="form.duration" id="duration" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter duration of song">
                    </div>

                    <div class="mb-6" v-if="authUser.data.is_admin">
                        <label for="gender" class="block text-gray-700 font-medium mb-2">Artist</label>
                        <select v-model="id" id="gender" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                            <option value="" disabled selected>Select artist</option>
                            <option :value="`${artist.id}`" v-for="artist in artists">{{ artist.fullname }}</option>
                        </select>
                    </div>

                    <div class="mb-6">
                        <label for="release-date" class="block text-gray-700 font-medium mb-2">Release Date</label>
                        <input v-model="form.release_date" type="date" id="release-date" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>

                    <div class="mb-6">
                        <label for="genre" class="block text-gray-700 font-medium mb-2">Genre</label>
                        <input v-model="form.genre" type="text" id="genre" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter genre">
                    </div>

                    <div class="mb-6">
                        <label for="song-file" class="block text-gray-700 font-medium mb-2">Song File</label>
                        <input type="file" id="song-file" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>

                    <div>
                        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Create Song</button>
                    </div>
                </form>
            </div>
        </main>
</template>

<script>
    import axios from 'axios'

    export default {
        props: {
            artistId: Number,
        },
        data() {
            return {
                id: this.artistId,
                form: {},
                artists: {}
            }
        },
        computed: {
            authUser() {
                return this.$store.state.user
            }
        },  
        emits: ["handleClose"],
        methods: {
            async fetchArtists() {

                const url = `${import.meta.env.VITE_BASE_URL}/user/get_all_artists/`
                await axios(url, {
                    method: "get",
                    headers: {
                        "Authorization": `Bearer ${window.localStorage.getItem("access_token")}` 
                    },
                })
                .then((response) => {
                    console.log(response.data)
                    this.artists =  response.data.data
                })
                .catch((error) => {
                    console.log(error)
                })
            },
            async createSong() {
                const url = `${import.meta.env.VITE_BASE_URL}/user/${this.id}/create_song/`
                console.log(url)
                await axios(url, {
                    method: 'post',
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${this.$store.state.user.access}`
                    },
                    data: this.form
                })
                .then((response) => {
                    console.log(response.data)

                    this.$store.commit("addToast", {
                        title: response.statusText,
                        isError: false,
                        message: response.data.message
                    })

                    this.$emit("handleSubmit", response.data.data)
                    this.$emit("handleClose")
                })
                .catch((error) => {
                    console.log(error)
                })
            }
        },
        mounted() {
            this.fetchArtists()
        }
    }
</script>
