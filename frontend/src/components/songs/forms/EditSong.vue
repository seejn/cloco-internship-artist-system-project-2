<template>
        <main class="container mx-auto px-6 py-8">
            <div class="bg-white rounded-lg shadow-lg p-6">
                <div class="flex justify-between items-center">
                    <h1 class="text-3xl font-bold mb-6">Edit Song</h1>
                    <div>
                        <button @click="$emit('handleClose')" class="bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Close</button>
                    </div>
                </div>
                <form @submit.prevent="saveChanges">
                    <div class="mb-6">
                        <label for="song-title" class="block text-gray-700 font-medium mb-2">Song Title</label>
                        <input v-model="form.title" type="text" id="song-title" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter song title">
                    </div>

                    <!-- <div class="mb-6">
                        <label for="artist-name" class="block text-gray-700 font-medium mb-2">Artist Name</label>
                        <input type="text" id="artist-name" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter artist name">
                    </div> -->

                    <div class="mb-6">
                        <label for="release-date" class="block text-gray-700 font-medium mb-2">Release Date</label>
                        <input v-model="form.release_date" type="date" id="release-date" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>

                    <div class="mb-6">
                        <label for="genre" class="block text-gray-700 font-medium mb-2">Genre</label>
                        <input v-model="form.genre" type="text" id="genre" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter genre">
                    </div>

                    <div class="mb-6">
                        <label for="duration" class="block text-gray-700 font-medium mb-2">Duration</label>
                        <input v-model="form.duration" type="text" id="duration" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter duration">
                    </div>

                    <div class="mb-6">
                        <label for="song-file" class="block text-gray-700 font-medium mb-2">Upload New Song File</label>
                        <input type="file" id="song-file" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>

                    <div>
                        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Save Changes</button>
                    </div>
                </form>
            </div>
        </main>

</template>

<script>
    import axios from 'axios'

    export default {
        props: {
            song: Object,
            artistId: Number,
        },
        data() {
            return {
                form: {
                    artist_id: this.artistId,
                    title: this.song.title,
                    release_date: this.song.release_date,
                    genre: this.song.genre,
                    duration: this.song.duration
                }
            }
        },
        emits: ["handleSubmit", "handleClose"],
        methods: {
            async saveChanges() {
                const url = `${import.meta.env.VITE_BASE_URL}/song/${this.song.id}/update/`
                console.log(url)
                await axios(url, {
                    method: 'put',
                    headers: {
                        "Content-Type": "application/json",
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
        }
        
    }
</script>
