<template>
        <main class="container mx-auto px-6 py-8">
            <div class="bg-white rounded-lg shadow-lg p-6">
                <div class="flex justify-between items-center">
                    <h1 class="text-3xl font-bold mb-6">Edit Artist Profile</h1>
                    <div>
                        <button @click="$emit('handleClose')" class="bg-red-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Close</button>
                    </div>
                </div>

                <form @submit.prevent="updateProfile">
                    <div class="mb-6">
                        <label for="profile-picture" class="block text-gray-700 font-medium mb-2">Profile Picture</label>
                        <input type="file" id="profile-picture" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>

                    <div class="flex flex-col md:flex-row">
                        <div class="w-full md:w-1/2  mb-6">
                            <label for="first-name" class="block text-gray-700 font-medium mb-2">First Name</label>
                            <input v-model="form.first_name" type="text" id="first-name" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter first name">
                        </div>

                        <div class="w-full md:w-1/2 mb-6">
                            <label for="last-name" class="block text-gray-700 font-medium mb-2">Last Name</label>
                            <input v-model="form.last_name" type="text" id="last-name" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter last name">
                        </div>
                    </div>

                    <div class="mb-6">
                        <label for="email" class="block text-gray-700 font-medium mb-2">Email Address</label>
                        <input v-model="form.email" type="email" id="email" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="youremail@gmail.com">
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
                        <select id="gender" v-model="form.gender" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                            <option value="male">Male</option>
                            <option value="female">Female</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <div class="mb-6">
                        <label for="nationality" class="block text-gray-700 font-medium mb-2">Nationality</label>
                        <input type="text" v-model="form.nationality" id="nationality" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter nationality">
                    </div>

                    <div class="mb-6">
                        <label for="biography" class="block text-gray-700 font-medium mb-2">Biography</label>
                        <textarea id="biography" v-model="form.biography" rows="5" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Enter artist biography"></textarea>
                    </div>

                    <div class="mb-6">
                        <label for="social-media" class="block text-gray-700 font-medium mb-2">Social Media Links</label>
                        <input type="text" id="twitter" v-model="form.twitter_link" class="block w-full mb-2 text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Twitter URL">
                        <input type="text" id="facebook" v-model="form.facebook_link" class="block w-full mb-2 text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Facebook URL">
                        <input type="text" id="instagram"  v-model="form.instagram_link" class="block w-full text-gray-900 border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" placeholder="Instagram URL">
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
            artist: {
                type: Object,
                required: true
            }
        },
        data() {
            return  {
                form: {
                    first_name: this.artist.fullname.split(' ')[0],
                    last_name: this.artist.fullname.split(' ')[1],
                    email: this.artist.email,
                    stagename: this.artist.stagename,
                    dob: this.artist.dob,
                    gender: this.artist.gender,
                    nationality: this.artist.nationality,
                    biography: this.artist.biography,
                    twitter_link: this.artist.twitter_link,
                    facebook_link: this.artist.facebook_link,
                    instagram_link: this.artist.instagram_link,
                }
            }
        },
        emits: ["handleClose", "handleSubmit"],
        methods: {
            async updateProfile() {
                const url = `${import.meta.env.VITE_BASE_URL}/user/update_artist/${this.artist.id}/`
                console.log(url)
                await axios(url, {
                    method: 'put',
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
        }
        
    }
</script>
