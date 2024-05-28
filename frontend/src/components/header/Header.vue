<template>
        <Toasts />
        <span v-if="$store.state.role!=='admin'">

            <header class="bg-gray-800 text-white">
                <div class="container mx-auto flex justify-between items-center py-4 px-6">
                    <div class="text-2xl font-bold">MusicApp</div>
                    <nav class="space-x-4 flex">
                        <RouterLink to="/artist/home" class="p-2 rounded-lg hover:text-gray-400">Home</RouterLink>
                        <RouterLink to="/artist/listsongs" class="p-2 rounded-lg hover:text-gray-400">Songs</RouterLink>
                        <RouterLink to="/artist/listartists" class="p-2 rounded-lg hover:text-gray-400">Artists</RouterLink>
                        <span v-if="!isLoggedIn" class="p-2">
                            <RouterLink to="/signin" class="bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Sign In</RouterLink>
                        </span>
                        <span v-else="isLoggedIn">
                            <div class="relative ml-3" @click="toggleMenu">
                                <div>
                                    <button type="button" class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                                    <img class="h-8 w-8 rounded-full" src="https://via.placeholder.com/150" alt="">
                                    </button>
                                </div>
                                <div :class="menuToggleClassObject" class="absolute right-0 z-10 mt-4 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                                    <RouterLink :to="'/artist/profile/'+this.user.data.id" class="block px-4 py-2 text-sm text-gray-700 hover:bg-zinc-300" role="menuitem" tabindex="-1" id="user-menu-item-0">Your Profile</RouterLink>
                                    <p @click="this.$store.dispatch('signOut')" class="block px-4 py-2 text-sm text-gray-700 hover:bg-zinc-300" role="menuitem" tabindex="-1" id="user-menu-item-2">Sign out</p>
                                </div>
                            </div>
                        </span>
                    </nav>
                </div>
                
            </header>
        </span>

        <span v-else="role=='admin'">
            <header class="bg-gray-800 text-white">
                <div class="container mx-auto flex justify-between items-center py-4 px-6">
                    <div class="text-2xl font-bold">MusicApp</div>
                    <nav class="space-x-4 flex items-center nav-menu">
                        <RouterLink to="/admin/dashboard" class="p-2 rounded-lg hover:text-gray-400">Dashboard</RouterLink>
                        <RouterLink to="/admin/artist" class="p-2 rounded-lg hover:text-gray-400">Manage Artists</RouterLink>
                        <RouterLink to="/admin/songs" class="p-2 rounded-lg hover:text-gray-400">Manage Songs</RouterLink>
                        <span v-if="!isLoggedIn" class="p-2">
                            <RouterLink to="/signin" class="bg-indigo-600 hover:bg-slate-900 text-white py-1 px-4 rounded">Sign In</RouterLink>
                        </span>
                        <span v-else="isLoggedIn">
                            <div class="relative ml-3" @click="toggleMenu">
                                <div>
                                    <button type="button" class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                                    <img class="h-8 w-8 rounded-full" src="https://via.placeholder.com/150" alt="">
                                    </button>
                                </div>
                                <div :class="menuToggleClassObject" class="absolute right-0 z-10 mt-4 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                                    <RouterLink :to="'/artist/profile/'+this.user.data.id" class="block px-4 py-2 text-sm text-gray-700 hover:bg-zinc-300" role="menuitem" tabindex="-1" id="user-menu-item-0">Your Profile</RouterLink>
                                    <p @click="this.$store.dispatch('signOut')" class="block px-4 py-2 text-sm text-gray-700 hover:bg-zinc-300" role="menuitem" tabindex="-1" id="user-menu-item-2">Sign out</p>
                                </div>
                            </div>
                        </span>
                    </nav>
                </div>
                
            </header>
        </span>

</template>

<script>
import { RouterLink } from 'vue-router';

export default {
    data() {
        return {
            profileIcon: true,
        }
    },
    methods: {
        toggleMenu() {
            this.profileIcon = !this.profileIcon
        },
    },
    computed: {
        user() {
            console.log("headers user", this.$store.state.user)
            return this.$store.state.user
        },
        isLoggedIn() {
            return this.$store.state.isLoggedIn
        },
        menuToggleClassObject() {
            return{
                "hidden": this.profileIcon
            }
        }
    },
    watch: {
        user(newValue, oldValue){},
    },
   
}
</script>

<style scoped>
    .router-link-active{
        background-color: rgb(17 24 39);
    }
</style>