<template>
    <!-- <div class="bg-gray-100 flex flex-wrap justify-around">
    </div> -->
    <h2 class="text-2xl font-bold m-4">Songs</h2>
    <section class="mb-8 flex flex-wrap justify-between">
        <Card v-for="song in songs" :song="song" />
  </section>
</template>

<script>
    import Card from './Song.vue'

    export default {
        props: {
            songs: Array
        },
        components: {
            Card
        },
    }
</script>