import axios from 'axios';

export async function fetchSongs() {

    const url = `${import.meta.env.VITE_BASE_URL}/song/get_all_songs/`
    await axios(url, {
        method: "get",
    })
    .then((response) => {
        return response.data.data
    })
    .catch((error) => {
        console.log(error)
    })
}
export async function fetchArtists() {

    const url = `${import.meta.env.VITE_BASE_URL}/user/get_all_artists/`
    await axios(url, {
        method: "get",
        headers: {
            "Authorization": `Bearer ${window.localStorage.getItem("access_token")}` 
        }
    })
    .then((response) => {
        return response.data.data
    })
    .catch((error) => {
        console.log(error)
    })
}