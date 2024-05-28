import { createStore } from 'vuex'
import axios from 'axios'
import router from '../router.js'

export default createStore({
    state() {
        return {
            isLoggedIn: Boolean(window.localStorage.getItem("authUser")),
            // userId: null,
            user: JSON.parse(window.localStorage.getItem("authUser")) || {},
            role:  window.localStorage.getItem("role"),
            songs: [],
            artists: {},

            toasts: []
        }
    }, 

    mutations: {
        setUser(state, user){
            state.user = user
        },
        setSongs(state, songs) {
            state.songs = songs
        }, 
        setArtists(state, artists) {
            state.artists = artists
        },

        addToast(state, toast) {

            state.toasts.push({
                id: Math.random() * 1000,
                ...toast
            })
        },
        clearToast(state, toast) {
            const index = state.toasts.findIndex((t) => t.id === toast.id)
            state.toasts.splice(index, 1)
        }

    },
    
    actions: {
        async authenticateUser(context) {
            console.log("store authenticateUser")
            await axios(`${import.meta.env.VITE_BASE_URL}/authenticate/user/`,{
                method: 'post',
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${context.state.user.access}` 
                    // "Authorization": `Bearer 8ab56c65087f9bb6d59f0ffb906b6b4632025d1147eff08cf95dcf0f672999dd` 
                }
            })
            .then((response) => {
                console.log(response.data)
                context.commit("setLoggedInState", true)
                context.commit("setUser", response.data.data)
                context.commit("addToast", {
                    title: "Login Success",
                    isError: false,
                    message: response.data.message
                })
            })
            .catch((error) => {
                console.log(error.response.data)
            })
        },
        async signOut(context) {
            const url = `${import.meta.env.VITE_BASE_URL}/user/sign_out/`
            await axios(url, {
                method: 'post',
                headers: {
                    'Authorization': `Bearer ${context.state.user.access}`
                }
            })
            .then((response) => {
                window.localStorage.removeItem("authUser")
                window.localStorage.removeItem("access_token")
                window.localStorage.removeItem("role")
                context.state.isLoggedIn = false
                context.state.role = ""
                context.commit("addToast", {
                    title: response.statusText,
                    isError: false,
                    message: response.data.message
                })
                router.push('/')
            })
            .catch((error) => {
                console.log("signout error: ", error)
                context.commit("addToast", {
                    title: error.response.statusText,
                    isError: true,
                    message: error.response.data.message
                })
            })
        },  
        async fetchSongs(context) {

            const url = `${import.meta.env.VITE_BASE_URL}/song/get_all_songs/`
            await axios(url, {
                method: "get",
            })
            .then((response) => {
                context.commit("setSongs", response.data.data)
            })
            .catch((error) => {
                console.log(error)
            })
        },
        async fetchArtists(context) {

            const url = `${import.meta.env.VITE_BASE_URL}/user/get_all_artists/`
            await axios(url, {
                method: "get",
                headers: {
                    "Authorization": `Bearer ${window.localStorage.getItem("access_token")}` 
                }
            })
            .then((response) => {
                context.commit("setArtists", response.data.data)
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
})