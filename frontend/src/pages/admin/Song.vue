<template>
    <PageLayout>
        <template #main>
            <span v-if="!isAdding">
                <main class="container mx-auto px-6 py-8">
                    <h1 class="text-3xl font-bold mb-6">Song Management</h1>
    
                    <div class="mb-6">
                        <button @click="toggleAdding" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Add New Song</button>
                    </div>
    
                    <div class="bg-white rounded-lg shadow-lg overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Artist</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Release Date</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Genre</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr v-for="(song, index) in songs">
                                    <td class="px-6 py-4 whitespace-nowrap">{{ index+1 }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">{{ song.title }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">{{ song.artist.fullname }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">{{ song.release_date }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">{{ song.genre }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <a href="#" class="text-red-600 hover:text-red-900">Delete</a>
                                        <span class="mx-2 text-gray-400">|</span>
                                        <RouterLink :to="`/admin/song/detail/${song.id}`" class="text-blue-600 hover:text-blue-900">View Details</RouterLink>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </main>
            </span>
            <span v-else="isAdding">
                <CreateSong @handleClose="toggleAdding" />
            </span>
        </template>
    </PageLayout>
</template>
       
<script>
    import CreateSong from '../../components/songs/forms/CreateSong.vue';

    export default {
        components: {
            CreateSong,
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
        },
        computed: {
            songs() {
                return this.$store.state.songs
            }
        },
        mounted() {
            this.$store.dispatch("fetchSongs")
        }
    }
</script>
