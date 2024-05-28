<template>
    <PageLayout>
        <template #main>
            <main class="container mx-auto px-6 py-8">
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <div class="mb-6">
                        <h1 class="text-3xl font-bold">Playlist Title</h1>
                        <p class="text-gray-600">Description of the playlist. This section can include details about the theme, mood, or purpose of the playlist.</p>
                        <p class="text-gray-600 mt-2">Created by <span class="font-semibold">User Name</span></p>
                    </div>

                    <div class="space-y-4">
                        <div class="bg-gray-100 rounded-lg shadow-lg p-4 flex items-center justify-between">
                            <div>
                                <h3 class="text-lg font-semibold">Song Title</h3>
                                <p class="text-gray-600">Artist Name</p>
                            </div>
                            <div class="flex space-x-4">
                                <button class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Play</button>
                                <button class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-700">Add to Playlist/Favorites</button>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </template>
    </PageLayout>
</template>
