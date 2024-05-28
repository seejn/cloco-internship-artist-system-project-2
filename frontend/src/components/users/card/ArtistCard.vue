<template>

    <div class="w-full md:w-1/3 lg:w-1/4  m-5 rounded overflow-hidden shadow-lg bg-white">
        <img class="w-full" src="https://via.placeholder.com/150" alt="Artist Image">
        <div class="px-6 py-4">
          <RouterLink :to="'/artist/profile/'+this.artist.id" class="font-bold text-xl mb-2">{{ artist.fullname }}</RouterLink>
          <p class="text-gray-700 text-base">
            Brief description about the artist. This section can include information about their genre, style, or notable achievements.
          </p>
        </div>
    </div>
      
</template>

<script>
 export default {
    props: {
      artist: {
        type: Object,
        required: true,
      }
    }
  }
</script>