<template>
    <div class="bg-gray-100 text-gray-900">
        <Header />
        <slot name="main"></slot>
        <Footer />
    </div>
</template>

<script>
    import Header from '../components/header/Header.vue/'
    import Footer from '../components/footer/Footer.vue/'

    export default {
        components: {
            Header,
            Footer
        }
    }
</script>