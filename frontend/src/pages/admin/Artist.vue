<template>
    <PageLayout>
        <template #main>
            <span v-if="isAdding">
                <CreateArtist @handleClose="toggleAdding" />
            </span>
            <span v-else="!isAdding">
                <main class="container mx-auto px-6 py-8">
                    <h1 class="text-3xl font-bold mb-6">Artist Management</h1>
    
                    <div class="mb-6">
                        <button @click="toggleAdding" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Add New Artist</button>
                    </div>
    
                    <div class="bg-white rounded-lg shadow-lg overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Songs</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
    
                                <tr v-for="(artist, index) in artists" :key="artist.id">
                                    <td class="px-6 py-4 whitespace-nowrap">1</td>
                                    <td class="px-6 py-4 whitespace-nowrap">{{ artist.fullname }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">{{ artist.songs_count }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <a @click="deleteArtist(artist.id)" class="cursor-pointer text-red-600 hover:text-red-900">Delete</a>
                                        <span class="mx-2 text-gray-400">|</span>
                                        <RouterLink :to="`/admin/artist/profile/${artist.id}`" class="cursor-pointer text-blue-600 hover:text-blue-900">View Details</RouterLink>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </main>
            </span>
        </template>
    </PageLayout>
</template>

<script>
    import CreateArtist from '../../components/users/forms/CreateArtist.vue'
    import axios from 'axios'

    export default {
        components: {
            CreateArtist
        },
        data() {
            return{
                isAdding: false
            }
        },
        methods: {
            toggleAdding() {
                this.isAdding = !this.isAdding
            },
            async deleteArtist(id) {
                
                const  url = `${import.meta.env.VITE_BASE_URL}/user/update_artist/${id}/`
                axios(url, {
                    method: 'put',
                    headers: {
                        "Authorization": `Bearer ${this.authUser.access}`
                    },
                    data: {
                        is_deleted: true
                    }
                })
                .then((response) => {
                    console.log(response.data)

                    this.$store.commit("addToast", {
                        title: response.statusText,
                        isError: false,
                        message: "Artist Deleted Successfully"
                    })
                })
                .catch((error) => {
                    console.log(error)
                })

                const updated_artists = this.artists.filter((artist) => artist.id !== id)
                this.$store.state.artists = updated_artists

            }
        },
        computed: {
            authUser() {
                return this.$store.state.user
            },
            artists() {
                return this.$store.state.artists
            }
        },
        mounted() {
            this.$store.dispatch("fetchArtists")
        }
    }
</script>