<template>
    <PageLayout>
        <template #main>
            <main class="container mx-auto px-6 py-8">
                <!-- <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="bg-white rounded-lg shadow-lg p-6">
                        <h2 class="text-xl font-bold mb-4">Total Artists</h2>
                        <p class="text-3xl font-bold text-blue-500">250</p>
                    </div>
    
                    <div class="bg-white rounded-lg shadow-lg p-6">
                        <h2 class="text-xl font-bold mb-4">Total Songs</h2>
                        <p class="text-3xl font-bold text-blue-500">1,500</p>
                    </div>
    
                    <div class="bg-white rounded-lg shadow-lg p-6">
                        <h2 class="text-xl font-bold mb-4">Total Albums</h2>
                        <p class="text-3xl font-bold text-blue-500">100</p>
                    </div>
    
                    <div class="bg-white rounded-lg shadow-lg p-6">
                        <h2 class="text-xl font-bold mb-4">Total Users</h2>
                        <p class="text-3xl font-bold text-blue-500">500</p>
                    </div>
                </div> -->
    
                <div class="mt-8">
                    <canvas id="salesChart" width="400" height="200"></canvas>
                </div>
    
                <!-- <div class="mt-8">
                    <h2 class="text-xl font-bold mb-4">Recent Activities</h2>
                    <div class="bg-white rounded-lg shadow-lg overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Activity</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr>
                                    <td class="px-6 py-4 whitespace-nowrap">2024-05-20</td>
                                    <td class="px-6 py-4 whitespace-nowrap">Created a new song</td>
                                    <td class="px-6 py-4 whitespace-nowrap">Admin User</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div> -->
            </main>
        </template>
    </PageLayout>
</template>
       
