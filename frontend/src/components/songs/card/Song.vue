<template>
          <div class="m-5 w-full md:w-1/3 lg:w-1/4 bg-white rounded-lg shadow-lg overflow-hidden">
              <img src="https://via.placeholder.com/300" alt="Album Art" class="w-full h-40 object-cover">
              <div class="p-4">
                  <p>
                    <RouterLink :to="'/song/detail/'+song.id" class="text-lg font-semibold">{{ song.title }}</RouterLink>
                  </p>
                  <p>
                    <RouterLink :to="'/artist/profile/' + song.artist.id" class="text-gray-600">{{ song.artist.fullname }}</RouterLink>
                  </p>
              </div>
          </div>
    <!-- <div class="m-2 w-1/3 bg-white shadow-lg rounded-lg overflow-hidden flex">
        <div class="w-1/3">
          <img class="w-full h-full object-cover" src="https://placehold.jp/150x50.png" alt="Song Image">
        </div>
        <div class="w-2/3 p-6 flex flex-col justify-between">
          <div>
            <h2 class="text-2xl font-bold text-gray-900 mb-2">{{ song.title }}</h2>
            <p class="text-gray-700 mb-4">{{ song.artist.fullname }}</p>
          </div>
          <div class="flex items-center mt-4">
            <img class="w-12 h-12 rounded-full object-cover" src="https://placehold.jp/150x50.png" alt="Singer Image">
            <div class="ml-3">
              <p class="text-gray-900 leading-none">{{ song.artist.fullname }}</p>
              <p class="text-gray-600">Additional Info</p>
            </div>
          </div>
      </div>
    
    </div> -->
</template>

<script>
  export default {
    props: {
      song: {
        type: Object,
        required: true,
      }
    }
  }
</script>
