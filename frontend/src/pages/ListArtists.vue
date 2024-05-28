<template>
    <PageLayout>
        <template #main>
            <Artists />
        </template>
    </PageLayout>
</template>

<script>
    import Artists from '../components/users/card/ArtistCards.vue'

    export default {
        components: {
            Artists
        }
    }
</script>