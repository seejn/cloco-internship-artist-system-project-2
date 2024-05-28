<template>
        <main class="container mx-auto px-6 py-8">
            <div class="bg-white rounded-lg shadow-lg p-6">
                <div class="flex justify-between items-center">
                    <h1 class="text-3xl font-bold mb-6">Add New Artist</h1>
                    <div>
                        <button @click="$emit('handleClose')" class="bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Close</button>
                    </div>
                </div>

                <form @submit.prevent="createArtist">
                    <div class="mb-6">
                        <label for="profile-picture" class="block text-gray-700 font-medium mb-2">Profile Picture</label>
                        <input type="file" id="profile-picture" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>

                    <div class="flex">
                        <div class="mb-6 me-3 w-1/2">
                            <label for="first-name" class="block text-gray-700 font-medium mb-2">First Name</label>
                            <input v-model="form.first_name" type="text" id="first-name" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter first  name">
                        </div>
                        <div class="mb-6 ms-3 w-1/2">
                            <label for="last-name" class="block text-gray-700 font-medium mb-2">Last Name</label>
                            <input v-model="form.last_name" type="text" id="last-name" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter last name">
                        </div>
                    </div>

                    <div class="mb-6">
                        <label for="email" class="block text-gray-700 font-medium mb-2">Email</label>
                        <input v-model="form.email" type="email" id="stage-name" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="youremail@email.com">
                    </div>

                    <div class="mb-6">
                        <label for="stage-name" class="block text-gray-700 font-medium mb-2">Stage Name</label>
                        <input v-model="form.stagename" type="text" id="stage-name" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter stage name">
                    </div>

                    <div class="mb-6">
                        <label for="dob" class="block text-gray-700 font-medium mb-2">Date of Birth</label>
                        <input v-model="form.dob" type="date" id="dob" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>

                    <div class="mb-6">
                        <label for="gender" class="block text-gray-700 font-medium mb-2">Gender</label>
                        <select v-model="form.gender" id="gender" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                            <option value="" disabled selected>Select gender</option>
                            <option value="male">Male</option>
                            <option value="female">Female</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <div class="mb-6">
                        <label for="nationality" class="block text-gray-700 font-medium mb-2">Nationality</label>
                        <input v-model="form.nationality" type="text" id="nationality" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter nationality">
                    </div>

                    <div class="mb-6">
                        <label for="biography" class="block text-gray-700 font-medium mb-2">Biography</label>
                        <textarea v-model="form.description" id="biography" rows="5" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter artist biography"></textarea>
                    </div>

                    <div class="mb-6">
                        <label for="social-media" class="block text-gray-700 font-medium mb-2">Social Media Links</label>
                        <input v-model="form.twitter_link" type="text" id="twitter" class="block w-full mb-2 text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Twitter URL">
                        <input v-model="form.facebook_link" type="text" id="facebook" class="block w-full mb-2 text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Facebook URL">
                        <input v-model="form.instagram_link" type="text" id="instagram" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Instagram URL">
                    </div>

                    <div>
                        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Create Profile</button>
                    </div>
                </form>
            </div>
        </main>

</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                form: {
                    first_name: '',
                    last_name: '',
                    email: '',
                    stagename: '',
                    dob: '',
                    gender: '',
                    nationality: '',
                    description: '',
                    twitter_link: '',
                    instagram_link: '',
                    facebook_link: '',
                }
            }
        },
        computed: {
            authUser() {
                return this.$store.state.user
            }
        },
        methods: {
            async createArtist() {
                // const updatedArtists = [...this.$store.state.artists, this.form]
                // this.$store.state.artists = updatedArtists

                const url = `${import.meta.env.VITE_BASE_URL}/user/create_artist/`
                await axios(url, {
                    method: 'post',
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${this.authUser.access}`
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
    }
</script>