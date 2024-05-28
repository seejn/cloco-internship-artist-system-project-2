import { createRouter, createWebHistory } from 'vue-router'

import ListSongs from './pages/ListSongs.vue'
import ListArtists from './pages/ListArtists.vue'
import SignIn from './pages/SignIn.vue'
import SignUp from './pages/SignUp.vue'

import ArtistHomePage from './pages/artist/HomePage.vue'
import ArtistProfilePage from './pages/artist/ProfilePage.vue'
import SongDetailPage from './pages/song/DetailPage.vue'
import SongPlaylistPage from './pages/song/PlaylistPage.vue'

import Dashboard from './pages/admin/Dashboard.vue'
import Artist from './pages/admin/Artist.vue'
import Song from './pages/admin/Song.vue'

import store from './store/store.js'

const routes = [
    {
        path: '/',
        component: ListSongs,
    },
    {
        path: '/listartists',
        component: ListArtists,
    },
    {
        path: '/signin',
        component: SignIn,
    },
    {
        path: '/signup',
        component: SignUp,
    },
    {
        path: '/admin/dashboard',
        component: Dashboard,
    },
    {
        path: '/admin/artist',
        component: Artist,
    },
    {
        path: '/admin/songs',
        component: Song,
    },
    {
        path: '/admin/artist/profile/:artistId',
        component: ArtistProfilePage,
    },
    {
        path: '/admin/song/detail/:songId',
        component: SongDetailPage,
    },
    {
        path: '/artist/home',
        component: ArtistHomePage,
    },
    {
        path: '/artist/profile/:artistId',
        component: ArtistProfilePage,
    },
    {
        path: '/artist/listsongs',
        component: ListSongs,
    },
    {
        path: '/artist/listartists',
        component: ListArtists,
    },
    {
        path: '/song/detail/:songId',
        component: SongDetailPage,
    },
    {
        path: '/song/playlist',
        component: SongPlaylistPage,
    },
    {
        path: '/not-found',
        component: () => import('./pages/NotFound.vue'),
    },
]

const router =  createRouter({
    history: createWebHistory(),
    routes
})

// router.beforeEach((to, from, next) => {

//     if(to.path === '/not-found') next()

//     const isLoggedIn = store.state.isLoggedIn
//     if(!isLoggedIn && to.path === '/') next()
//     if(!isLoggedIn) next('/')

//     const authUser = JSON.parse(window.localStorage.getItem("authUser"))

//     let allRoutes = []
//     let adminRoutes = []
//     let artistRoutes = []
//     const excludeRoutes = ['not-found']

//     for(const route of routes) {
//         const path = route.path.split('/')[1]
//         if(!excludeRoutes.includes(path)) allRoutes.push(route.path)
        
//         if(path === "admin") adminRoutes.push(route.path)
//         else if(path === "artist") artistRoutes.push(route.path)
//     }

//     console.log("allRoutes:", allRoutes)
//     console.log("adminRoutes:", adminRoutes)
//     console.log("artistRoutes:", artistRoutes)

//     console.log("to: ", to.path)

//     if(!allRoutes.includes(to.path)){
//         console.log("form all routes check")
//         next('/not-found')
//     }
//     else if(!authUser.is_admin && adminRoutes.includes(to.path)) {
//         console.log("form admin routes check")
//         next('/not-found')
//     }
//     else if(!authUser.is_user && artistRoutes.includes(to.path)) {
//         console.log("form artist routes check")
//         next('/not-found')
//     }not-found')
//     else{
//         next()
//     }
// })

router.beforeEach((to, from, next) => {

    console.log("to", to.path)
    const isLoggedIn = store.state.isLoggedIn

    if(!isLoggedIn || to.path === '/not-found') {
        next()
    }
    const authUser = JSON.parse(window.localStorage.getItem("authUser"))

    let adminRoutes = []
    let artistRoutes = []
    let remainingRoutes = []
    const excludeRoutes = ['not-found']
    
    for(const route of routes) {
        const path = route.path.split('/')[1]
        
        if(path === "admin") adminRoutes.push(route.path)
        else if(path === "artist") artistRoutes.push(route.path)
        else remainingRoutes.push(route.path)
    }
    
    // console.log("allRoutes:", allRoutes)
    // console.log("adminRoutes:", adminRoutes)
    // console.log("artistRoutes:", artistRoutes)
    
    // console.log("to: ", to.path)
    // console.log("authUser: ", authUser)
    

    console.log(!authUser.data.is_artist)
    console.log(!authUser.data.is_artist)
    console.log(/artist/gm.test(to.path))
    if(!authUser.data.is_admin && adminRoutes.includes(to.path)) {
        console.log("form admin routes check")
        next('/not-found')
    }
    else if(!authUser.data.is_artist && artistRoutes.includes(to.path)) {
        console.log("form artist routes check")
        next('/not-found')
    }
    
    next()
})

export default router